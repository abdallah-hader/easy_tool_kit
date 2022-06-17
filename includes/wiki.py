import wikipedia as wi
import wx
import shelve
import os
from shutil import rmtree as Delete
from threading import Thread
from time import sleep
from datetime import datetime
from settingsconfig import get
from pyperclip import copy
from webbrowser import open
from . import speak


DataPath=os.path.join(os.getenv("appdata"), "Easy Toolkit/data")
FullPath=os.path.join(os.getenv("appdata"), "Easy Toolkit/data/saved_articles")
say=speak.say

class WikiPediaSearch(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, id=-1, title=_("search in wikipedia"))
		p=wx.Panel(self)
		if get("escapetoback"):
			self.Bind(wx.EVT_CHAR_HOOK, self.OnHook)
		wx.StaticText(p, -1, _("search for?"))
		self.Field=wx.TextCtrl(p, -1, style=wx.HSCROLL)
		wx.StaticText(p, -1, _("The number of search results to display, 0 to search without specifying a number."))
		self.Count=wx.SpinCtrl(p, -1, min=0, max=100)
		self.go=wx.Button(p, -1, _("&search"))
		self.go.SetDefault()
		self.go.Bind(wx.EVT_BUTTON, self.OnSearch)
		self.random=wx.Button(p, -1, _("Show &Random Pages"))
		self.random.Bind(wx.EVT_BUTTON, lambda event :ShowResults(self, word='', count=int(self.Count.GetValue()) if int(self.Count.GetValue())>0 else None,rnd=True))
		self.saved=wx.Button(p, -1, _("Saved &Articles"))
		self.saved.Bind(wx.EVT_BUTTON, lambda event: Ofline(self).Show())
		if not get("hideclosebutton"):
			self.close=wx.Button(p, -1, _("&close"))
			self.close.Bind(wx.EVT_BUTTON, lambda event: self.Destroy())
		self.Bind(wx.EVT_CLOSE, self.OnClose)

	def OnSearch(self,event):
		c=int(self.Count.GetValue())
		word=self.Field.GetValue()
		ShowResults(self, word=word, count=c  if c>0 else None, rnd=False)
#		Thread(target=self.SearchThread).start()

	def OnClose(self,event):
		if not get("confirmation_to_exit"):
			wx.Exit()
		else:
			ask=wx.MessageBox(_("Do you want to close the program?"), _("confirmation"), style=wx.YES_NO)
			if ask==wx.YES:
				wx.Exit()

	def OnHook(self,event):
		k=event.GetKeyCode()
		if k==wx.WXK_ESCAPE:
			self.Destroy()
		event.Skip()

