import random as rnd
from accessible_output2 import outputs
import wx
from settingsconfig import get
from . import speak
from . import GetTextFromUser

say=speak.say

class Lottery(wx.Dialog):
	def __init__(self,parent):
		wx.Dialog.__init__(self, parent, id=-1, title=_("Random Draw"))
		p=wx.Panel(self)
		self.CenterOnParent()
		if get("escapetoback"):
			self.Bind(wx.EVT_CHAR_HOOK, self.OnHook)
		else:
			pass
		self.ItemsList=wx.StaticText(p, -1, _("items list"))
		self.List=wx.ListBox(p, -1)
		self.List.Bind(wx.EVT_CONTEXT_MENU, self.OnContext)
		self.Add=wx.Button(p, -1, _("add &new"))
		self.Add.Bind(wx.EVT_BUTTON, self.OnAdd)
		self.choice =wx.Button(p, -1, _("&draw"))
		self.choice.Bind(wx.EVT_BUTTON, self.OnChoice)
		self.clear=wx.Button(p, -1, _("C&lear all items"))
		self.clear.Bind(wx.EVT_BUTTON, self.OnClear)
		if not get("hideclosebutton"):
			self.close=wx.Button(p, -1, _("&close"))
			self.close.Bind(wx.EVT_BUTTON, lambda event: self.Destroy())
		self.Bind(wx.EVT_CLOSE, self.OnClose)

	def OnAdd(self, event):
		item=GetTextFromUser.GetTextFromUser(self, _("item name"), _("Enter the name of the item to be added to the draw list"))
		if item.txt.Value.lower() in self.List.GetStrings(): 
			wx.MessageBox(_("This item is already in the items list"), _("error"), style=wx.ICON_ERROR)
		elif item.txt.Value!='':
			self.List.Append(item.txt.Value.lower())
			self.List.SetStringSelection(item.txt.Value)
			self.SetCaption()

	def OnChoice(self,event):
		if self.List.GetCount()<2:
			wx.MessageBox(_("You can't make a draw until you add at least two items"), _("error"), style=wx.ICON_ERROR, parent=self)
		else:
			rnd.shuffle(self.List.GetStrings())
			ri=rnd.choice(self.List.GetStrings())
			wx.MessageBox(_("The item has been randomly selected: %s ")%(ri), _("result"))
			if get("deltheitemdrawed"):
				self.List.Delete(self.List.FindString(ri))
				self.SetCaption()

	def OnContext(self,event):
		if self.List.GetSelection()==-1:
			say(_("No item selected"))
			return
		else:
			contextmenu=wx.Menu()
			edit=contextmenu.Append(-1, _("edit"))
			delete=contextmenu.Append(-1, _("delete"))
			self.Bind(wx.EVT_MENU, self.OnEdit, edit)
			self.Bind(wx.EVT_MENU, self.OnDelete, delete)
			self.PopupMenu(contextmenu)

	def OnEdit(self, event):
		itemname=self.List.GetStringSelection()
		ItemIndex=self.List.GetSelection()
		new=GetTextFromUser.GetTextFromUser(self, _("new value"), _("Enter the new value for the item %s ")%(itemname))
		if new.txt.Value.lower()==itemname.lower():
			wx.MessageBox(_("You cannot modify the value to the current value, please give a different value to change."), _("error"), style=wx.ICON_ERROR)
		elif new.txt.Value!="":
			self.List.Delete(ItemIndex)
			self.List.Insert(new.txt.Value.lower(), ItemIndex)
			self.List.SetStringSelection(new.txt.Value)

	def OnDelete(self,event):
		id=self.List.GetSelection()
		msg=wx.MessageBox(_("Are you sure you want to delete %s?")%(self.List.GetString(id)), _("alert"), style=wx.YES_NO, parent=self)
		if msg==wx.YES:
			self.List.Delete(id)
			self.List.SetSelection(0)
			self.SetCaption()
			say(_("Item Deleted"))
		else:
			pass
		try:
			self.List.SetSelection(0)
		except:
			pass

	def OnClear(self,event):
		if self.List.IsEmpty():
			wx.MessageBox(_("The list does not contain items to delete"), _("error"), style=wx.ICON_ERROR)
		else:
			msg=wx.MessageBox(_("There are %d items in the list, Do you want to delete them?")%(self.List.GetCount()), _("alert"), style=wx.YES_NO, parent=self)
			if msg==wx.YES:
				self.List.Clear()
				wx.MessageBox(_("all items deleted"),_("success"), parent=self)
				self.SetCaption()

	def SetCaption(self):
		if self.List.GetCount()==1:
			self.ItemsList.SetLabel(_("items list, contains %d item")%(self.List.GetCount()))
		elif self.List.GetCount()==2:
			self.ItemsList.SetLabel(_("items list, contains 2 items"))
		elif self.List.IsEmpty():
			self.ItemsList.SetLabel(_("items list"))
		else:
			self.ItemsList.SetLabel(_("items list, contains %d items")%(self.List.GetCount()))

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
