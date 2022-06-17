import wx
from random import choice, shuffle
from settingsconfig import get

all_characters="abcdefghijkmnopqrstuvwxyz/ABCDEFGHIJKMNOPQRSTUVWXYZ"
all_numbers="1234567890"
all_symbols="!@#$%^&*/"

class PasswordGenerator(wx.Dialog):
	def __init__(self, parent):
		wx.Dialog.__init__(self, parent, id=-1, title=_("Random Password Generator"))
		self.Center()
		p=wx.Panel(self)
		self.h=wx.StaticText(p, -1, _("the generated password:"))
		self.result=wx.TextCtrl(p, -1, style=wx.TE_READONLY|wx.TE_MULTILINE|wx.HSCROLL)
		wx.StaticText(p, -1, _("The length of the password to be generated"))
		self.Length=wx.SpinCtrl(p, -1, min=4, max=170)
		self.Numbers=wx.CheckBox(p, -1, _("include numbers"))
		self.Symbols=wx.CheckBox(p, -1, _("includes symbols"))
		self.Upper=wx.CheckBox(p, -1, _("Include capital letters"))
		generate=wx.Button(p, -1, _("Generate new password"))
		generate.Bind(wx.EVT_BUTTON, self.OnGenerate)
		self.h.Hide(), self.result.Hide()
		if not get("hideclosebutton"):
			self.close=wx.Button(p, -1, _("&close"))
			self.close.Bind(wx.EVT_BUTTON, lambda event: self.Destroy())
		if get("escapetoback"):
			self.Bind(wx.EVT_CHAR_HOOK, self.OnHook)


	def OnGenerate(self, event):
		try:
			self.h.Show(), self.result.Show()
		except:
			pass
		self.result.Value=self.GeneratePass(Upper=self.Upper.GetValue(), numbers=self.Numbers.GetValue(), symbols=self.Symbols.GetValue(), length=self.Length.GetValue())
		self.result.SetFocus()

	def GeneratePass(self, numbers=True, Upper=True, symbols=True, length=4):
		u=all_characters.split("/")
		all=u[0]
		if Upper:
			all=all + u[1]
		if numbers:
			all=all + all_numbers
		if symbols:
			all=all + all_symbols
		password=[]
		for i in range(0, length):
			password.append(choice(all))
		shuffle(password)
		return "".join(password)

	def OnHook(self,event):
		k=event.GetKeyCode()
		if k==wx.WXK_ESCAPE:
			self.Destroy()
		event.Skip()