class ShowResults(wx.Dialog):
	def __init__(self, parent, word, count, rnd):
		wx.Dialog.__init__(self, parent, id=-1, title=_("search results for : %s")%(word))
		p=wx.Panel(self, size=self.GetSize())
		self.SetSize((250, 200))
		if get("escapetoback"):
			self.Bind(wx.EVT_CHAR_HOOK, self.OnHook)
		wi.set_lang(get("wikipedialang"))
		self.Centre()
		self.KeyWord=word
		self.CountOfResults=count
		self.rnd=rnd
		wx.StaticText(p, -1, _("List of search results"))
		self.list=wx.ListBox(p, -1)
		self.Bind(wx.EVT_MENU, self.ShowResult)
		self.Bind(wx.EVT_CHAR_HOOK, self.Shortcuts)
		wx.StaticText(p, -1, _("The result of the selected article"))
		self.TextField=wx.TextCtrl(p, -1, style=wx.TE_READONLY|wx.TE_MULTILINE|wx.HSCROLL)
		if not get("hideclosebutton"):
			self.close=wx.Button(p, -1, _("&close"))
			self.close.Bind(wx.EVT_BUTTON, lambda event: self.Destroy())
		self.SetupContextMenu()
		self.getting=False
		self.CurrentPageUrl=None

		threadsearch=Thread(target=self.start)
		threadsearch.demon=True
		threadsearch.start()
		self.ShowModal()

	def start(self):
		try:
			say(_("Searching"))
			self.getting=True
			if self.rnd:
				r=wi.random(pages=self.CountOfResults)
			else:
				r=wi.search(self.KeyWord, results=self.CountOfResults)
			if r==[]:
				wx.MessageBox(_("An error occurred while searching, please try again, Reasons: It is possible that there is no internet connection, or there may be no search results, try using other words to search."), _("error"), parent=self, style=wx.ICON_ERROR)
				wx.CallAfter(self.Destroy)
			else:
				wx.CallAfter(self.list.Append, r)
				self.getting=False
				wx.CallAfter(self.list.SetSelection, 0)
				say(_("Search completed"))
		except :
			wx.MessageBox(_("An error occurred while searching, please try again, Reasons: It is possible that there is no internet connection, or there may be no search results, try using other words to search."), _("error"), parent=self, style=wx.ICON_ERROR)
			wx.CallAfter(self.Destroy)


	def ShowResult(self,event):
		thread1=Thread(target=self.getSummary)
		thread1.demon=True
		thread1.start()
		self.getting=True

	def getSummary(self):
		if self.getting:
			say(_("Please wait while the article summary is loading"))
			return
		else:
			say(_("Article summary is being obtained, please wait"))
			txt=self.list.GetStringSelection()
			t=wi.summary(txt)
			p=wi.page(txt, auto_suggest=False)
			self.CurrentPageUrl=p.url
			wx.CallAfter(self.TextField.SetValue, t)
			say(_("loading complete"))
		self.getting=False

	def save(self,event):
		thread=Thread(target=self.setSave)
		thread.demon=True
		thread.start()

	def setSave(self):
		try:
			os.mkdir(DataPath)
		except FileExistsError:
			pass
		if self.getting:
			say(_("There is another saving process, please wait for it to complete"))
			return
		self.getting=True
		say(_("Saving..."))
		date=datetime.now()
		GetTime=str("%s/%s/%s %s:%s "%(date.day,date.month,date.year,date.hour,date.minute))
		with shelve.open(FullPath) as data:
			try:
				d=data["articles"]
			except KeyError:
				d={}
			try:
				dt=data["atf"]
			except KeyError:
				dt={}
			if not self.list.GetStringSelection() in d:
				d[self.list.GetStringSelection()] = wi.summary(self.list.GetStringSelection())
				dt[self.list.GetStringSelection()+"time"] = GetTime
				data["articles"] =d
				data["atf"] = dt
				self.getting=False
				wx.MessageBox(_("The article was saved successfully, you can access it from the saved articles list."), _("alert"), parent=self)
			else:
				wx.MessageBox(_("This article is already in the saved articles list, so it cannot be saved"), _("error"), parent=self, style=wx.ICON_ERROR)
				self.getting=False

	def Shortcuts(self,event):
		if event.GetKeyCode()==wx.WXK_F1:
			if not self.CurrentPageUrl:
				say(_("No result selected, select a result to open it in the browser"))
				return
			else:
				open(self.CurrentPageUrl)
				say(_("Opening {result} in browser").format(result=self.list.GetStringSelection()))
		elif event.GetKeyCode()==wx.WXK_F2:
			if not self.CurrentPageUrl:
				say(_("Select an article to copy its link to clipboard"))
				return
			else:
				try:
					copy(self.CurrentPageUrl)
					say(_("Article link copied: {article}").format(article=self.list.GetStringSelection()))
				except:
					say(_("Something went wrong. The article link cannot be copied to clipboard"))
		event.Skip()

	def SetupContextMenu(self):
		menu=wx.Menu()
		save=menu.Append(-1, _("save to saved articles list"))
		self.Bind(wx.EVT_MENU, self.save, save)
		self.list.Bind(wx.EVT_CONTEXT_MENU, lambda event:self.PopupMenu(menu))

	def OnHook(self,event):
		k=event.GetKeyCode()
		if k==wx.WXK_ESCAPE:
			self.Destroy()
		event.Skip()

