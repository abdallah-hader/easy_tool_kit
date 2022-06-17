import wx
import requests
import sys
import urllib
from webbrowser import open as o
from settingsconfig import get
from threading import Thread
from . import GetTextFromUser

class ShortUrl(wx.Dialog):
	def __init__(self, parent):
		wx.Dialog.__init__(self, parent, id=-1, title=_("url shortener"))
		p=wx.Panel(self)
		if get("escapetoback"):
			self.Bind(wx.EVT_CHAR_HOOK, self.OnHook)
		wx.StaticText(p, -1, _("the shortened url"))
		self.f=wx.TextCtrl(p, -1, style=wx.HSCROLL)
		self.url=GetTextFromUser.GetTextFromUser(p, _("url"),_("Enter the url you want to shorten"))
		if self.url.canceled:
			return
		if len(self.url.txt.Value)<=4 or self.url.txt.Value=="":
			wx.MessageBox(_("Please enter a valid url"),_("error"), style=wx.ICON_ERROR)
			return
		thread=Thread(target=self.short, args=[self.url.txt.Value])
		thread.demon=True
		thread.start()
		self.open=wx.Button(p, -1, _("&open in browser"))
		if not get("hideclosebutton"):
			self.close=wx.Button(self, -1, _("&close"))
			self.close.Bind(wx.EVT_BUTTON, lambda event: self.Destroy())
		self.open.Bind(wx.EVT_BUTTON, lambda event: o(self.f.GetValue()))
		self.Bind(wx.EVT_CLOSE, self.OnClose)
		self.Show()


	def short(self,url_long):
		link = "http://tinyurl.com/api-create.php"
		try:
			url = link + "?" \
			+ urllib.parse.urlencode({"url": url_long})
			res = requests.get(url)
			wx.CallAfter(self.f.SetValue, res.text)
		except:
			wx.MessageBox(_("Error: The link cannot be shortened"), _("error"), style=wx.ICON_ERROR)
			wx.CallAfter(self.Destroy)

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
