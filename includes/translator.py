import wx
import os
from settingsconfig import new, get
from threading import Thread
import pyperclip as clip
from . import app_info
from . import speak

try:
	from deep_translator import GoogleTranslator as gt
except:
	pass


say=speak.say

class translator(wx.Frame):
	def __init__(self, parent):
		super().__init__(parent, -1, title=_("google translator"), name=app_info.name)
		p=wx.Panel(self)
		if get("escapetoback"):
			self.Bind(wx.EVT_CHAR_HOOK, self.OnHook)
		self.CentreOnParent()
		try:
			self.supported_languages = gt.get_supported_languages()
		except:
			self.supported_languages=[]
			wx.MessageBox(_("Sorry, there is an error in your network connection, for this reason, we will not be able to connect, check your Internet connection, and then try again."),_("connection error"), style=wx.ICON_ERROR)
			self.Destroy()
		wx.StaticText(p, -1, _("The text to be translated"))
		self.Text=wx.TextCtrl(p, -1, style=wx.TE_MULTILINE|wx.HSCROLL)
		wx.StaticText(p,-1,_("Choose the source language"))
		self.source=wx.Choice(p, -1, choices=self.supported_languages)
		try:
			self.source.SetStringSelection(get("translatorsource"))
		except:
			pass
		wx.StaticText(p,-1,_("Choose the target language"))
		self.target=wx.Choice(p, -1, choices=self.supported_languages)
		try:
			self.target.SetStringSelection(get("translatortarget"))
		except:
			pass
		self.Translate=wx.Button(p, -1, _("&Translate"))
		self.Translate.Bind(wx.EVT_BUTTON, self.Start)
		if not get("hideclosebutton"):
			self.close=wx.Button(p, -1, _("&close"))
			self.close.Bind(wx.EVT_BUTTON, lambda event: self.Destroy())
		self.Bind(wx.EVT_CLOSE, self.OnClose)
		for i in p.GetChildren():
			i.Bind(wx.EVT_KEY_DOWN, self.shortcuts)

	def Start(self,event):
		thread=Thread(target=self.start_translate)
		thread.demon=True
		thread.start()

	def start_translate(self):
		wx.CallAfter(self.Translate.Disable)
		say(_("translating"))
		t=self.target.GetStringSelection()
		s=self.source.GetStringSelection()
		if not get("translatorsource")==s:
			new("translatorsource", s)
		if not get("translatortarget")==t:
			new("translatortarget", t)

		try:
			tran=gt(source=self.source.GetStringSelection(),target=self.target.GetStringSelection()).translate(self.Text.GetValue())
			wx.CallAfter(Resulte, self,tran)
			say(_("Translation completed"))
			wx.CallAfter(self.Translate.Enable)
		except:
			wx.MessageBox(_("Can\'t translate, make sure text is put in text field, source language and target language are selected correctly, then try again."), _("translate error"))
			wx.CallAfter(self.Translate.Enable)

	def shortcuts(self,event):
		k=event.GetKeyCode()
		t=self.target.GetStringSelection()
		s=self.source.GetStringSelection()
		if k==wx.WXK_F2:
			try:
				self.source.SetStringSelection(t)
				self.target.SetStringSelection(s)
			except:
				pass
			say(_("translating from: %s to %s.")%(self.source.GetStringSelection(), self.target.GetStringSelection()))
		event.Skip()

	def OnHook(self,event):
		k=event.GetKeyCode()
		if k==wx.WXK_ESCAPE:
			self.Destroy()
		event.Skip()

	def OnClose(self,event):
		if not get("confirmation_to_exit"):
			wx.Exit()
		else:
			ask=wx.MessageBox(_("Do you want to close the program?"), _("confirmation"), style=wx.YES_NO)
			if ask==wx.YES:
				wx.Exit()


class Resulte(wx.Dialog):
	def __init__(self,parent,text):
		wx.Dialog.__init__(self, parent, -1, title=_("result of translated text"), size = (250,150))
		p=wx.Panel(self)
		if get("escapetoback"):
			self.Bind(wx.EVT_CHAR_HOOK, self.OnHook)
		self.CenterOnParent()
		self.r=wx.StaticText(p,-1,_("result"))
		self.text_resulte=wx.TextCtrl(p, -1, value=text, style=wx.TE_MULTILINE|wx.HSCROLL|wx.TE_READONLY)
		self.SaveToFile=wx.Button(p, -1, _("&Save the translation result in a text file"))
		self.SaveToFile.Bind(wx.EVT_BUTTON, self.save)
		self.copy=wx.Button(p, -1, _("Copy translation result to cli&pboard"))
		self.copy.Bind(wx.EVT_BUTTON, self.OnCopy)
		self.FileText=wx.StaticText(p, -1, _("file name"))
		self.FileName=wx.TextCtrl(p, -1, style=wx.HSCROLL)
		self.textpath=wx.StaticText(p, -1, _("file path"))
		self.path=wx.TextCtrl(p, -1, style=wx.HSCROLL)
		self.select=wx.Button(p, -1, _("select &folder"))
		self.select.Bind(wx.EVT_BUTTON, self.selectfolder)
		self.save_file=wx.Button(p, -1, _("sa&ve"))
		self.save_file.Bind(wx.EVT_BUTTON, self.file)
		self.save_file.Hide()
		self.select.Hide()
		self.path.Hide()
		self.textpath.Hide()
		self.FileName.Hide()
		self.FileText.Hide()
		if not get("hideclosebutton"):
			self.ok=wx.Button(p, wx.ID_OK, _("&Close"))
		self.Show()

	def save(self,event):
		self.SaveToFile.Hide(), self.text_resulte.Hide(), self.r.Hide(), self.copy.Hide()
		self.path.Show(), self.textpath.Show(), self.select.Show(), self.FileName.Show(), self.FileText.Show(), self.save_file.Show()
		self.FileName.SetFocus()
		self.path.SetValue(os.path.join(os.getenv("userprofile"), "Documents"))

	def selectfolder(self,event):
		directory = os.getcwd()
		dlg = wx.DirDialog(self, _("Choose the path to save the file"), directory)
		if dlg.ShowModal() == wx.ID_OK:
			directory = dlg.GetPath()
			self.path.SetValue(directory)

	def file(self,event):
		message=""
		if self.path.Value=='':
			message=_("select the path to save the file")
			say(message)
		elif self.FileName.Value=='':
			message=_("write the file name to save the file")
			say(message)
		elif self.path.Value!='' and self.FileName!='':
			fp=self.path.Value+'/'+self.FileName.Value+'.txt'
			file=open(fp,'w+')
			file.write(self.text_resulte.GetValue())
			file.close()

	def OnCopy(self,event):
		try:
			clip.copy(self.text_resulte.GetValue())
			wx.MessageBox(_("The translation result is copied to the clipboard"), _("success"))
		except:
			wx.MessageBox(_("There is an error that the translation result is not copied, if this error continues to appear, contact the program developers to solve the problem"), _("error"), style=wx.ICON_ERROR)

	def OnHook(self,event):
		k=event.GetKeyCode()
		if k==wx.WXK_ESCAPE:
			self.Destroy()
		event.Skip()