class Ofline(wx.Dialog):
	def __init__(self,parent):
		wx.Dialog.__init__(self, parent, id=-1, title=_("Saved Articles"))
		p=wx.Panel(self)
		self.Center()
		wx.StaticText(p, -1, _("saved articles"))
		self.list=wx.ListBox(p, -1)
		self.Bind(wx.EVT_MENU, self.ArticleGet)
		wx.StaticText(p, -1, _("the Article text"))
		self.Field=wx.TextCtrl(p, -1, style=wx.TE_READONLY+wx.HSCROLL)
		self.Bind(wx.EVT_CHAR_HOOK, self.OnHook)
		self.SetupContextMenu()
		self.set()

	def ArticleGet(self,event):
		with shelve.open(FullPath) as g:
			result=g["articles"][self.list.GetStringSelection()]
			self.Field.SetValue(result)

	def set(self):
		try:
			with shelve.open(FullPath) as data:
				self.list.Set([k for k in data["articles"].keys()])
				self.list.SetSelection(0)
		except FileNotFoundError:
			wx.MessageBox(_("You are not save articles yet, to save an article, click applications button in the results list, then choose Save."), _("error"), style=wx.ICON_ERROR)
			self.Destroy()
	def check(self):
		if get("hideclosebutton"):
			self.close.Hide()
		else:
			self.close.Show()

	def ArticleInformation(self):
		with shelve.open(FullPath) as data:
			name=self.list.GetStringSelection()
			date=data["atf"][name+"time"]
			CharsLen=len(data["articles"][name])
			WordsLen=len(data["articles"][name].split(" "))
			say(str(_("Saved article name: %s, added in: %s, Article length: %s characters, Article word count: about %s word.")%(name,date,CharsLen,WordsLen)))

	def SetupContextMenu(self):
		self.ContextMenu=wx.Menu()
		delete=self.ContextMenu.Append(-1, _("delete"))
		copy=self.ContextMenu.Append(-1, _("Copy the title and text of the article"))
		self.Bind(wx.EVT_MENU, self.OnDelete, delete)
		self.Bind(wx.EVT_MENU, self.OnCopy, copy)
		self.list.Bind(wx.EVT_CONTEXT_MENU, self.ShowContextMenu)

	def ShowContextMenu(self, event):
		if self.list.Selection==-1:
			say(_("No item selected"))
			return
		self.PopupMenu(self.ContextMenu)

	def OnDelete(self,event):
		alert=wx.MessageBox(_("Are you sure you want to delete %s?")%(self.list.GetStringSelection()), _("alert"), style=wx.YES_NO, parent=self)
		if alert==wx.YES:
			with shelve.open(FullPath) as data:
				id=self.list.GetSelection()
				d=data["articles"]
				dt=data["atf"]
				del d[self.list.GetStringSelection()]
				del dt[self.list.GetStringSelection()+"time"]
				self.list.Delete(id)
				data["articles"]=d
				data["atf"]=dt
				wx.MessageBox(_("The article was successfully deleted"), _("success"))
		if self.list.IsEmpty():
			Delete(DataPath)
			self.Destroy()

	def OnCopy(self,event):
		with shelve.open(FullPath) as data:
			title=self.list.GetStringSelection()
			article=data["articles"][title]
			copy(title+": "+article)
			wx.MessageBox(_("The article was successfully copied to the clipboard"), _("success"), parent=self)

	def OnHook(self,event):
		k=event.GetKeyCode()
		if k==wx.WXK_F1:
			self.ArticleInformation()
		elif k==wx.WXK_ESCAPE and get("escapetoback"):
			self.Destroy()
		if self.FindFocus()==self.list:
			if k== wx.WXK_NUMPAD_DELETE or k== wx.WXK_DELETE:
				self.OnDelete(None)
			elif event.controlDown and k==ord("C"):
				self.OnCopy(None)
		event.Skip()
