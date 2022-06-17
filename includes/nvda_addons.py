import requests
import wx
import json
import os
import subprocess
from webbrowser import open as OPEN
from pyperclip import copy
from . import speak
from threading import Thread
from wx.lib.newevent import NewEvent
from settingsconfig import get

download_path=get("DownloadAddonsPath")
url="http://blindgamers.net/easytoolkit/addons_names.txt"
jurl=""
addons={}
say=speak.say
ProgressChangedEvent, EVT_PROGRESS_CHANGED = NewEvent()
DownloadFinishedEvent, EVT_DOWNLOAD_FINISHED = NewEvent()

def SetUrl():
	global jurl
	try:
		r1=requests.get("http://blindgamers.net/easytoolkit/addons.json", timeout=5)
		jurl="http://blindgamers.net/easytoolkit/addons.json"
		return
	except:
		jurl="http://raw.githubusercontent.com/abdallah-hader/json-files-for-easy-toolkit/main/addons.json"

def PageUrlLanguage(url):
	lang=get("language")
	link=url.replace("\"lng\"", lang)
	return link


class GetNvdaAddons(wx.Dialog):
	def __init__(self, parent):
		wx.Dialog.__init__(self, parent, id=-1, title=_("download nvda addons tool"))
		p=wx.Panel(self)
		self.Center()
		self.ih=wx.StaticText(p, -1, _("addons list"))
		self.addons_list=wx.ListBox(p, -1)
		if not get("hideclosebutton"):
			self.close=wx.Button(p, -1, _("&close"))
			self.close.Bind(wx.EVT_BUTTON, lambda event: self.Destroy())
		self.SetupContextMenu()
		say(_("loading."))
		thread=Thread(target=self.addons_data)
		thread.demon=True
		thread.start()
		self.Bind(wx.EVT_CHAR_HOOK, self.shortcuts)

	def addons_data(self):
		SetUrl()
		items=[]
		global addons
		try:
			addonsget=requests.get(jurl)
			if addonsget.status_code !=200:
				wx.MessageBox(_("An error occurred while getting data, there may be a connection problem, or a temporary server problem, if you are sure that you are connected to the Internet, contact the developer to solve the problem."), _("error"), style=wx.ICON_ERROR, parent=wx.GetApp().GetTopWindow())
				return
			addons=addonsget.json()
			for name in addons.keys():
				items.append(name)
			items.sort()
			wx.CallAfter(self.addons_list.Set, items)
			wx.CallAfter(self.ih.SetLabel, _("addons list, contains {} addons").format(len(items)))
			say(_("loading complete"))
#			print("connected to {}".format(jurl))
		except requests.ConnectionError:
			wx.MessageBox(_("An error occurred while getting data, there may be a connection problem, or a temporary server problem, if you are sure that you are connected to the Internet, contact the developer to solve the problem."), _("error"), style=wx.ICON_ERROR, parent=wx.GetApp().GetTopWindow())

	def download(self):
		name=self.addons_list.GetStringSelection()
		link=addons[name][2]
		if os.path.exists(f"{download_path}/{self.addons_list.GetStringSelection()}.nvda-addon"):
			msg=wx.MessageBox(_("A file for this addon was found in the addons download path. Do you want to re-download it?"), _("alert"), style=wx.YES_NO, parent=self)
			if msg==wx.YES:
				wx.CallAfter(download, wx.GetApp().GetTopWindow(), name, link)
			else:
				return
		else:
			wx.CallAfter(download, wx.GetApp().GetTopWindow(), name, link)

	def SetupContextMenu(self):
		self.menu=wx.Menu()
		self.Open=self.menu.Append(-1, _("open"))
		self.show=self.menu.Append(-1, _("show in folder"))
		OpenInBrowser=self.menu.Append(-1, _("open in &browser"))
		cpl=self.menu.Append(-1, _("copy download link"))
		cpl2=self.menu.Append(-1, _("Copy addon &page link"))
		def popup():
			if self.addons_list.Selection==-1:
				return
			addonpath=f"{download_path}/{self.addons_list.GetStringSelection()}.nvda-addon"
			self.Open.Enable(enable=False) 		if not os.path.exists(addonpath)else self.Open.Enable(enable=True)
			self.PopupMenu(self.menu)
		self.Bind(wx.EVT_CONTEXT_MENU, lambda e:popup())
		self.Bind(wx.EVT_MENU, self.OpenAddon, self.Open)
		self.Bind(wx.EVT_MENU, self.ShowInFolder, self.show)
		self.Bind(wx.EVT_MENU, self.CopyPageLink, cpl2)
		self.Bind(wx.EVT_MENU, self.CopyDownloadLink, cpl)
		self.Bind(wx.EVT_MENU, self.OpenInBrowser, OpenInBrowser)

	def CopyDownloadLink(self, event):
		copy(addons[self.addons_list.GetStringSelection()][2])

	def CopyPageLink(self, event):
		copy(PageUrlLanguage(addons[self.addons_list.GetStringSelection()][3]))

	def OpenInBrowser(self, event):
		open(PageUrlLanguage(addons[self.addons_list.GetStringSelection()][3]))

	def OpenAddon(self, event):
		addonpath=f"{download_path}/{self.addons_list.GetStringSelection()}.nvda-addon"
		os.startfile(addonpath)

	def ShowInFolder(self, event):
		addon=self.addons_list.GetStringSelection()
		subprocess.run(f"explorer /select, {download_path}\\{addon}.nvda-addon")

	def shortcuts(self, event):
		item=self.addons_list.GetStringSelection()
		key=event.GetKeyCode()
		if key==wx.WXK_F1:
			say(_("addon name: {name},\n The version of NVDA required to run the addon {rver}, \ndescription: {description}.").format(name=item, rver=addons[item][0], description=addons[item][1]))
		elif key == wx.WXK_RETURN and self.FindFocus()==self.addons_list and self.addons_list.Strings!="":
			self.download()
		elif key==wx.WXK_LEFT and self.FindFocus()==self.addons_list and self.addons_list.Selection!=-1 or key ==wx.WXK_RIGHT and self.FindFocus()==self.addons_list and self.addons_list.Selection!=-1:
			return say(item)
		if key==wx.WXK_ESCAPE:
			if get("escapetoback"):
				self.Destroy()
		event.Skip()


