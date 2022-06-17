import requests
import wx
from threading import Thread
from wx.lib.newevent import NewEvent
import os
import json
from accessible_output2 import outputs
from includes import app_info
from settingsconfig import get
import shutil
import subprocess
import sys



ProgressChangedEvent, EVT_PROGRESS_CHANGED = NewEvent()
DownloadFinishedEvent, EVT_DOWNLOAD_FINISHED = NewEvent()
say=outputs.auto.Auto().speak
update_path=os.path.join(os.getenv("appdata"), "Easy Toolkit/updates")

def GetLang():
	if get("language")=="ar":
		return 0
	elif get("language")=="en":
		return 1
	else:
		return 1

def cfu(silent=False):
	lang=GetLang()
	url="http://blindgamers.net/easytoolkit/info.json"
	try:
		request=requests.get(url)
		if request.status_code !=200:
			wx.MessageBox(_("Unable to access the update service, there may be a temporary problem, or there may be a connection problem, please try again later."), _("error"), style=wx.ICON_ERROR, parent=wx.GetApp().GetTopWindow()) if not silent else None
			return
		info = request.json()
		if info["version"]>app_info.version:
			discription=info["discription"].split("\t")
			changes=info["changes"].split("\t")
			ask=wx.MessageBox(_("There is a new update,\n easy tool kit version {ver},\n description: {desc},\n new features: {changes},\n do you want to download the update now؟").format(desc=discription[lang], ver=info["version"], changes=changes[lang]), _("A new update has been found"), style=wx.YES_NO, parent=wx.GetApp().GetTopWindow())
			if ask==wx.YES:
				wx.CallAfter(DownloadUpdate, wx.GetApp().GetTopWindow(), info["url"])
		else:
			wx.MessageBox(_("You have the latest version of the easy tool kit"), _("information"), parent=wx.GetApp().GetTopWindow()) if not silent else None
	except requests.ConnectionError:
		wx.MessageBox(_("An error occurred while connecting to the updates service, please try again later"), _("connection error"), style=wx.ICON_ERROR, parent=wx.GetApp().GetTopWindow()) if not silent else None


class DownloadUpdate(wx.Dialog):
	def __init__(self, parent, url):
		wx.Dialog.__init__(self, parent, title=_("downloading updates"))
		p=wx.Panel(self)
		self.Center()
		wx.StaticText(p, -1, _("download status"))
		self.download_status=wx.TextCtrl(p, -1, style=wx.TE_READONLY|wx.HSCROLL)
		self.download_status.SetFocus()
		cancelButton = wx.Button(p, wx.ID_CANCEL, _("cancel"))
		self.ProgressBar=wx.Gauge(p, -1, range=100)
		self.ProgressBar.Bind(EVT_PROGRESS_CHANGED, self.onChanged)
		self.Bind(EVT_DOWNLOAD_FINISHED, self.onFinished)
		cancelButton.Bind(wx.EVT_BUTTON, self.onCancel)
		self.Bind(wx.EVT_CLOSE, self.onClose)
		Thread(target=self.updateDownload, args=[url]).start()
		self.download = True
		self.ShowModal()

	def updateDownload(self, url):
		if os.path.exists(update_path):
			shutil.rmtree(update_path)
		os.mkdir(update_path)
		name = os.path.join(update_path, url.split("/")[-1])
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
							shutil.rmtree(update_path)
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
		wx.MessageBox(_("An error occurred during the update process, please try again later.."), _("error"), style=wx.ICON_ERROR, parent=self)
		shutil.rmtree(update_path)
		self.Destroy()
	def onChanged(self, event):
		self.ProgressBar.SetValue(event.value)
		self.download_status.SetValue(_("downloading updates {}").format(event.value)+"%")

	def onFinished(self, event):
		wx.MessageBox(_("The updates have been downloaded successfully, click OK to start the installation"), _("success"), parent=self)
		try:
			self.download_status.Value = _("Installing updates")
			path = os.path.join(update_path, event.path)
			subprocess.Popen('"{}" /silent'.format(path), shell=True)
		except:
			wx.MessageBox(_("An unexpected error occurred when trying to open the file for installation, re-download the update again, and if the problem persists, contact the developer to solve it"), _("error"), style=wx.ICON_ERROR, parent=self)
			self.Destroy()
			return
		sys.exit()
	def onCancel(self, event):
		self.download = False
	def onClose(self, event):
		if self.download:
			message = wx.MessageBox(_("There is a download process in progress. Do you want to cancel it؟"), _("confirm"), style=wx.YES_NO, parent=self)
			if message == wx.YES:
				self.download = False
			return
		self.Destroy()