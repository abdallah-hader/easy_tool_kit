import wx
import win32con
import sys
from threading import Thread
import webbrowser as we
from OpenDocFile import help
from settingsconfig import init_config,get
from language import init_translation
from includes import app_info
from includes import translator
from includes import lottery as lt
from includes import settings_dialog
from includes import wiki
from includes import short_url
from includes import weather
from includes import speak
from includes import updater
from includes import currency_converter
from includes import password_generator
from includes import nvda_addons
from accessible_output2 import outputs

init_config()
init_translation("Easy_Toolkit")
say=speak.say

class MainScreen(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, parent=None, id=-1, title=app_info.name+_(" version %s")%(app_info.version))
		self.Gshortcut()
		p=wx.Panel(self)
		self.Center()
		self.SetSize(wx.DisplaySize())
		self.Maximize(True)
		self.Bind(wx.EVT_HOTKEY, self.onkey, id=self.showHideId)
		self.hint=wx.StaticText(p, -1, _("Press the alt key to access the options"))
		self.hint.SetFocus()
#create the menu bar
		menubar=wx.MenuBar()
#create the menus
		file=wx.Menu()
		options=wx.Menu()
		about=wx.Menu()
		contact=wx.Menu()
#add the menus to the menubar
		menubar.Append(file, _("Main Menu"))
		menubar.Append(options, _("tools"))
		menubar.Append(about, _("about"))
		about.AppendSubMenu(contact, _("Contact us"))
#add the options to the menus
		hide=file.Append(-1, _("hide the program"))
		settings=file.Append(-1, _("program settings\tctrl+shift+s"))
		CheckUpdates=file.Append(-1, _("Check for updates"))
		close=file.Append(-1, _("exit\tctrl+w"))
		translator=options.Append(-1, _("Translator\tctrl+t"))
		wikipedia=options.Append(-1, _("Search in Wikipedia\tctrl+shift+w"))
		currency=options.Append(-1, _("currency converter\tctrl+shift+v"))
		Weather=options.Append(-1, _("weather condition\tctrl+shift+o"))
		short=options.Append(-1, _("url shortener\tctrl+shift+u"))
		rpw=options.Append(-1, _("random password generator\tctrl+shift+p"))
		nvdaaddons=options.Append(-1, _("download nvda addons tool\tctrl+shift+n"))
		lottery=options.Append(-1, _("random draw\tctrl+r"))
		AboutInfo=about.Append(-1, _("about the program"))
		UserGuyd=about.Append(-1, _("User guide\tf1"))
		telegram=contact.Append(-1, _("telegram"))
		facebook=contact.Append(-1, _("facebook"))
		twitter=contact.Append(-1, _("twitter"))

		email=contact.Append(-1, _("gmail"))
#bind the options
		self.Bind(wx.EVT_MENU, self.onkey, hide)
		self.Bind(wx.EVT_MENU, self.OnClose, close)
		self.Bind(wx.EVT_MENU, self.CheckForUpdates, CheckUpdates)
		self.Bind(wx.EVT_MENU, self.ShowTranslator, translator)
		self.Bind(wx.EVT_MENU, self.ShowLottery, lottery)
		self.Bind(wx.EVT_MENU, self.ShowSettings, settings)
		self.Bind(wx.EVT_MENU, self.ShowWikiPedia, wikipedia)
		self.Bind(wx.EVT_MENU, self.ShowUrlShort, short)
		self.Bind(wx.EVT_MENU, self.ShowWeather, Weather)
		self.Bind(wx.EVT_MENU, self.ShowRpw, rpw)
		self.Bind(wx.EVT_MENU, lambda event: wx.MessageBox(_("Easy_Toolkit version %s, author: _(%s), description: A program designed for screen reader users that contains various tools that are added from time to time")%(app_info.version, app_info.author), _("about")), AboutInfo)
		self.Bind(wx.EVT_MENU, self.ShowCurrency, currency)
		self.Bind(wx.EVT_MENU, self.NvdaAddons, nvdaaddons)
		self.Bind(wx.EVT_MENU, lambda event: help(), UserGuyd)

		self.Bind(wx.EVT_MENU, lambda e: we.open("https://t.me/abdallah_alanbry"), telegram)
		self.Bind(wx.EVT_MENU, lambda e: we.open("https://www.facebook.com/profile.php?id=100009657259379"), facebook)
		self.Bind(wx.EVT_MENU, lambda e: we.open("https://twitter.com/ABDALLAHHAYDER5"), twitter)
		self.Bind(wx.EVT_MENU, lambda e: we.open("mailto:abd23200@gmail.com"), email)
		self.SetMenuBar(menubar)
		self.Bind(wx.EVT_CLOSE, self.OnClose)
		if get("checkforupdatesatstartup"):
			Thread(target=updater.cfu, args=[True]).start()
		if get("getcurrencyupdates"):
			c=currency_converter.CurrencyConverter(self)
			t=Thread(target=c.GetRates)
			t.start()
		self.Show()

	def ShowTranslator(self,event):
		tr=translator.translator(self)
		tr.Show()

	def ShowLottery(self, event):
		l=lt.Lottery(self)
		l.ShowModal()

	def ShowWikiPedia(self, event):
		wp=wiki.WikiPediaSearch(self)
		wp.Show()

	def ShowSettings(self, event):
		ss=settings_dialog.settings_dialog(self)
		ss.Show()

	def ShowUrlShort(self,event):
		r=short_url.ShortUrl(self)

	def ShowWeather(self,event):
		Weather=weather.Weather(self)

	def ShowCurrency(self,event):
		c=currency_converter.CurrencyConverter(self)
		c.ShowModal()

	def ShowRpw(self, event):
		pw=password_generator.PasswordGenerator(self)
		pw.ShowModal()

	def NvdaAddons(self, event):
		window=nvda_addons.GetNvdaAddons(self)
		window.ShowModal()

	def Gshortcut(self,):
		self.showHideId = -1
		self.RegisterHotKey(self.showHideId, win32con.MOD_CONTROL+win32con.MOD_SHIFT, ord("H"))

	def onkey(self,event):
		self.Show(not self.Shown)
		if self.Shown:
			say(_("The program has been shown"))
			self.hint.SetFocus()
		else:
			say(_("The program is hidden"))

	def CheckForUpdates(self, event):
		say(_("checking for updates, please wait"))
		updater.cfu()

	def OnClose(self,event):
		if not get("confirmation_to_exit"):
			wx.Exit()
		else:
			ask=wx.MessageBox(_("Do you want to close the program?"), _("alert"), style=wx.YES_NO)
			if ask==wx.YES:
				wx.Exit()

app=wx.App()
MainScreen()
app.MainLoop()