class download(wx.Dialog):
	def __init__(self, parent, addonname, url):
		wx.Dialog.__init__(self, parent, id=-1, title=_("Downloading {}").format(addonname))
		p=wx.Panel(self)
		self.Center()
		self.fname=addonname
		self.path=f"{download_path}\{self.fname}.nvda-addon"
		wx.StaticText(p, -1, _("download status"))
		self.download_status=wx.TextCtrl(p, -1, style=wx.TE_READONLY|wx.HSCROLL)
		cancelButton = wx.Button(p, wx.ID_CANCEL, _("cancel"))
		self.ProgressBar=wx.Gauge(p, -1, range=100)
		self.ProgressBar.Bind(EVT_PROGRESS_CHANGED, self.onChanged)
		self.Bind(EVT_DOWNLOAD_FINISHED, self.onFinished)
		cancelButton.Bind(wx.EVT_BUTTON, self.onCancel)
		self.Bind(wx.EVT_CLOSE, self.onClose)
		thread=Thread(target=self.download_addon, args=[url])
		thread.demon=True
		thread.start()
		self.download = True
		self.ShowModal()

	def download_addon(self, url):
		if not os.path.exists(download_path):
			os.mkdir(download_path)
		name = os.path.join(download_path, self.fname+".nvda-addon")
		try:
			with requests.get(url, stream=True) as r:
				if r.status_code != 200:
					self.errorAction()
					return
				size = r.headers.get("content-length")
				try:
					size = int(size)
				except TypeError:
					self.errorAction()
					return
				recieved = 0
				progress = 0
				with open(name, "wb") as file:
					for part in r.iter_content(1024):
						file.write(part)
						if not self.download:
							file.close()
							os.remove("""{}""".format(download_path+"\\"+self.fname+".nvda-addon"))
							self.Destroy()
							return
						recieved += len(part)
						progress = int(
							(recieved/size)*100
						)
						wx.PostEvent(self.ProgressBar, ProgressChangedEvent(value=progress))
			wx.PostEvent(self, DownloadFinishedEvent(path=name))
		except requests.ConnectionError:
			self.errorAction()

	def errorAction(self):
		wx.MessageBox(_("An error occurred during the download process, please try again later."), _("error"), style=wx.ICON_ERROR, parent=self)
		self.Destroy()

	def onChanged(self, event):
		self.ProgressBar.SetValue(event.value)
		self.download_status.SetValue(_("Downloading addon {}").format(event.value)+"%")

	def onFinished(self, event):
		wx.MessageBox(_("addon download completed successfully, addon path: {}").format(download_path+"\\"+self.fname+".nvda-addon"), _("success"), parent=self)
		self.Destroy()
		return

	def onCancel(self, event):
		self.download = False
		say(_("canceled"))

	def onClose(self, event):
		if self.download:
			message = wx.MessageBox(_("There is a download process in progress. Do you want to cancel it؟"), _("confirm"), style=wx.YES_NO, parent=self)
			if message == wx.YES:
				self.download = False
			return
		self.Destroy()