import wx
import weathercom
import json
from . import speak
from . import GetTextFromUser
from settingsconfig import get,new
from threading import Thread

say=speak.say

class Weather(wx.Dialog):
	def __init__(self, parent):
		wx.Dialog.__init__(self, parent, id=-1, title=_("weather condition"))
		if get("escapetoback"):
			self.Bind(wx.EVT_CHAR_HOOK, self.OnHook)
		p=wx.Panel(self)
		wx.StaticText(p, -1, _("weather condition"))
		self.Field=wx.TextCtrl(p, -1, style=wx.TE_MULTILINE|wx.TE_READONLY|wx.HSCROLL)
		self.Field.SetValue(_("getting data, please wait..."))
		if not get("hideclosebutton"):
			self.close=wx.Button(p, -1, _("&close"))
			self.close.Bind(wx.EVT_BUTTON, lambda event: self.Destroy())
		self.adding=False
		if get("city")=="None" or get("city")=="":
			self.adding=True
			city=GetTextFromUser.GetTextFromUser(p, _("city name"), _("Enter city name to get weather condition. note you can change this later via settings/weather settings."))
			if city.canceled and self.adding==True:
				self.adding=False
				self.Destroy()
				return
		if self.adding==True:
			new("city", city.txt.Value)
		thread=Thread(target=self.GetWeather)
		thread.demon=True
		thread.start()
		self.Show()

	def GetWeather(self):
		say(_("getting data, please wait..."))
		try:
			data=json.loads(weathercom.getCityWeatherDetails(get("city")))
		except KeyError:
			wx.MessageBox(_("Sorry we can\'t get the weather in %s city. Type your city name correctly, then try again")%(get("city")),_("error"), style=wx.ICON_ERROR)
			return
		except:
			wx.MessageBox(_("No internet connection, connect to the internet and try again"), _("error"), style=wx.ICON_ERROR)
			self.Destroy()
			return
		r=_("weather condition in: ")+str(data.get("city"))+_("\ntemperature: ")+str(data["vt1observation"].get("temperature"))+_("\ntemperature Max Since7am: ")+str(data["vt1observation"].get("temperatureMaxSince7am"))+_("\nhumidity: ")+str(data["vt1observation"].get("humidity"))+_("\nWind speed: ")+str(data["vt1observation"].get("windSpeed"))+_("KM/H")+_("\nwind Dir Compass: ")+str(data["vt1observation"].get("windDirCompass"))+_("\nWind dir degrees: ")+str(data["vt1observation"].get("windDirDegrees"))
		wx.CallAfter(self.Field.SetValue, r)
		say(_("loading complete"))

	def OnHook(self,event):
		k=event.GetKeyCode()
		if k==wx.WXK_ESCAPE:
			self.Destroy()
		event.Skip()
