import wx
import shelve
from google_currency import convert, CODES
from threading import Thread
from settingsconfig import get,new
import os
from wx.adv import NotificationMessage
from .speak import say
from sys import getwindowsversion

DataPath=os.path.join(os.getenv("appdata"), "Easy Toolkit/data")
FullPath=os.path.join(os.getenv("appdata"), "Easy Toolkit/data/currency_rate")

class CurrencyConverter(wx.Dialog):
	def __init__(self, parent):
		wx.Dialog.__init__(self, parent, title=_("currency converter"))
		p=wx.Panel(self)
		wx.StaticText(p, -1, _("from:"))
		self.From=wx.ComboBox(p, -1, style=wx.CB_SORT)
		wx.StaticText(p, -1, _("to:"))
		self.to=wx.ComboBox(p, -1, style=wx.CB_SORT)
		wx.StaticText(p, -1, _("amount:"))
		self.amount=wx.TextCtrl(p, -1)
		wx.StaticText(p, -1, _("Conversion result"))
		self.result=wx.TextCtrl(p, -1, style=wx.TE_READONLY|wx.TE_MULTILINE|wx.HSCROLL)
		start_btn=wx.Button(p, -1, _("convert"))
		start_btn.Bind(wx.EVT_BUTTON, self.OnStart)
		start_btn.SetDefault()
		sf=wx.Button(p, -1, _("Set the selected currency to get its rate on startup"))
		sf.Bind(wx.EVT_BUTTON, self.SetAsRate)
		self.converting=False
		CurrencyList=list()
		for key,value in CODES.items():
			CurrencyList.append("{}:{}".format(key,value))
		try:
			self.From.Set(CurrencyList)
			self.to.Set(CurrencyList)
			self.From.SetStringSelection(get("cfrom"))
			self.to.SetStringSelection(get("cto"))
		except:
			pass
		self.Bind(wx.EVT_CHAR_HOOK, self.Shortcuts)

	def OnStart(self,event):
		if self.converting:
			return
		From=self.From.Value.split(":")
		to=self.to.Value.split(":")
		amount=self.amount.Value
		say(_("Converting from {} to {}").format(From[1], to[1]))
		try:
			if amount=="":
				amount=1.0
			amount=float(amount)
			if amount - int(amount) == 0.0:
				amount=int(amount)
		except ValueError:
			say(_("You can only enter numbers"))
			self.amount.SetFocus()
			return
		self.converting=True
		t = Thread(target=self.CurrencyConverter, args=[From, to, amount, True])
		t.demon=True
		t.start()

	def CurrencyConverter(self, From, to, amount, w):
		data=convert(From[0], to[0], amount)
		r_obj="{} {} = {} {}.".format(amount, From[1], data["amount"], to[1])
		if w:
			self.result.Value=r_obj
			wx.CallAfter(self.result.SetFocus)
			self.converting=False
			new("cfrom", self.From.Value) if not get("cfrom") ==self.From.Value else None
			new("cto", self.to.Value) if not get("cto") ==self.to.Value else None
		else:
			return r_obj

	def Shortcuts(self, event):
		k = event.GetKeyCode()
		if k == wx.WXK_F2:
			From=self.From.Value
			to=self.to.Value
			self.From.Value=to
			self.to.Value=From
			say(_("Converting from {t} to {f}").format(t=self.to.Value, f=self.From.Value))
		elif k == wx.WXK_ESCAPE and get("escapetoback"):
			self.Destroy()
		event.Skip()

	def SetAsRate(self, event):
		c=convert(self.From.Value.split(":")[0], self.to.Value.split(":")[0], 1)
		try:
			os.mkdir(DataPath)
		except FileExistsError:
			pass
		try:
			with shelve.open(FullPath) as data:
				try:
					data["from"] = self.From.Value
					data["to"] = self.to.Value
					data["count"] = c["amount"]
					say(_("successfully set {f} against {t}").format(f=self.From.Value, t=self.to.Value))
				except:
							say(_("An error occurred which caused the tool not to set the specified currency to get its rate"))
		except:
			say(_("An error occurred which caused the tool not to set the specified currency to get its rate"))


	def GetRates(self):
#		try:
		with shelve.open(FullPath) as data:
			f=data["from"]
			t=data["to"]
			c=float(data["count"])
			sf=f.split(":")
			st=t.split(":")
			cr=convert(sf[0], st[0], 1)
			if float(cr["amount"]) > c:
				message=_("The price of the currency {From} has gone up against its last price and is now 1 {From} = {count} {cName}").format(From=f, cName=st[0], count=cr["amount"])
			elif float(cr["amount"]) <c:
				message=_("The price of the currency {From} has gone down against its last price and is now 1 {From} = {count} {cName}").format(From=f, cName=st[0], count=cr["amount"])
			else:
				return
		with shelve.open(FullPath) as data:
			data["count"] = cr["amount"]
			NotificationMessage(_("currency rate"), message).Show(10)