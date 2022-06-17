import wx
from .speak import say

class GetTextFromUser(wx.Dialog):
	def __init__(self, parent, title, message):
		wx.Dialog.__init__(self, parent, id=-1, title=title)
		p=wx.Panel(self)
		wx.StaticText(p, -1, message)
		self.txt=wx.TextCtrl(p, -1)
		self.canceled=False
		self.ok=wx.Button(p, wx.ID_OK)
		self.cancel=wx.Button(p, -1, _("&cancel"))
		self.ok.SetLabel(_("&Ok"))
		self.cancel.Bind(wx.EVT_BUTTON, self.OnCancel)
		self.Bind(wx.EVT_CHAR_HOOK, self.OnEscape)
		self.ok.SetDefault()
		self.ShowModal()

	def OnCancel(self, event):
		say(_("canceled"))
		self.canceled=True
		self.Destroy()

	def OnEscape(self,event):
		k=event.GetKeyCode()
		if k==wx.WXK_ESCAPE:
			self.OnCancel(None)
		event.Skip()