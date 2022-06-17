import wx
from settingsconfig import get, new
import os
import sys
from language import supported_languages
from . import speak

say=speak.say
languages = {index:language for language, index in enumerate(supported_languages.values())}


class settings_dialog(wx.Dialog):
	def __init__(self, parent):
		wx.Dialog.__init__(self, parent, id=-1, title=_("settings"))
		p=wx.Panel(self)
		self.CenterOnParent()
		if get("escapetoback"):
			self.Bind(wx.EVT_CHAR_HOOK, self.OnHook)
		wx.StaticText(p, -1, _("List of sections, choose what you want to modify its settings from the list below"))
		tab1=wx.Listbook(p, -1)
		self.program=ProgramSettings(tab1)
		tab1.AddPage(self.program, _("general settings"))
		self.randomdraw=RandomDrawSettings(tab1)
		tab1.AddPage(self.randomdraw, _("random draw settings"))
		self.Wikipedia=WikipediaSettings(tab1)
		tab1.AddPage(self.Wikipedia, _("wikipedia settings"))
		self.weather=WeatherSettings(tab1)
		tab1.AddPage(self.weather, _("weather settings"))
		self.currency=CurrencySettings(tab1)
		tab1.AddPage(self.currency, _("currency converter settings"))
		self.NvdaAddons=AddonsSettings(tab1)
		tab1.AddPage(self.NvdaAddons, _("download nvda addons tool settings"))
		self.ok=wx.Button(p, -1, _("&save settings"))
		self.cancel=wx.Button(p, -1, _("&cancel"))
		self.cancel.Bind(wx.EVT_BUTTON, lambda event: self.Destroy())
		self.ok.Bind(wx.EVT_BUTTON, self.OnOk)
		self.ok.SetDefault()

	def OnOk(self,event):
		lang=self.program.lang.GetStringSelection()
		if not get("confirmation_to_exit") == self.program.AskToExit.GetValue():
			new("confirmation_to_exit", self.program.AskToExit.GetValue())
		if not get("deltheitemdrawed") == self.randomdraw.DelItemDrawed.GetValue():
			new("deltheitemdrawed", self.randomdraw.DelItemDrawed.GetValue())
		if not get("hideclosebutton") == self.program.CloseButton.GetValue():
			new("hideclosebutton", self.program.CloseButton.GetValue())
		if not get("escapetoback") == self.program.Escape.GetValue():
			new("escapetoback", self.program.Escape.GetValue())
		if not get("checkforupdatesatstartup") == self.program.CFU.GetValue():
			new("checkforupdatesatstartup", self.program.CFU.GetValue())
		if not get("getcurrencyupdates") == self.currency.Get.GetValue():
			new("getcurrencyupdates", self.currency.Get.GetValue())

		if not get("city") == self.weather.city.GetValue():
			new("city", self.weather.city.GetValue())
		if not get("DownloadAddonsPath") == self.NvdaAddons.path.GetValue():
			new("DownloadAddonsPath", self.NvdaAddons.path.GetValue())
			say(_("you changed the downloading nvda addons path, you shuld restart the program to apply to new path"))

		lang = {value:key for key, value in languages.items()}
		if not lang[self.Wikipedia.lang.Selection] == get("wikipedialang"):
			new("wikipedialang", lang[self.Wikipedia.lang.Selection])
		if not lang[self.program.lang.Selection] == get("language"):
			new("language", lang[self.program.lang.Selection])
			msg = wx.MessageBox(_("You changed the program language to  %s, which means you have to restart the program, do you want to restart the program now؟")%(self.program.lang.GetStringSelection()), _("alert"), style=wx.YES_NO, parent=self)
			os.execl(sys.executable, sys.executable, *sys.argv) if msg == wx.YES else None
		self.Destroy()

	def OnHook(self,event):
		k=event.GetKeyCode()
		if k==wx.WXK_ESCAPE:
			self.Destroy()
		event.Skip()

class ProgramSettings(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)
		wx.StaticText(self, -1, _("Program language"))
		self.lang=wx.Choice(self, -1)
		self.lang.Set(list(supported_languages.keys()))
		try:
			self.lang.Selection = languages[get("language")]
		except KeyError:
			self.lang.Selection = 0
		self.AskToExit=wx.CheckBox(self, -1, _("Confirmation before exit"))
		self.AskToExit.SetValue(get("confirmation_to_exit"))
		self.Escape=wx.CheckBox(self, -1, _("Use the escape key to close windows"))
		self.Escape.SetValue(get("escapetoback"))
		self.CloseButton=wx.CheckBox(self, -1, _("Hide the close buttons from the windows. make sure you activate the escape key to close the windows so that no errors occur."))
		self.CloseButton.SetValue(get("hideclosebutton"))
		self.CFU=wx.CheckBox(self, -1, _("Check for updates at startup"))
		self.CFU.SetValue(get("checkforupdatesatstartup"))

class RandomDrawSettings(wx.Panel):
	def __init__(self,parent):
		wx.Panel.__init__(self, parent)
		self.DelItemDrawed=wx.CheckBox(self, -1, _("Delete the dragged item when the random draw button is pressed"))
		self.DelItemDrawed.SetValue(get("deltheitemdrawed"))

class WikipediaSettings(wx.Panel):
	def __init__(self,parent):
		wx.Panel.__init__(self, parent)
		wx.StaticText(self, -1, _("Language: When you select a Wikipedia language, results and pages will appear in the selected language"))
		self.lang=wx.Choice(self, -1)
		self.lang.Set(list(supported_languages.keys()))
		try:
			self.lang.Selection = languages[get("wikipedialang")]
		except KeyError:
			self.lang.Selection = 0

class WeatherSettings(wx.Panel):
	def __init__(self,parent):
		wx.Panel.__init__(self,parent)
		wx.StaticText(self, -1, _("City. Type the name of the city you want to get the weather for"))
		self.city=wx.TextCtrl(self, -1)
		self.city.SetValue(get("city"))

class CurrencySettings(wx.Panel):
	def __init__(self,parent):
		wx.Panel.__init__(self,parent)
		self.Get=wx.CheckBox(self, -1, _("Get the currency rate at startup"))
		self.Get.Value=get("getcurrencyupdates")

class AddonsSettings(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)
		wx.StaticText(self, -1, _("addons save path"))
		self.path=wx.TextCtrl(self, -1, style=wx.TE_READONLY|wx.TE_MULTILINE)
		self.path.Value=get("DownloadAddonsPath")
		self.browse=wx.Button(self, -1, _("browse"))
		self.browse.Bind(wx.EVT_BUTTON, self.SelectDirectory)

	def SelectDirectory(self, event):
		dialog=wx.DirDialog(self, _("Choose a path to save the addons after downloading them."), get("DownloadAddonsPath"))
		if dialog.ShowModal() == wx.ID_OK:
			self.path.Value=dialog.GetPath()