import json
from settingsconfig import get


def GetOriginalLink(Link):
	lng=get("language")
	return Link.replace("\"lng\"", lng)

def AddLinks():
	for i in dict.keys():
		try:
			dict[i].append(dict2[i])
			print(f"added {dict2[i]} to {i}")
		except:
			pass


# here the first dictionery which containse addon name, and list for addon info, like what version of nvda needed, addon description, link for download.
dict={
	"Sound Splitter":["2019.3+", "This add-on, partly based on Tony's Enhancements by Tony Malykh, adds the ability to split audio from NVDA and other sounds onto separate audio channels.\nCommands:\n• Alt+NvDA+S: toggle sound splitter. If enabled, NVDA will be heard through the right channel.\nSound Splitter settings\nYou can configure add-on settings from NVDA menu/Preferences/Settings/Sound Splitter category.\n• Split NVDA sound and applications' sounds into left and right channels: checkinb this checkbox will enable sound splitting feature.\n• Switch left and right during sound split: by default, NVDA will be heard through the right channel if sound splitting is on. You can instead hear NVDA through the left channel by checking this checkbox.\nVersion 22.02\n• Initial version based on Tony Malykh's Tony's Enhancements add-on.", "https://addons.nvda-project.org/files/get.php?file=soundsplitter"],
	"Quick Notetaker":["2019.3 / 2021.2", """The Quick Notetaker add-on is a wonderful tool which allows writing notes quickly and easily anytime and from any app the user is using. Whether the user is watching a video for example, or participating in a meeting on Zoom, teams or Google meet, they can easily and smoothly open the notetaker and take a note. In order to create a quick note, NVDA + Alt + n key combination can be used, a floating window appears at the top left corner of the screen, so the note can be typed there.
Every note that is being Created can optionally get the active window title, and as such, the note content can get the context in which this note was created by having the note title as the active window title the user was using. This behavior can be changed from the add-on settings, where the user can decide whether the active window title is captured when creating a new note.
The Notetaker dialog
• 
The note edit area: When opening the Notetaker interface the focus will be in this edit area. Writing with Markdown (a markup language to easily produce HTML content) is supported also. For more info on Markdown visit the Markdown guide page.
• 
Preview note: to view the note in an HTML window.
• 
Copy: to copy the note as is to the clipboard.
• 
Copy HTML code: to copy the HTML code representing the note. A useful feature for those who write in Markdown.
• 
A checkbox to allow saving the note as Microsoft Word also, or updating the corresponding one if it exists.
• 
A save and close button.
• 
A discard button to discard changes when desired. When unsaved changes exist, a warning message is displayed to the user asking if they are sure they want to exit and discard their changes.
The Notes Manager interface
Opening and closing this interface
• 
NVDA + Alt + v will launch the Notes Manager interface.
• 
Using either the Escape key or the close button found at the bottom of this window will close this interface.
The notes list
The notes are organized in a tabular list which includes:
. 1
The note title: If the note hasn’t got the active window title, the first line of the note will be the note title displayed in this list.
. 2
Last edited time stamp.
. 3
A preview text of the note content.
The options available in Notes Manager interface
• 
View note: to view the note in an HTML window.
• 
Edit note: opens the note to be edited using Notetaker interface.
• 
Copy note: copies the note content as is to the clipboard.
• 
Create a Microsoft Word document: Creates a Microsoft Word document representing this note in case it has no such document.
• 
Open in Microsoft Word: opens the Microsoft Word document attached to this note in case it has a one.
• 
Copy HTML code: copies the HTML code representing this note. A useful feature for those who write in Markdown.
• 
Delete note: displays a warning before performing the note deletion.
• 
New note: the Notetaker interface can be reached from this interface to create a new note.
• 
Open settings: opening the add-on settings is also possible from here.
• 
Close: to close the window.
The add-on settings
The add-on settings are a part of NVDA’s settings interface. To reach those settings, the user needs to open the NVDA menu using NVDA key + n, choose preferences > settings, and then arrow down until reaching Quick Notetaker category.
Using the settings interface the user can:
• 
Default documents directory: to choose the default directory where Quick Notetaker documents will be saved. The user can press the “Browse” button to change the path of this directory.
• 
Ask me each time where to save the note's corresponding Microsoft Word document: a checkbox (not checked by default) – to show the dialog for choosing the location where the document will be saved on each save or update operation for the note’s Microsoft Word document if such a one exists.
• 
Open the note's corresponding Microsoft Word document after saving or updating: a checkbox (not checked by default) – to allow the user to choose whether the Microsoft Word document will be opened after a save or update operation in case the note has such document.
• 
Capture the active window title when creating a new note: a checkbox (checked by default) – to allow the note to get the active window title the user was using when they created the note. This title will be also the title of the Microsoft Word document for the note in case it has a one.
• 
Remember the note taker window size and position: a checkbox (not checked by default) – to tell the add-on to remember the size and the position of the Notetaker dialog when creating or editing a note. As such, when the user opens the dialog next time, the position and the size will be the same as the last time the dialog was used. The default position of this dialog is at the top left corner of the screen.
• 
Auto align text when editing notes (relevant for RTL languages): a checkbox (checked by default) – to control whether the text when creating or editing a note should be auto aligned according to the language used. This is mostly relevant for right to left languages. For example, if the language used is Arabic or Hebrew, then the text will be right aligned when this option is chosen, if the language is English or French, then the text will be left aligned.
Keyboard shortcuts
• 
NVDA + Alt + n: to open the Notetaker interface.
• 
NVDA + Alt + v: to open the Notes Manager interface.
Keyboard shortcuts in the different interfaces
Interface
Command
Keyboard shortcut
Notetaker
Focus the note edit area
Alt + n
Notetaker
Align text to the right
Control + r
Notetaker
Align text to the left
Control + l
Notetaker
Preview note in an HTML window
Alt + r
Notetaker
Copy
Alt + p
Notetaker
Copy HTML code
Alt + h
Notetaker
Save note as a Microsoft Word document
Alt + w
Notetaker
Update the note corresponding Microsoft Word document
Alt + w
Notetaker
Save and close
Alt + s
Notetaker
Discard
Alt + d
Notetaker
Open notes Manager
Alt + m
Notes Manager
View note
Alt + v
Notes Manager
Edit note
Alt + e
Notes Manager
Copy note
Alt + p
Notes Manager
Open in Microsoft Word (if such a document exists)
Alt + o
Notes Manager
Create a word document for a saved note
Alt + w
Notes Manager
Copy HTML code
Alt + h
Notes Manager
Delete note
Alt + d
Notes Manager
New note
Alt + n
Notes Manager
Open settings
Alt + s
Notes Manager
Close the interface
Alt + c
The settings interface
Ask me each time where to save the note's corresponding Microsoft Word document
Alt + w
The settings interface
Open the note's corresponding Microsoft Word document after saving or updating
Alt + o
The settings interface
Capture the active window title when creating a new note
Alt + c
The settings interface
Remember the note taker window size and position
Alt + r
The settings interface
Auto align text when editing notes (relevant for RTL languages)
Alt + t
Acknowledgements
• 
The add-on comes bundled with Pandoc, a wonderful tool which allows converting documents between different formats. Without this tool the add-on won’t be able to offer the capabilities it offers.""", "https://addons.nvda-project.org/files/get.php?file=quickNotetaker"],
	"Ignore Blanks Indentation Reporting":["2021.1 and beyond", """This is an NVDA addon that alters the reporting of indentation by disregarding blank lines when deciding whether to report changes in indentation. It is best understood by contrasting with normal behaviour with an example.
Consider this example:
def foo():
    x = 42

    return x

def bar():
The current behaviour of NVDA is to report indentation changes for any line where the indentation has changed, even if the line is blank. So, the example would be read like:
def foo():
tab x = 42
no indent blank
tab return x
no indent blank
def bar():
The disadvantage for this behaviour is that for most programming languages, like python, a blank line has no semantic significance and is just used to visually separate lines of code with no change to the code's meaning. Therefore, by reporting the change of indentation upon entering a blank line and then reporting it again after landing on the next line is just noise that makes it harder to focus on understanding the code.
This addon aims to improve on the behaviour by ignoring blank lines when computing indentation speech, thus the example is read like this instead:
def foo():
tab x = 42
blank
return x

no indent def bar():""", "https://addons.nvda-project.org/files/get.php?file=ibir"],
	"Search With":["2019.3 and beyond", """This addon helps you to search text, via various search engines. Let no text selected, and press the gesture of the addon, a dialog will be displayed, with an edit box to enter a search query, to search with Google press enter, or tab to search with other engins.
And if you want to search for selected text, select some text and press once, a menu will be displayed with various search engines to choose. and you can if you like, press the gesture twice to search selected text with Google directly.
The Default gesture for the addon is: NVDA+ Windows+ S. If the keystroke do not work for you, or conflict with other keystroke, you can as always add a gesture or change the existent one going to: NVDA menu>preferences>inputGestures>Search With category.
Usage
• If you want to enter a search query, just press the addon gesture. A dialog will be displayed, with an edit field to enter the search term.
• Want to search with Google? just press enter.
• Otherwise tab to Other Engines button, and give it a space, a popup menu will show up, with various search engines to choose. Yahoo, Bing, DuckDuckGo, and Youtube. This is the default menu, and you may modify it from addon's setting panel.
• Another way to use the addon, is by selecting some text. And on Pressing the addon's gesture, or any other you have assigned to it, a virtual menu will be displayed with various search engines, either the default menu, or any other you have tailed to your needs.
• Choose one and press enter, the default browser will open displaying search results. or, if you want to search with Google directly, press the gesture twice, and you are done.
• Want to trigger search menu specifically for clipboard or last spoken text? OK, then you can from input gestures dialog, assigned a gesture for:
• Trigger search menu for clipboard text, and pressed twice searches that text by Google directly.
• Trigger search menu for last spoken text, and pressed twice searches that text by Google directly.
• Want to modify Search with menu? Yes you can do that from the setting panel, and adjust the menu to fit to your mood and needs.
• You can from there, add to Search with menu, other available search engines. And you can if you like, remove an item from it, move item up, move item down, or return and set menu to default state.
• If you want these modifications to be permanent, you have to save configuration after wards.
• Want to search Google using other language options?
• 
Then, go to Search With category in setting panels, from the cumbo box there, you can choose search Google either:
• Using browser settings and language.
• Using NVDA language.
• Using windows language.
• 
Moreover, you have the option to choose the default query in Search with dialog. From the Options for default query combo box in setting panel, you can choose either
• Leave blank
• Use clipboard text
• Use last spoken text
• 
And if clipboard or last spoken text is chosen, text in search box will be displayed selected, so that you can easily override it.
• Lastly, especially for advanced users
• You can through a check box in setting panel, choose if you want to preserve your data folder upon installing a new version. Be aware, choosing that you will not get new search engines, if any were included in the new addon version. And that's it, hope to search for good and find it, happy searching!""", "https://addons.nvda-project.org/files/get.php?file=searchwith"],
	"Event Tracker":["2021.2 and beyond", """This add-on outputs information about objects for which events were fired. Properties recorded in debug log mode include object type, name, role, event, app module, and accessibility API specific information such as accName for IAccessible object and Automation Id for UIA objects.
Notes:
• This add-on is designed for developers and power users needing to track events coming from apps and various controls.
• In order to use the add-on, NVDA must be logging in debug mode (configured from general settings/logging level, or restart with debug logging enabled).
• It might be possible that add-ons loaded earlier than Event Tracker may not pass on the event to other add-ons, including Event Tracker. If this happens, Event Tracker will not be able to log events.
• Events are handled from global plugins, app modules, tree interceptors, and NVDA objects, in that order.
Events and their information
The following events are tracked and recorded:
• Focus manipulation: gain focus, lose focus, focus entered, foreground
• Changes: name, value, state, description, live region
• UIA events: controller for, element selected, item status, layout invalidated, notification, text change, tooltip open, window open
For each event, the following information will be recorded:
• Event name
• Object
• Object name
• Object role
• Object value or state depending on events
• App module
• For IAccessible objects: acc name, child ID
• For UIA objects: Automation Id, class name, notification properties if recording notification event information, child count for layout invalidated event""", "https://addons.nvda-project.org/files/get.php?file=evttracker"],
	"PC Keyboard Braille Input for NVDA":["2019.3 +", """This NVDA add-on allows braille to be entered via the PC keyboard. Currently, the following keyboard layouts are supported:
• English QWERTY keyboard.
• French (France).
• German (Germany).
• Italian (Italy).
• Persian.
• Portuguese (Portugal).
• Spanish (Spain and Mexico).
• Turkish.
How to configure
The add-on can be configured from its category in the NVDA's settings dialog, under NVDA's menu, Preferences submenu. A gesture for opening the add-on settings panel can be assigned from Input gestures dialog, configuration category.
Check the corresponding checkbox if you want to type using only one hand, or ensure it's not checked if you prefer to type using the standard mode (two hands).
You can also select if NVDA should speak a single typed dot (using )the feature of "one hand mode").
كيفية الاستخدام
. 1Press NVDA+0 to enable braille input. This gesture can be changed from Input gestures dialog, Braille category.
. 2
Type braille by pressing keys together on the PC keyboard as if it were a braille keyboard.
• 
If you want to enter text using two hands, use the following keys if you work with a QWERTY English keyboard, or the keys located at the corresponding positions in other layouts:
• f, d and s for dots 1, 2 and 3 respectively.
• j, k and l for dots 4, 5 and 6 respectively.
• Use the keys a and ; (semi-colon) for dots 7 and 8, respectively.
• You can also use the keys on the row above; i.e. q, w, e, r, u, i, o and p.
• 
If you want to type text using one hand, you can compose characters pressing keys simultaneously or in several keystrokes, adding the dots corresponding to the desired character. Press g or h to type the character when you have added all its dots. If you make a mistake building a character, you can clear the dots before typing it by pressing t or y. The keys used in QWERTY English keyboard are the following:
• Left hand: f, d, s, r, e, w, a, q for dots 1, 2, 3, 4, 5, 6, 7 and 8.
• Right hand: j, k, l, u, i, o, ; (semicolon), p for dots 1, 2, 3, 4, 5, 6, 7 and 8.
. 3
You can press most other keys as normal, including space, backspace, enter and function keys. Take care about not pressing alt+shift, since changing the keyboard layout may affect the entered dots.
. 4Press space bar in combination with braille dots to move the system cursor (or report the current line), just if you were using a braille display. For example, space+dot1 to emulate upArrow, space+dot4+dot5+dot6 to emulate control+end, space+dot1+dot4 to report the current line, etc.
. 5Press NVDA+0 to disable braille input.""", "https://addons.nvda-project.org/files/get.php?file=pckbbrl"],
	"Windows Magnifier":["2018.3 and beyond", """This add-on improves the use of Windows Magnifier with NVDA.
Features
• Allows to report the result of some native Magnifier keyboard commands.
• Allows to reduce the cases where table navigation commands conflict with Magnifier's commands.
• Adds some keyboard shortcuts to toggle various Magnifier options.
Settings
The setting panel of Windows Magnifier add-on allows to configure how NVDA reacts to native Windows Magnifier commands. You may want to have more or less commands reported according to what you are able to see. This panel may be opened choosing Preferences -> Settings in the NVDA menu and then selecting the Windows Magnifier category in the Settings window. The keyboard shortcut NVDA+Windows+O then O also allows to open this settings panel directly.
The panel contains the following options:
• 
Report view moves: controls what is reported when you move the view with Control+Alt+Arrows commands. The three options are:
• Off: Nothing is reported.
• With speech: a speech message indicates the position of the zoomed view on the dimension the view is being moved.
• With tones: a tone is played and its pitch indicates the position of the zoomed view on the dimension the view is being moved.
This option only affects full view mode.
• 
Report turn on or off: If checked, the Magnifier's state is reported when you use Windows++ or Windows+Escape commands to turn it on or off.
• Report zoom: If checked, the Magnifier's zoom level is reported when you use Windows++ or Windows+- zoom commands.
• Report color inversion: If checked, the color inversion state is reported when you use the control+Alt+I toggle command.
• Report view change: If checked, the view type is reported when you use a command that changes the view type (Control+Alt+M, Control+Alt+F, Control+Alt+D, Control+Alt+L)
• Report lens or docked window resizing: If checked, a message is reported when you use the resizing commands (Alt+Shift+Arrows). In docked window mode, the height or the width is reported. In lens mode, the new dimension cannot be reported for now. These resizing command do not seem to be available on all versions of Windows; if your Windows version does not support them, you should keep this option unchecked.
• 
In documents and list views, pass control+alt+arrows shortcuts to Windows Magnifier: There are three possible choices:
• Never: The command is not passed to Windows Magnifier and standard NVDA table navigation can operate. When used in documents out of a table, the Control+Alt+Arrow command reports a "Not in a table" error message. This is the standard behaviour of NVDA without this add-on.
• Only when not in table: In table or in list views, Control+Alt+Arrow commands perform standard table navigation. When used in documents out of a table, Control+Alt+Arrow commands perform standard Magnifier view move commands. If you still want to move Windows Magnifier view while in table or in list view, you will need to press NVDA+F2 before using Control+Alt+Arrow commands. This option is the best compromise if you want to use Control+Alt+Arrow for both Magnifier and table navigation.
• Always: Control+Alt+Arrow commands moves the Magnifier's view in any case. This option may be useful if you do not use Control+Alt+Arrow to navigate in table, e.g. because you have changed table navigation shortcuts in NVDA or because you exclusively use Easy table navigator add-on for table navigation.
Commands added by this add-on
In addition to native Magnifier commands, this add-on provide additional commands that allow to control Magnifier's options without opening its configuration page. All the commands added to control Magnifier options are accessible through the Magnifier layer command NVDA+Windows+O:
• NVDA+Windows+O then C: Toggles on or off caret tracking.
• NVDA+Windows+O then F: Toggles on or off focus tracking.
• NVDA+Windows+O then M: Toggles on or off mouse tracking.
• NVDA+Windows+O then T: Toggles on or off tracking globally.
• NVDA+Windows+O then S: Toggles on or off smoothing.
• NVDA+Windows+O then R: Switches between mouse tracking modes (within the edge of the screen or centered on the screen); this feature is only available on Windows 10 build 17643 or higher.
• NVDA+Windows+O then X: Switches between text cursor tracking modes (within the edge of the screen or centered on the screen); this feature is only available on Windows 10 build 18894 or higher.
• NVDA+Windows+O then V: Moves the mouse cursor in the center of the magnified view (command available in full screen view only).
• NVDA+Windows+O then O: Opens Windows Magnifier add-on settings.
• NVDA+Windows+O then H: Displays help on Magnifier layer commands.
There is no default direct gesture for each command, but you can attribute one normally in the input gesture dialog if you wish. The same way, You can also modify or delete the Magnifier layer access gesture (NVDA+Windows+O). Yet, you cannot modify the shortcut key of the Magnifier layer sub-commands.
Magnifier's native commands
The result of the following Magnifier native commands may be reported by this add-on, according to its configuration:
• Start Magnifier: Windows++ (on alpha-numeric keyboard or on numpad)
• Quit Magnifier: Windows+Escape
• Zoom in: Windows++ (on alpha-numeric keyboard or on numpad)
• Zoom out: Windows+- (on alpha-numeric keyboard or on numpad)
• Toggle color inversion: Control+Alt+I
• Select the docked view: Control+Alt+D
• Select the full screen view: Control+Alt+F
• Select the lens view: Control+Alt+L
• Cycle through the three view types: Control+Alt+M
• Resize the lens with the keyboard: Shift+Alt+Left/Right/Up/DownArrow. Note: although this does not seem to be documented, this shortcut seems to have been withdrawn in recent Windows versions such as Windows 2004.
• Move the magnified view: Control+Alt+Arrows (reporting only affects full screen mode)
Here is also a list of other Magnifier native commands, just for information:
• Control+Alt+mouseScrollWheel: Zooms in and out using the mouse scroll wheel.
• Control+Windows+M: Opens the Magnifier's settings window.
• Control+Alt+R: Resizes the lens with the mouse.
• Control+Alt+Space: Quickly shows the entire desktop when using full screen view.
None of the Magnifier native commands can be modified.
Notes
• For computers equipped with an Intel graphic card, control+alt+arrow (left/right/up/down) are also shortcuts to modify the orientation of the screen. These shortcut are enabled by default and conflict with Windows Magnifiers shortcuts to move the view. You will need to disable them to be able to use them for the Magnifier. They can be disabled in the Intel control panel or in the Intel menu present in the system tray.
• 
Depending on your Windows version, Alt+Shift+Arrow are Windows Magnifier shortcuts to resize the magnified view (lens or docked). When Magnifier is active (even in full screen mode), these shortcuts are captured by Magnifier and cannot be passed to the application, even if you press NVDA+F2 before. To use these shortcuts in the current application, you need to quit the Magnifier (Windows+Escape) and re-open it after (Windows++). For example in MS word, to decrease title level:
• Press Windows+Escape to quit Magnifier.
• Press Alt+Shift+RightArrow to decrease current title level.
• Press Windows++ to re-open the Magnifier.
• 
For more information about Windows Magnifier's features and shortcuts, you may want to consult the following pages:
• Use Magnifier to make things on the screen easier to see
• Windows keyboard shortcuts for accessibility""", "https://addons.nvda-project.org/files/get.php?file=winmag"],
	"Direct Link":["2019.3 and beyond", """The purpose of the addon is to convert the Dropbox, Google Drive or oneDrive (both personal and business) links to a direct link, furthermore, it generates a direct link to a WhatsApp chat with the chosen selected phone number.
Usage
• Select or copy a shared Dropbox, Google Drive or oneDrive link
• Press alt+NVDA+l to convert the link. The resulting URL will be in your clipboard.
• Similarly for the phone number, copy or select the number you like to chat with or share and press the same shortcut (alt+NVDA+L).
• if you like to open the resulted link in your browser, press alt+NVDA+shift+l.
Why the direct link?
A direct link will allow you to get the well-known save dialog box directly if you open it in the browser, without being hassled by the hosting company download page and locating the download link. Moreover, the direct link can be used to stream a file or view a file in certain programs such as media players (if coming with URL support). Likewise, if WhatsApp is common in your country, rather than creating a new contact each time if you need to chat with someone, weather it is a customer or technical support, you can simply select the number or copy it and start chatting right away. Even more, you can share the WhatsApp link of your own number if people usually need to contact you in case you work as a freelancer.
Notes
• A link of a folder cannot be converted; the link has to be directing to a file.
• Make sure the link you are sharing is public (anyone with the link can access) in order for it to be successfully converted.
• You can change the hotkeys from the NVDA menu> preferences> input gestures.
• If you find a certain format of a phone number that is not detected, you can email me with an example.
• Certain type of files and sizes in Google Drive might take you to a page that says "Google Drive can't scan this file for viruses." in that case, you have to click on download anyway link.""", "https://addons.nvda-project.org/files/get.php?file=directlink"],
	"NVDA Unmute":["2019.3 and beyond", """This add-on checks the status of the Windows audio system when NVDA starts. And, if it turns out that the sound is muted - the add-on forcibly turns it on.
At the same time, the volume level is checked separately for the NVDA process.
The add-on also checks the status of the speech synthesizer. If there are problems with its initialization, attempts are made to start the synthesizer, which is specified in the NVDA settings.
There is an additional opportunity to check on which audio device the NVDA sound is output. And, if this device differs from the default device, the output automatically switches to the audio device installed in the system as the main one.
Note: If the add-on startup sound always plays even if the NVDA volume is online. That is, the add-on switches the output to the main audio device each time you start NVDA.
This occurs when the audio output device is in the NVDA settings is differ from the default output device or "Microsoft Sound Mapper".
This can be easily solved in one of the following ways:
. 1After restarting NVDA, just save the current configuration using NVDA+Ctrl+C. The default audio device will be saved in the NVDA settings and switching will not occur each time when NVDA starts.
. 2If you don't want to change the NVDA configuration - just disable the function of switching audio devices in the Unmute settings panel.
Add-on settings dialog
To open the add-on settings panel, follow these steps:
• Press NVDA+N to open NVDA menu.
• Then go to "Preferences" -> "Settings..." and in the categories list find and open "Unmute Windows Audio".
That's it, you can now use the Tab key to move between add-on settings.
The following options are available in the add-on settings dialog:
. 1
The first slider in the add-on settings dialog allows you to specify the volume level of Windows, which will be set when you start NVDA if the sound was previously muted or was too low.
. 2
The minimum Windows volume level at which the volume up procedure will be applied. This slider allows you to adjust the sensitivity level of the add-on.
If the volume level drops to less than the value specified here, the volume will be increased the next time you start NVDA.
Otherwise, if the volume level remains higher than the value specified here, then when you restart NVDA, its level will not change.
And, of course, if the sound was previously turned off, when restarts add-on will turn it on anyway.
. 3
The following check box allows to enable re-initialization of the voice synthesizer driver.
This procedure will only start if it is detected at NVDA startup that the voice synthesizer driver has not been initialized.
. 4
In this field you can specify the number of attempts to re-initialize the voice synthesizer driver. Attempts are performed cyclically with an interval of 1 second. A value of 0 means that attempts will be performed indefinitely until the procedure is successfully completed.
. 5
The "Switch to the default output audio device" option allows to check at startup the audio device on which NVDA sound is output. And, if this device differs from the default device, the output automatically switches to the audio device installed in the system as the main one.
. 6
The next checkbox turns on or off playing the startup sound when the operation is successful.
Third Party components
The add-on uses the following third-party components:
• For interaction with the Windows Core Audio API - PyCaw module that is distributed under the MIT license.
• For getting the information about running processes and using the PyCaw component - psutil module that is distributed under BSD-3 license.""", "https://addons.nvda-project.org/files/get.php?file=unmute"],
	"Check Input Gestures":["2019.3 and beyond", """Find and fix input gestures conflicts in NVDA and add-ons. The general term "input gestures" includes keyboard commands, commands entered from Braille keyboards and gestures of touch screens.
Each of the installed add-ons can make changes to the NVDA configuration by adding or reassigning existing input gestures. If the same input gestures are binded to several functions, it will be impossible to call some of them.
Search for duplicate gestures
To detect duplicate gestures, call the NVDA menu, go to the "Tools" submenu, then - "Check Input Gestures" and activate the menu item "Search for duplicate gestures...".
After that, all input gestures used in NVDA will be checked in the following order:
. 1globalCommands;
. 2globalPlugins.
If the same input gestures will be detected, which are assigned to different functions, their list will be displayed in a separate dialog box.
After pressing the Enter key on the selected list item, the corresponding NVDA function will be selected and opened in the standard "Input Gestures..." dialog, where you can delete or reassign the associated gesture.
Note: As you know, features that don't have a text description do not appear in the "Input Gestures..." dialog. Therefore, after activating such an element, the corresponding warning will be displayed.
Gestures without description
To view the list of gestures binded with functions without a text description, if they are found in your NVDA configuration, you need to call the NVDA menu, go to the submenu "Tools", then - "Gestures without description...".
Such features do not appear in the standard NVDA "Input Gestures..." dialog, so it is not yet possible to delete or reassign associated gestures.
Help
One way to view this help page is to call up the NVDA menu, go to the "Tools" submenu, then - "Check Input Gestures", and activate "Help".
Note: All features of the add-on are presented in the NVDA "Input Gestures" dialog and you can assign your own keyboard shortcuts to each of them.
Contributions
We are very grateful to everyone who made the effort to develop, translate and maintain this add-on:
• Wafiqtaher - Arabic translation;
• Angelo Miguel Abrantes - Portuguese translation;
• Cagri Dogan - Turkish translation.""", "https://addons.nvda-project.org/files/get.php?file=cig"],
	"NVDAUpdate Channel Selector":["2019.1 / 2021.1", """This add-on allows you to download and install the latest NVDA version of the chosen type without visiting any webpage nor using your web browser. It is useful when, for example, you want to test new features in a NVDA snapshot and then return back to the most recent stable release. If you test regularly NVDA snapshots and you usually install them in your computer, you will save a lot of time with this add-on. If you prefer testing snapshots in portable mode keeping your installed copy of NVDA unchanged, this add-on is for you as well.
Usage
You can change the NVDA update channel by going to NVDA menu, Preferences, Settings, Update channel category. Once you choose the desired channel and press OK, wait until the next automatic update check or go to NVDA help menu and choose "Check for updates" option. For now, these are the available channels:
• Default: this is the default channel used by your NVDA version. Choosing this option means the same as disabling the add-on.
• Stable: force update channel to stable. Useful when you want to return to a stable version from a snapshot.
• Stable, rc and beta: this is the channel for beta releases. You will receive the first beta version once it is released. This channel allows you to update through betas and release candidates until you reach the next stable version.
• Alpha (snapshots): choose this option to update to the latest alpha. Alpha snapshots allows you to test new features, but they are quite unstable. Please, be careful.
• Disable updates (not recommended): this option disables the update channel. If you check for updates an error message will be displayed. Remember that you can disable automatic updates from the General settings category. Use this option only with testing purposes.
Information about available updates for each channel will be retrieved in the background once the settings panel is opened. Press tab to navigate to a read only edit field, where you can see this information. This information will be dynamically updated when you change the update channel from the combo box. If there is an update available for the selected channel, one or two links will appear next to the edit field:
• Download: press spacebar on this link to open it in your web browser and download the latest installer.
• View changelog: press spacebar on this link to open the What's new document in your web browser. For some channels, this link won't be displayed.""", "https://addons.nvda-project.org/files/get.php?file=updchannelselect"],
	"Proxy support for NVDA":["2019.3 / 2021.1", """This add-on allows the NVDA screen reader to connect to the Internet through one or more proxy servers. To make it possible, it applies various patches to the standard Python library or modifies certain environment variables, depending on the chosen configuration. You will be able to update NVDA and their add-ons automatically from your corporate environment and even perform remote sessions, provided that your organization proxy server allows it.
Features
• Support for various proxy server types: http, socks4 and socks5.
• Ability to redirect all traffic through the proxy server or only specific traffic (http, https, ftp).
• Ability to redirect all traffic through a proxy server and, after that, redirect specific traffic through other servers (nested proxies).
• Profile switch and config reset aware: if you usually work with a portable copy of NVDA, you can create various profiles for different environments (home, work, office1, office2) and manually activate them.
Usage
This add-on adds a new category to the NVDA settings dialog called "Proxy". In this category, you will find four settings groups. The first one allows you to configure a general proxy for all traffic. The other groups allow you to configure proxy servers only for specific protocols. All groups have the following fields:
• Host: hostname or ip address of the proxy server. Leave empty to disable that particular proxy.
• Port: server port.
• Username: optional. User name for server autentication.
• Password: optional. Password for server autentication. Note that password is not required for socks4 servers.
In addition to the previous fields, the following options are available in the first settings group:
• SOCKS proxy type: socks4, socks5 or http can be selected.
• Use proxy for dns requests if possible: when this checkbox is checked, hostnames or domain names will be directly sent to and resolved on the proxy server. When it is unchecked, names will be resolved locally and the server will receive only the destination ip address. Note that not all socks4 proxy servers support this option.
Tipically, most users will only have to configure the first settings group. If you don't know your proxy details, ask your organization network administrator for more information.
Limitations
• Very limited IPV6 support.
• UDP traffic is not supported on all proxy servers.
• External DLL libraries won't respect the settings configured in this add-on.
• Only basic autentication is supported for http proxy servers. Digest autentication is not supported.
• In order to redirect all traffic (including https connections) through an http proxy, the server must support the CONNECT http method.
• A "direct connection" mode can't be configured. If you disable a specific proxy, the system default will be used instead.""", "https://addons.nvda-project.org/files/get.php?file=nvdaproxy"],
	"WordNav":["2019.3 +", """WordNav NVDA add-on improves built-in navigation by word, as well as adds extra word navigation commands with different definition for the word.
Most text editors support Control+LeftArrow/RightArrow commands for word navigation. However the definition of the word changes from one program to another. This is especially true of modern web-based text editors, such as Monaco. NVDA should know the definition of word in given program in order to speak words correctly. If NVDA doesn't know the exact definition, then either words are going to be skipped, or pronounced multiple times. Moreover, some web-based text editors position the cursor in the end of the word, instead of the beginning, making editing much harder for visually impaired users. In order to combat this problem I have created enhanced word navigation commands, that take the word definition from Notepad++ and they do not rely on program's definition of words, but rather parse lines into words on NVDA's side. The Control+LeftArrow/RightArrow gesture is not even sent to the program, thus ensuring the consistency of the speech.
Please note that a prototype of WordNav was formerly a part of Tony's enhancements add-on. Please either uninstall it or upgrade to Tony's enhancements latest stable version to avoid conflicts.
Currently WordNav supports four definitions of the word, assigned to different gestures:
• Left Control+Arrows: Notepad++ definition, that treats alphanumeric characters as words, and adjacent punctuation marks are also treated as words. This should be the most convenient word definition for the majority of users.
• RightControl+Arrows: Fine word definition splits camelCaseIdentifiers and underscore_separated_identifiers into separate parts, thus allowing the cursor to go into long identifiers.
• LeftControl+Windows+Arrows: Bulky word definition treats almost all punctuation symbols adjacent to text as part of a single word, therefore it would treat paths like C:\directory\subdirectory\file.txt as a single word.
• RightControl+Windows+Arros: Multiword definition, that groups several words together. The amount of words is configurable.
Gestures can be customized in WordNav settings panel.
Notes
• At this time WordNav doesn't modify Control+Shift+LeftArrow/RightArrow gestures to select words, since implementation of such commands are significantly more complicated.
• If you would like to use virtual desktops feature of Windows 10, please remember to disable Control+Windows+Arrows keyboard shortcuts either in WordNav Settings panel, or in NVDA Input gestures dialog.
• WordNav doesn't work reliably in VSCode, since due to its internal optimizations, VSCode presents only a few lines of file contents at a time, that change dynamically, and this occasionally interferes with WordNav algorithm.""", "https://addons.nvda-project.org/files/get.php?file=wordnav"],
	"Win Wizard":["2019.3 and beyond", """This add-on allows you to perform some operations on the focused window or the process associated with it.
Keyboard commands:
All these commands can be remapped from the Input gestures dialog in the Win Wizard category.
Hiding and showing hidden windows:
• NVDA+Windows+numbers from 1 to 0 - hides currently focused window in the slot corresponding to the pressed number
• NVDA+Windows+left arrow - moves to the previous stack of hidden windows.
• NVDA+Windows+right arrow - moves to the next stack of hidden windows.
• Windows+Shift+h - hides the currently focused window in the first available slot
• NVDA+Windows+h - shows the last hidden window
• Windows+Shift+l - shows the list of all hidden windows grouped by the stacks (please note that by default last hidden window is selected)
Managing processes:
• Windows+F4 - kills the process associated with the currently focused window
• NVDA+Windows+p - opens dialog allowing you to set priority of the process associated with the currently focused window
Miscellaneous commands:
• NVDA+Windows+TAB - switches between top level windows of the current program (useful in foobar2000, Back4Sure etc.) Since this command moves the system focus it can be found in the System focus category of the Input gestures dialog.
• CTRL+ALT+T - allows you to change title of the currently focused program""", "https://addons.nvda-project.org/files/get.php?file=winwizard"],
	"Console Toolkit":["2019.3 and later", """Console Toolkit is NVDA add-on, that provides accessibility improvements for Windows console, also known as Command prompt. It also works well in Windows PowerShell. Some of the features may work in alternative terminals, such as Cygwin, PuTTY and Windows Terminal, however, the add-on has only been carefully tested with the default Windows Console. SSH users might find this add-on especially handy.
Some of the features were previously part of Tony's enhancements add-on.
Downloads
Console toolkit
Real-time console speech
This option makes NVDA to speak new lines immediately as they appear in console output, instead of queueing new speech utterances. For example, if NVDA is busy speaking a line that appeared on the screen 1 minute ago, and now a new line appears, this option will cancel speaking the old line and start speaking the new line right away, thus providing a more real-time feedback on what's happening in console window.
Beep on console updates
Beep a low pitch impulse every time console text is updated.
Enforce Control+V in consoles
This option makes Control+V shortcut to work inside ssh sessions.
Experimental: command prompt editing
Note: this feature is experimental. Please read this section carefully and make sure you understand how it works before reporting issues.
Press NVDA+E to identify current prompt in console window and edit it in an accessible "Edit prompt" window. After editing you can either press Escape to update current command line, or Enter to update and immediately execute command. Alternatively you can press Alt+F4 to close edit prompt window without updating command line.
This feature has been tested in Windows command prompt cmd.exe as well as in bash shell over ssh connections, as well as in WSL and cygwin. It might also work in alternative Unix shells, however it hasn't been tested.
Here is how add-on extracts current command.
. 1It presses End key and then sends a control character, that is a rare Unicodecharacter not likely to be used anywhere.
. 2Then it presses home key and sends another control character.
. 3Then it waits for control characters to appear on the screen, which might take some time on slow SSH connections.
. 4Command is what appears between two control characters.
. 5When "Use UI Automation to access the Windows Console when available" option is enabled in NVDA settings, it sends one more control character in the beginning of the string. This is needed to parse multiline commands correctly: UIA implementation trims whitespaces in the end of each line, so in order to deduce whether there is a space between two lines, we need to shift them by one character. Please note, however, that this way we don't preserve the number of spaces between words, we only guarantee to preserve the presence of spaces.
. 6Before editing add-on makes sure to remove control characters by placing cursor in the beginning and end and simulating Delete and Backspace key presses.
. 7It presents command in "Edit prompt" window for user to view or edit.
. 8
After user presses Enter or Escape,it first erases current line in the console. This is achieved via one of four methods, the choice of the method is configurable. Currently four methods are supported:
• Control+C: works in both cmd.exe and bash, but leaves previous prompt visible on the screen; doesn't work in emacs; sometimes unreliable on slow SSH connections
• Escape: works only in cmd.exe"),
• Control+A Control+K: works in bash and emacs; doesn't work in cmd.exe
• Backspace (recommended): works in all environments; however slower and may cause corruption if the length of the line has changed
. 9
Then add-on simulates keystrokes to type the updated command and optionally simulates Enter key press.
Troubleshooting:
• Verify that 'Home', 'End', 'Delete' and 'Backspace' keys work as expected in your console.
• Verify that your console supports Unicode characters. Some ssh connections don't support Unicode.
• Verify that selected deleting method works in your console.
Experimental: capturing command output
Note: this feature is experimental. Please read this section carefully and make sure you understand how it works before reporting issues.
While in command line or in "Edit prompt" window, press Control+Enter to capture command output. This add-on is capable of capturing large output that spans multiple screens, although when output is larger than 10 screens capturing process takes significant time to complete. Add-on will play a long chime sound, and it will last as long as the add-on is capturing the output of currently running command, or until timeout has been reached. Alternatively, press NVDA+E to interrupt capturing.
When "Use UI Automation to access the Windows Console when available" feature is enabled in NVDA settings, you can switch to other windows while capturing is going on. However, if this option is disabled, then NVDA is using a legacy console code, that only works when consoel is focused, and therefore switching to any other window will pause capturing.
Command capturing works by redirecting command output to less command. Default suffix that is appended to commands is: |less -c 2>&1 Please only change it if you know what you're doing. This add-on knows how to interact with the output of less command to retrieve output page by page.
On Windows less.exe tool needs to be installed separately. You can install it via cygwin, or download a windows binary elsewhere.
If you are using tmux or screen in Linux, please make sure that no status line is displayed in the bottom. In tmux run tmux set status off to get rid of status line, or modify your tmux.conf file.
Troubleshooting:
• After a failed output capturing attempt, press UpArrow in the console to check what command has actually been executed.
• Revert back to default capturing suffix, mentioned above.
• Try troubleshooting steps from "command prompt editing" section.""", "https://addons.nvda-project.org/files/get.php?file=consoletoolkit"],
	"Quick Dictionary":["2019.3 / 2020.3", """Welcome to NVDA Quick Dictionary addon, which will allow you to quickly get a dictionary article with the translation of a word or phrase into your chosen language by pressing a key combination. There are few basic keyboard shortcuts and they are all intuitive and convenient so you will remember them quickly.
Dictionary articles contain detailed information about a word, such as part of speech, gender, plural or singular, translation options, list of meanings, synonyms and detailed examples. Such information will be useful for people who are learning foreign languages, or seek to use in communication all the richness and diversity of their own language.
The add-on supports several online dictionary services. You can select the desired remote dictionary in the appropriate dialog box or by using keyboard shortcuts. Each available service has its own settings panel.
There are also advanced opportunities for working with profiles of the voice synthesizers. You can associate a voice synthesizer profile with a specific language, after that translations into this language will be automatically voiced by the selected synthesizer.
Below are all the features of the add-on and keyboard shortcuts to control them. By default all functions are called using two-layer commands. But for any of these methods you can always assign convenient for you keyboard shortcuts. You can do it in the NVDA "Preferences" -> "Input gestures..." dialog.
Receiving a dictionary article
In order to get an article from the dictionary, you must first select the word you are interested in or copy it to the clipboard. Then just press NVDA+Y twice. There is also another way to get a dictionary entry: pressing NVDA+Y once switches the keyboard to add-on control mode, then just use the D key.
Add-on control mode
To access all the features of the add-on, you need to switch to add-on control mode, you can do this by pressing NVDA+Y once. You will hear a short low beep and will be able to use the other commands described below. When you press a key that is not used in the add-on, you will hear another signal notifying you of an erroneous command and the add-on control mode will be automatically turned off.
Add-on commands list
Basic dictionary commands:
• D - announce a dictionary entry for a selected word or phrase (same as NVDA+Y);
• W - show dictionary entry in a separate browseable window;
• S - swap languages and get Quick Dictionary translation;
• A - announce the current source and target languages;
• C - copy last dictionary entry to the clipboard;
• E - edit text before sending;
• U - download from online dictionary and save the current list of available languages;
• function keys - select online dictionary service;
• Q - statistics on the using the online service;
• F - choose online service.
Voice synthesizers profiles management:
• from 1 to 9 - selection of the voice synthesizer profile;
• G - announce the selected profile of voice synthesizers;
• B - back to previous voice synthesizer;
• R - restore default voice synthesizer;
• Del - delete the selected voice synthesizer profile;
• V - save configured voice synthesizer profile;
• P - display a list of all customized voice synthesizers profiles.
Press O to open add-on settings dialog.
Help on add-on commands
You can see a list of all the commands used in the add-on as follows:
• Via the NVDA menu - by pressing NVDA+N, go to the submenu "Tools", then - "Quick Dictionary" and activate the menu item "Help on add-on commands".
• Press the H key in add-on control mode (NVDA+Y).
Add-on help
To open the add-on help - press NVDA+N, go to the "Tools" submenu, then - "Quick Dictionary" and activate the menu item "Help".
Contributions
We are very grateful to everyone who made the effort to develop, translate and maintain this add-on:
• Cagri Dogan - Turkish translation;
• Wafiqtaher - Arabic translation.
Several good solutions from other developments were used in the Quick Dictionary add-on. Thanks to the authors of the following add-ons:
• Instant Translate - Alexy Sadovoy, Beqa Gozalishvili, Mesar Hameed, Alberto Buffolino and other NVDA contributors.
• To work with voice synthesizers profiles were used ideas from the Switch Synth add-on (thanks to Tyler Spivey).""", "https://addons.nvda-project.org/files/get.php?file=quickdictionary"],
	"Numpad Nav Mode":["unnown", """Numpad Nav Mode is an NVDA add-on, which allows you to easily switch your keyboard's numpad between NVDA's navigation controls and the non-screenreader Windows navigation controls.
The normal functions of the PC number pad, with numlock off, are: page up, page down, home, end, four-way arrow keys, and a delete key. But NVDA completely takes over the numpad, to provide review keys, mouse controls, and object navigation controls. This is true even in laptop keyboard mode, which duplicates those functions on non-numpad keys for those who do not have a numpad.
However some users do have a numpad on their laptop, and would prefer to use it for Windows navigation purposes, especially because some laptops do not provide home, end, or other such keys. That is where this add-on can help. Additionally, some desktop users may sometimes find it convenient to use the numpad for those keyboard functions rather than the normal keys, which this add-on enables.
How it works
With numlock off, no matter what keyboard layout you are using, this add-on will let you press Alt+NVDA+NumpadPlus (which is usually the long key second up on the right), to quickly and easily switch between the normal NVDA navigation controls, and the classic Windows navigation controls. This key can be remapped under Input Gestures, in the Input section.
Note that this add-on doesn't disable the use of numpad insert as an NVDA modifier, if you have it set as such. If you want that feature, please let me know, although you can manually turn off numpad insert as a modifier in NVDA keyboard settings.
If you would prefer to have NVDA start with the Windows nav mode active by default, you can configure that in NVDA configuration. Go to NVDA's preferences, then settings, and find the Numpad Nav Mode settings panel. There you will be able to select a checkbox to turn Windows Nav Mode on by default when you start NVDA. To get there quickly, press NVDA+N, P, S, then N one or more times until you hear "Numpad Nav Mode".""", "https://addons.nvda-project.org/files/get.php?file=numpadNav"],
	"Zoom Accessibility Enhancements":["2018.4 / 2020.2", """This add-on improves the experience of using Zoom for NVDA users by providing keyboard shortcuts to Handle alerts for Different events While In a meeting, make the process of remote control much more accessible and smoother, and more.
keyboard shortcuts for controlling alerts In meetings
• 
NVDA + Shift + A: cycles between different modes of reporting alerts. The following modes are available:
• Report all alerts mode, where all alerts are reported as usual
• Beep for alerts, where NVDA will play a short beep for every alert displayed in Zoom
• Silence all alerts, where NVDA will ignore all alerts
• Custom mode, Where the user can customize which alerts they want to have and which not. This can be done using the settings dialog of the add-on, or by using the dedicated keyboard shortcuts for that
The following shortcuts can be used to toggle on / off the announcements of each type of alert (note that this will be effective when custom mode is selected):
• NVDA + Ctrl + 1: Participant Has Joined/Left Meeting (Host Only)
• NVDA + Ctrl + 2: Participant Has Joined/Left Waiting Room (Host Only)
• NVDA + Ctrl + 3: Audio Muted by Host
• NVDA + Ctrl + 4: Video Stopped by Host
• NVDA + Ctrl + 5: Screen Sharing Started/Stopped by a Participant
• NVDA + Ctrl + 6: Recording Permission Granted/Revoked
• NVDA + Ctrl + 7: Public In-meeting Chat Received
• NVDA + Ctrl + 8: Private In-meeting Chat Received
• NVDA + Ctrl + 9: In-meeting File Upload Completed
• NVDA + Ctrl + 0: Host Privilege Granted/Revoked
• NVDA + Shift + Ctrl + 1: Participant Has Raised/Lowered Hand (Host Only)
• NVDA + Shift + Ctrl + 2: Remote Control Permission Granted/Revoked
• NVDA + Shift + Ctrl + 3: IM chat message received
Note that you need to leave reporting all alert types selected (in Zoom accessibility settings) to have the add-on function as expected.
Keyboard shortcut for Opening add on Dialogue
NVDA + Z Opens the add-on dialog !
Using this dialog you can :
• See which alerts are announced and which aren't
• Select the types of the alerts you want to be announced
• Choose alerts reporting mode
• Save custom changes
Remote control
after a remote control permission is granted, NVDA + O will move the focus in /Out of the remote controlled screen
Note that the focus should be on one of the meeting controls to be able to remote control the other screen
An Important note
Currently the feature of custom alerts mode where the user can choose which alerts they want to have and which not works with Zoom only when the user interface language is set to english.""", "https://addons.nvda-project.org/files/get.php?file=zoom"],
	"Kill NVDA":["2019.2 / 2019.3", """This add-on is designed to temporarily kill NVDA, so that you can recover if it freezes.
Usage
. 1Install this add-on.
. 2Copy it to the logon screen with the button in General Settings.
. 3When NVDA dies, press control alt delete, then activate the NVDA menu, Tools, Kill NVDA.
After that, press escape. NVDA restarts, but you should be able to use your computer again.""", "https://addons.nvda-project.org/files/get.php?file=killnvda"],
	"Time Zoner":["2019.2.1 +", """An add-on for NVDA to announce the time in selected timezones.
Introduction
For a very long time now, Windows has had the ability to show multiple clocks from different timezones. Users can customize the clocks and they become instantly visible.
Unfortunately, for users of screen readers such as NVDA or JAWS, there is no simple way to get this information. These screen readers don't support additional clocks, so blind computer users have to resort to other, third-party solutions, some of which are paid.
A lot of the work I do involves working across timezones, and eventually I got tired of manually converting times in my head, especially for timezones that aren't aligned to the hour (such as India which is +5:30 UTC).
For these reasons, I've created this add-on for NVDA. The add-on lets you hear times in selected timezones through the use of the timezone ring.
Usage
The add-on supports both the legacy and the Python 3 version of NVDA.
Once the add-on is installed, press NVDA+N to bring up NVDA's context menu. Arrow down to "Preferences" and then up to "Time Zoner".
Press ENTER on "Configure timezone ring".
You will be presented with a dialog to set the timezones for which you want the time and date announced.
Select items in the timezone list to add them to your timezone ring. Deselect (or press the Remove button) to delete them from the ring.
You can also reorder the timezones in the ring by using the Move Up and Move Down buttons.
Use the "Filter" box to search for specific timezones.
Check the "Announce abbreviated timezones" box to hear abbreviated timezone names such as IST or GMT. Uncheck the box to hear the full timezone names such as Asia/Kolkata or Europe/London.
When you are finished configuring the timezones, press the Save button.
From here on, you can press NVDA+Alt+T to announce times and dates in your timezone ring.
When you first install the add-on, NVDA will default to your local timezone if it can get it.
Change Log
Version 1.03, released on 03/21/2020
• The add-on no longer crashes if the default timezone can't be set.
• Fixed an issue with relative links in the documentation.
Version 1.02, released on 03/18/2020
• When installing a new version of this add-on, the settings from a previous installation are no longer lost.
• Other changes to conform to NVDA add-on standard compliance.
Version 1.01, released on 03/12/2020
• The time and date are announced in the user's locale, meaning that 24-hour time is honored if set.
• NVDA will announce either the abbreviated or full timezone depending on the user's setting in the Timezone Ring dialog. For example, it will either say Europe/London, or it will say GMT or BST. This setting is controlled by checking or unchecking the "Announce abbreviated timezones" checkbox.
• Add-on includes translator comments (@ruifontes).
• Add-on now includes header comments (@ruifontes).
• The Escape key closes the Timezone Ring dialog (@ruifontes).
• The menu item to open the Timezone Ring dialog is now named appropriately (@ruifontes).
• NVDA now defaults to the local timezone on installation of this add-on, if the local timezone is available.
• Support for multiple timezones through the use of a timezone ring.
• This add-on now uses the key NVDA+Alt+T to prevent conflict with the Clock add-on.
• The timezone selector dialog now has a filter box. NVDA will announce the number of results as the user starts typing into the filter field.
• Python 2 support
• The date and time is now announced in a separate thread to prevent hanging the NVDA thread in case retrieval takes a little while.
• The timezone selector dialog now has a Cancel button and no longer prevents NVDA from shutting down.""", "https://addons.nvda-project.org/files/get.php?file=tz"],
	"Tony's enhancements":["2019.3", """This add-on contains a number of small improvements to NVDA screen reader, each of them too small to deserve a separate add-on.
This add-on is only compatible with NVDA versions 2019.3 and above.
Enhanced table navigation commands
• Control+Alt+Home/End - jump to the first/last column in the table.
• Control+Alt+PageUp/PageDown - jump to the first/last row in the table.
• NVDA+Control+digit - jump to 1st/2nd/3rd/... 10th column in the table.
• NVDA+Alt+digit - jump to 1st/2nd/3rd/... 10th row in the table.
• NVDA+Shift+DownArrow - read current column in the table starting from current cell down.
Dynamic keystrokes
You can assign certain keystrokes to be dynamic. After issuing such a keystroke, NVDA will be checking currently focused window for any updates and if the line is updated, NVDA will speak it automatically. For example, certain keystrokes in text editors should be marked dynamic, such as Jump to bookmark, jump to another line and debugging keystrokes,such as step into/step over.
The format of dynamic keystrokes table is simple: every line contains a rule in the following format:

appName keystroke
where appName is the name of the application where this keystroke is marked dynamic (or * to b marked dynamic in all applications), andkeystroke is a keystroke in NVDA format, for example, control+alt+shift+pagedown.
Real-time console output
This option is disabled by default and must be enabled in the settings.
This option makes NVDA to speak new lines immediately as they appear in console output, instead of queueing new speech utterances.
There is also an option to beep on command line updates - this would give you a better idea when new lines are printed in the console.
Beep when NVDA is busy
Check this option for NVDA to provide audio feedback when NVDA is busy. NVDA being busy does not necessarily indicate a problem with NVDA, but rather this is a signal to the user that any NVDA commands will not be processed immediately.
NVDA volume
• NVDA+Control+PageUp/PageDown - adjust NVDA volume.
This option controls the volume of NVDA speech as well as all the other sounds and beeps produced by NVDA. The advantage of this option compared to adjusting volume of a speech synthesizer, is that it affects the volume of all the beeps proportionally.
Blocking double insert keystroke
In NVDA pressing Insert key twice in a row toggles insert mode in applications. However, sometimes it happens accidentally and it triggers insert mode. Since this is a special keystroke, it cannot be disabled in the settings. This add-on provides a way to block this keyboard shortcut. When double insert is blocked, insert mode can stil be toggled by pressing NVDA+F2 and then Insert.
This option is disabled by default and must be enabled in the settings.""", "https://addons.nvda-project.org/files/get.php?file=tony"],
	"Phonetic Punctuation":["2019.3", """Phonetic punctuation is an NVDA add-on that allows to convert punctuation signs into audio icons. In general, it can also convert any regular expressions into audio icons.
Demo
You can listen to a sample speech output with phonetic punctuation here (10 seconds audio): https://soundcloud.com/user-977282820/nvda-phonetic-punctuation-demo
Usage
. 1Make sure that your symbol level is set to appropriate value. If you're not sure, then press NVDA+P several times until you select "Symbol level all".
. 2Make sure phonetic punctuation is enabled. Press NVDA+Alt+P to enable.
. 3Phonetic punctuation rules can be configured via a dialog box in NVDA preferences menu.
. 4Phonetic punctuation comes with a set of predefined audio rules. However, only a few of them are enabled by default. You can enable other rules, as well as add new rules in the configuration dialog.
. 5Audio rules are saved in a file called phoneticPunctuationRules.json in NVDA user configuration directory.
Supported voice synthesizers
Phonetic punctuation depends on new NVDA speech framework, and as of today (October 2019), not all voice synthesizers have proper support for the new commands. This means that phonetic punctuation might not work correctly with some voice synthesizers.
Synthesizers known to work well with Phonetic Punctuation:
• Microsoft Speech API
• eSpeak
• Windows OneCore Voices
Synthesizers known to have problems with PhoneticPunctuation:
• IBMTTS: see this issue.
• RHVoice: Break command is not supported.""", "https://addons.nvda-project.org/files/get.php?file=phoneticpunc"],
	"Percentage Checker":["2019.2 / 2019.3", """This add-on allows you to check how far - in percents - you are in the text or on a list. This information can be given either by spoken message, or by a beep. In addition you can jump to the given percentage or a line number in the text.
Key Commands:
• Shift+NVDA+j: Displays a dialog allowing you to jump to the given line number.
• Shift+NVDA+p: Announces percentage in the current text or on a list. In addition if you are in a text the amount of words in the field would be spoken. In case of a list this would be amount of all list items.
• Alt+NVDA+p: Presents your position in a text or on a list as a beep.
The two last commands can be pressed twice in quick succession to display a dialog allowing you to jump to a given percentage in a text. All these commands can be remapped from the input gestures dialog.""", "https://addons.nvda-project.org/files/get.php?file=perChk"],
	"Report Passwords":["2019.3 +", """This add-on adds the option of speaking the text typed in protected controls like passwords, such as when logging into web-based email sites, where typed characters are spoken as asterisks.
Note: NVDA has an option to configure if typed passwords will be spoken in Windows terminals. This add-on won't affect those kinds of controls.
How to configure
The add-on can be configured from its category in the NVDA's settings dialog, under NVDA's menu, Preferences submenu. A gesture for opening the add-on settings panel can be assigned from Input gestures dialog, configuration category.
Tip: If you have not configured NVDA to speak typed characters or words but want to hear typed text in passwords, you may create a configuration profile to enable the speaking of typed characters and passwords, and assign it to a gesture or create a trigger to enable it automatically in certain situations. For convenience, NVDA will ask if you want to create a dedicated profile when the add-on is installed.""", "http://addons.nvda-project.org/files/get.php?file=rp"],
	"Audio Themes":["unknown", """This add-on creates a virtual audio display that plays sounds when focusing or navigating objects (such as buttons, links etc...) the audio will be played in a location that corresponds to the object's location in the visual display.
The add-on also enables you to activate, install, remove, edit, create, and distribute audio theme packages.
Usage
This add-on enables you to perform three distinct tasks, including managing your installed audio themes, editing the currently active audio theme, and creating a new audio theme.
You can access these functions from the add-on's menu which is found in the main NVDA menu.
Managing Your Audio Themes
• The 'Manage Audio Themes' dialogue enables you to activate or deactivate audio themes, in addition to installing and removing audio themes.
• In this dialogue there are some additional options including:
• Play sounds in 3D mode: When you uncheck this box the add-on will play the sounds in mono mode (always in the centre of the audio display) regardless of the object location.
• Speak role such as button, edit box , link etc.: When you uncheck this box NVDA will start announcing the role when focusing objects rather than ignoring it (which is the default behaviour when installing this add-on).
• Use Synthesizer Volume: Checking this box will set the sound player of this add-on to use the active voice sound, thus making all audible output the same as the voice volume when ever you change that volume.
• Audio Theme Volume Slider: Alternatively you can set the volume for the add-on using this slider. Setting it to 0 will mute all sounds, and 100 is the maximum volume.
Editing The Active Audio Theme:
• When you click on the 'Edit the active audio theme' option, a dialogue will open with a list containing all the sounds contained in the currently active theme. From this dialogue you can:
• Change Selected: Selecting a sound from the list and clicking this button, will open a standard open file dialogue, select an ogg or wave audio file from your file system to replace the selected sound, and click OK to complete the process.
• Remove Selected: This will remove the selected sound from the theme, click 'Yes' to confirm the removal process, and the selected sound will be removed.
• Add New Sound: When clicking this button a new dialogue will be shown. From the first combo box in the newly opened dialogue select the object type you want to assign the sound to it, for example (button, link, tab, menu and so on), then click the 'Browse to an audio file' button to select the sound you want to assign for the previously selected object type. Optionally you can click the preview button to preview the sound, and finally clicking the OK button will apply the changes and assign the selected sound to the selected object.
• Close: Will exit the dialogue without performing any action.
Creating A New Audio Theme
• If you have a good sound production skills you can apply them here and create an audio theme of your own, rather than editing an existing one. To do this you can follow these steps. - Collect your audio files in one place, they must be in ogg or wave format, and rename them to what ever make sense to you. For example when I was creating the default audio theme for this add-on, I grouped sounds according to interaction patterns, for example, the combo box, the drop down button, and the split button can all have the same sound, while the Check box, The toggle button, and the menu check item can have the same sound. - From the add-on menu click 'Create a new audio theme' - A dialogue will be opened asking you for some information about your new audio theme, including: * Theme Name : The name of your theme which will be shown in the audio themes manager. This must be a valid windows folder name. * Your Name: Enter your real name or a nick name.
• Theme description : A Brief description about your audio theme. - Click OK to move to the next step. - In the next step a dialogue similar to the 'Audio Themes Editor' will be shown, and from their the process is the same as the Theme editing process, so refer to 'Editing The Active Audio Theme' section.
Copyright:
Copyright (c) 2014-2016 Musharraf Omer and Others
Although this add-on was started as an independent project, it evolved to be an enhanced version of the 'Unspoken' add-on by Austin Hicks and Bryan Smart. The majority of this add-on's development went into creating the tools to manage, edit and create audio theme packages. So a big thank you to them for creating such a wonderful add-on, and making it available for us to build on top of their work.
A Note on Third-party audio files:
The Default audio theme package in this add-on uses sounds from several sources, here is a breakdown for them: - Unspoken 3D Audio: An add-on for NVDA - TWBlue: A free and open source twitter client - Mushy TalkBack: An alternative talkback with better sounds.""", "https://addons.nvda-project.org/files/get.php?file=ath"],
	"Synth ring settings selector":["2019.2", """This add-on allows the user to select which settings should appear on the synth settings ring.
Features
This add-on provides the following features:
• A category panel in the NVDA settings to select which settings you want to include in the synth settings ring.
• save specific settings for each profile.
• overrides the default synth driver settings that are shown in the synth settings ring.
Requirements
You need NVDA 2019.2 or later.
Installation
Just install it as a NVDA add-on.
Usage
To enable or disable which settings are included, go to NVDA settings and select "Synth ring settings selector" category. In that category you can configure all supported features by this add-on. Settings included by default:
• language.
• voice.
• variant.
• rate.
• rate boost.
• volume.
• pitch.
• inflection.
Note: This dialog shows the supported settings by the current synthesizer only. Settings not present here aren't modified in the add-on config.""", "https://addons.nvda-project.org/files/get.php?file=synthrings"],
	"Debug Helper":["unknown", """The purpose of this add-on is to make debugging things in NVDA easier. New features will be added based on user suggestions. All emails or GitHub issues with feedback or feature ideas are most welcome.
Key Command
• NVDA+Shift+F1: Inserts a mark line in the NVDA log.
Explanation and Usage
When you press the command key, the add-on inserts a line like the following in the NVDA log (at the Info level):
-- Mark 1 --
It will also announce: "Logged Mark 1!"
If you press the key again, you will get:
-- Mark 2 --
and "Logged Mark 2!" will be spoken.
Let us say for example that you were about to perform a series of tasks, that you know generate lengthy error content in the NVDA log. You are going to post the relevant portions of your log to a mailing list or the NVDA GitHub issue tracker. However you don't want to hunt through your entire log to find the relevant content. So you use this add-on to insert mark 1, right before you do the thing that causes the first error. If you know something else will generate further errors, or a different kind, you insert another mark to separate that error from the previous one, or so you can say "this is what I was doing at mark 3, where some errors occurred." Another example: While using some application, something happens that causes an error (maybe you hear the Windows error sound). You want to go back and find that error later, but you don't want to stop working and save the log right now. So you use this add-on again, to insert a mark in your log. This time the mark will appear after the errors in your log, instead of before. But either way, the marks will help you narrow down the important sections of your log.
The mark lines shown above can be easily searched for with the find command in a text editor such as Notepad or Notepad++. Additionally, by default, there is a blank line inserted above each mark. Blank lines are also possible after the mark. Blank lines can be helpful if you are using NVDA's log viewer, or another text editor, and want to use the arrow keys to quickly read up/down through the log, to find a particular mark. It is easy to pick the word "blank" out of a bunch of text being spoken as you quickly move through the log. If you arrow really fast, you might need more than one blank line, which you can adjust in settings.
Note: The mark count will survive the reloading of plugins (NVDA+Control+F3), but will start back at one if you restart NVDA.
Configuration:
In the Settings section of NVDA Preferences, you will find a "Debug Helper" category. In the settings dialog you can change the number of blank lines inserted before and after each mark line. The default is one line before, and zero after, although you can use 0 through 10 lines for either. Under the Tools category of NVDA's Input Gestures panel, you can change NVDA+Shift+F1 to a key sequence of your choice.
Changelog
• 
Version 1.0.2 (2019-08-28)
• Translation and code cleanup.
• 
Version 1.0.1 (2019-08-26)
• Minor bugfix version to probably fix an install problem on certain versions of Windows.
• 
Version 1.0 (2019-08-22)
• 
Initial release. Including following features:
• Ability to generate numbered mark lines in the log (at info level).
• Ability to add 0-10 blank lines before and after each mark line.
• Configuration via NVDA settings dialog system.""", "https://addons.nvda-project.org/files/get.php?file=debughelper"],
	"Notepad++":["unknown", """This addon improves the accessibility of the notepad++ text editor. To learn more, and to read the documentation before installation, https://github.com/derekriemer/nvda-notepadplusplus visit the addons github page https://github.com/derekriemer/nvda-notepadplusplus""", "https://files.derekriemer.com/NotepadPlusPlus-2019.09.0.nvda-addon"],
	"Beep Keyboard":["2018.2 to 2019.2", """This add-on allows the user to configure NVDA to beeps with some keyboard events.
Features
This add-on provides the following features you can use to adapt NVDA keyboard behavior:
• Beep for uppercases when caps lock is on: if this feature is enabled, NVDA will beep when you typing an uppercase and caps lock is on. Don't make any more uppercase mistakes!
• Beep for typed characters when shift is pressed: with this feature NVDA will beep if you type a character with shift key pressed.
• Beep for toggle keys changes: with this feature, NVDA will beep higher if a toggle key goes on, and lower tone if it goes off. Please note that Windows has a toggle keys beep function built-in on Ease of Access Center. This native feature works well if you don't use laptop keyboard layout setting.
• Announce toggle keys changes: just when "Beep for toggle keys changes" is on. You can enable or disable NVDA to announce toggle key status.
• Beep for specified characters: NVDA will beep for all characters that you set in advanced settings.
• Disable beeping on password fields: this feature is enabled by default to aboid security risks. Disable it if you want to hear beeps on password fields.
Requirements
You need NVDA 2018.2 or later.
Installation
Just install it as a NVDA add-on.
Usage
To enable or disable features, go to NVDA settings and select beep keyboard category. In that category you can configure all supported features by this add-on.
• "Beep for uppercases when caps lock is on" is enabled by default.
If you need more settings, open the advanced settings dialog that contains the following options:
• Ignored characters with shift pressed: all characters here will be ignored to beeping when shift is pressed. Escape Sequences are allowed, e.g. "\t" for tab, "\r" for carriage return.
• Beep always for the following characters: set here all characters that you want NVDA beeps for. Escape Sequences are allowed, e.g. "\t" for tab, "\r" for carriage return.
• Select tone to configure: you can configure parameters for all tones. Select one here, and set the parameters in the next text boxes. When change selection, NVDA will beep for the current selected tone with the current parameters set in the dialog.
• Tone pitch: tone pitch for the current selected tone.
• Tone length: tone length for the current selected tone.
• Tone volume: tone volume for the current selected tone.
• Test tone: this button lets you to play a test with the current set parameters.
• Press OK button to save settings or cancel to discard.""", "https://addons.nvda-project.org/files/get.php?file=beepkeyboard"],
	"Developer Toolkit":["2019.1 / 2020.1", """Developer toolkit (DTK) is an NVDA add-on that helps blind and visually impaired developers independently create visually appealing user interfaces and web content. It provides gestures that enable you to navigate through objects and obtain information about them, such as their size, position, and characteristics. To begin using DTK, place focus on a control, then press ALT+WINDOWS+K. To disable it, press ALT+WINDOWS+K again. When on the web, press NVDA+SPACE to put NVDA in Focus Mode and press NVDA+SHIFT+SPACE to disable Single Letter Navigation.
Gestures
The following gestures are available when DTK is enabled.
• ALT+WINDOWS+K - Enable or disable DTK features.
• LEFT ARROW - Move to previous sibling.
• RIGHT ARROW - Move to next sibling.
• UP ARROW - Move to parent.
• DOWN ARROW - Move to first child.
• CTRL+HOME - Move to top-most parent.
• HOME - Move to the relative parent if one is assigned.
• A - In web content, speak HTML attributes. Press twice quickly to copy to the clipboard.
• B - Speak the position of the object's bottom edge. Press twice quickly to copy to the clipboard.
• SHIFT+B - Speak the distance between the object's bottom edge and the relative parent's bottom edge. Press twice quickly to copy to the clipboard.
• C - Speak the number of children contained inside the object. Press twice quickly to copy to the clipboard.
• control+c - Switch between RGB, Hex, and Name color values.
• CTRL+D - Enable or disable detailed messages.
• F - In web content, speaks the object's font and formatting information. Press twice quickly to copy to the clipboard.
• H - Speak the object's height. Press twice quickly to copy to the clipboard.
• L - Speak the position of the object's left edge. Press twice quickly to copy to the clipboard.
• n - Speak the object's name. Press twice quickly to copy to the clipboard.
• CTRL+P - Set the relative parent for obtaining size/location of objects.
• P - Speak the relative parent's name. Press twice quickly to copy to the clipboard.
• R - Speak the position of the object's right edge. Press twice quickly to copy to the clipboard.
• SHIFT+R - Speak the distance between the object's right edge and the relative parent's right edge. Press twice quickly to copy to the clipboard.
• ALT+R - Speak the object's Role/control type. Press twice quickly to copy it to the clipboard.
• S - Speak the number of siblings relative to the object. Press twice quickly to copy to the clipboard.
• SHIFT+S - Speak the object's control states. Press twice quickly to copy it to the clipboard.
• T - Speak the position of the object's top edge. Press twice quickly to copy to the clipboard.
• V - Speak Developer toolkit version. Press twice quickly to copy to the clipboard.
• W - Speak the object's width. Press twice quickly to copy to the clipboard.
Notes
• When using home or any modified version of the home key, using the numpad home key fails because NVDA will send the numpad7 keypress instead of a numpadHome keypress. Other keyboard add-ons that attempt to reassign numpad7 to the home key will fail in this add-on.
• 
When using the relative parent feature, DTK will set the relative parent to the desktop under the following conditions.
• The focused object and the relative parent are the same.
• The relative parent is not a direct ancestor of the focused object.
• 
DTK cannot access information such as CSS rules, padding, borders, or z-index. Doing so requires accessing them outside of the NVDA context, which presents a security concern for users.
Known issues
• The customizable list of font attributes found in Developer toolkit settings may be cumbersome to use. This is a limitation found in NVDA's user interface library.""", "https://addons.nvda-project.org/files/get.php?file=devtoolkit"],
	"Add-ons documentation":["2017.3 / 2019.2", """This add-on provides a quick way to access documentation for the add-ons you have installed. It creates, in the NVDA Help menu, two sub-menus. One, called "Running add-ons documentation", groups the documentation for each add-on and make available a list of commands for all running add-ons, with a table for each add-on. Other sub-menu called "Disabled add-ons documentation", lists the disabled add-ons, giving access to its documentation. Please, remember that the Synth and Braille drivers add-ons will not appear in any of the above categories. Note that you also can access the add-ons documentation through the Add-ons manager in NVDA, Tools menu. Here you have also the information about the state of an add-on. Also remember that you can access the NVDA and add-ons commands in the Input gestures dialog. However, in this dialog the add-ons commands are not grouped and you can not find a command containing "windows", by instance...""", "https://addons.nvda-project.org/files/get.php?file=addonshelp"],
	"Character Information":["2017.3 / 2021.1", """This add-on allows to present in a message character information such as unicode name, number, category, etc.
Commands
• Numpad2 (all keyboard layouts) or NVDA+. (laptop layout): when pressed 4 times, displays information about the character of the current navigator object where the review cursor is situated.
Notes
• 
This add-on provides also two gestures that are unassigned by default:
• A script to display directly the review cursor character information. If you feel unconfortable with the four press gesture, you may assign to it a gesture in NVDA's input gesture dialog ("Text review" category).
• A script to display character information for the character at the position of the caret (works only in places where there is a caret). It can be found in the "system caret" category of NVDA input gestures dialog.
• 
The provided information is in english since it is part of Unicode norm. If a local translation exists for this add-on, the information is also provided alongside with english.
• The CLDR name (Unicode Common Locale Data Repository) is only supported with NVDA 2019.1 and above.
• For the characters written with Microsoft proprietary fonts Symbol, Wingding (1, 2,, 3) and Webding, some additional information is provided: character name, font name and information of the corresponding unicode character.""", "https://addons.nvda-project.org/files/get.php?file=chari"],
	"Addon to count elements of selected text":["2017.2 / 2019.1", """This addon announces the number of words, characters, paragraphs and lines of the selected text by pressing Control+Shift+F12.
Note: In some applications, like Word, WordPad and DSpeech, it only announces word and characters, to avoid hanging NVDA.
In any text editor, or in a virtual document, for example in a web browser, PDF, email body, etc., select the desired text using the usual text selection commands and press Control+Shift+F12.
This command can be modified in the "Input gestures" dialog in the "Text editing" section.""", "https://addons.nvda-project.org/files/get.php?file=wc"],
	"Online image describer":["2018.3 / 2020.2", """This addon aims at adding online image recognition engines to NVDA.
There are two types of engines. OCR and image describer.
OCR extract text from image.
Image describer describe visual features in image in text form, such as general description, color type landmarks and so on.
Internet connection is required to use this addon, since image describe services are provided by API endpoints on the Internet.
They are called engines in this addon.
There are three types of engine for this addon.
• Online OCR engine
• Online image describer engine
• Windows 10 OCR engine (offline)
You also need to choose the source of recognition image.
• Current navigator object
• Current foreground window
• The whole screen
• Image data or file from clipboard
• Image file pathname or image url from clipboard
Keyboard commands
After choosing these types, you can start recognition with one gesture.
NVDA+Alt+P Perform recognize according to source and engine type setting, Then read result. If pressed twice, open a virtual result document.
There are four additional gestures left unassigned. Please assign them before using.
Cycle through different recognition engine types.
Cycle through different recognition source types.
Cancel current recognition
This gesture can be useful if you think you have waited for too long and want to cancel.
Also sometimes you do not want to be disturbed by recognition message because you need to review some messages arrived after recognition start.
Show previous result in a virtual result document.
Though there is a feature to copy result to clipboard. Character position information cannot be preserved, so this gesture is added to solve this problem.
There are also four old gestures are left unassigned for users who prefer gestures in previous versions.
It is recommended to use new gesture and switch engine type according to your need.
Recognize current navigator object with online OCR engine Then read result. If pressed twice, open a virtual result document.
Recognizes image in clipboard with online OCR engine. Then read result. If pressed twice, open a virtual result document.
Recognize current navigator object Then read result. If pressed twice, open a virtual result document.
Recognizes image in clipboard . Then read result. If pressed twice, open a virtual result document.
Engine Configuration
You can choose recognition engines and configure them in detail in Online Image Describer category in NVDA settings dialog.
The author of addon have registered account with free API quota and set up a proxy server on www.nvdacn.com to make this addon easier to test at first. Test quota is limited and may be cancelled by API provider anytime.
It is highly recommended to register your own key according to guide in each engine.
The following settings are applicable to all engines.
• Copy recognition result to the clipboard: if enabled, recognition result text will be copied to clipboard after recognition.
• Use browseable message for text result: if enabled, recognition result text will be shown in a popup window instead of speech or braille message.
• Swap the effect of repeated gesture with none repeated ones: by default, a virtual result document is shown only if you press the corresponding gesture twice, if you use that frequently you can enable this option so that you only need to press once to get a result viewer.
• Enable more verbose logging for debug purposes: some logs are essential for debugging but affects performance and takes up a lot of space. Only turn this on if specifically instructed to by the addon author or an NVDA developer.
• Proxy type: which type of proxy you are using. If you do not know what a proxy is just leave it as is.
• Proxy address: full URL of your proxy. If you do not know what a proxy is just leave it as is. If you choose to use proxy your proxy will be verified before saving , after verification, there will be a prompt to tell you result.
The following settings means the same in all engines, describe them here to save space.
• 
API Access Type: this controls how you get access to the corresponding API endpoints.
• If you choose "Use public quota", you are using free quota in an account registered by addon author.
• If you choose "Use your own API key", this addon will use quota from your own account.
• 
APP ID, API key or API Secret Key: if you want to use quota from your own account corresponding access tokens is required. Some engines only need API key. Some engines require two tokens. These are only valid if you choose "use your own API key" in API Access type.
Note that the quality and accuracy of results are affected by many factors.
• Models and techniques used by engine provider
• Quality of uploaded image
• Is navigator object hidden behind something else
• Screen resolution
Online image description
Here are three engines available.
Microsoft Azure Image Analyser
This engine extracts a rich set of visual features based on the image content.
This engine is english only. If you want description in other languages, you can use Microsoft Azure Image Describer
Visual Features include:
• Adult - detects if the image is pornographic in nature (depicts nudity or a sex act). Sexually suggestive content is also detected.
• Brands - detects various brands within an image, including the approximate location. The Brands argument is only available in English.
• Categories - categorizes image content according to a taxonomy defined in documentation.
• Color - determines the accent color, dominant color, and whether an image is black&white.
• Description - describes the image content with a complete sentence in supported languages.
• Faces - detects if faces are present. If present, generate coordinates, gender and age.
• ImageType - detects if image is clip art or a line drawing.
• Objects - detects various objects within an image, including the approximate location. The Objects argument is only available in English.
• Tags - tags the image with a detailed list of words related to the image content.
Some features also provide additional details:
• Celebrities - identifies celebrities if detected in the image.
• Landmarks - identifies landmarks if detected in the image.
Microsoft Azure Image describer
This engine generates a description of an image in human readable language with complete sentences. The description is based on a collection of content tags, which are also returned by the operation.
More than one description can be generated for each image. Descriptions are ordered by their confidence score.
There are two settings for this engine.
• Language: the language in which the service will return a description of the image. English by default.
• Maximum Candidates: maximum number of candidate descriptions to be returned. The default is 1.
Online OCR
Online engines rely on the use and presence of the following services.
https://www.nvdacn.com
https://ocr.space/ocrapi
https://azure.microsoft.com/en-us/services/cognitive-services/
http://ai.qq.com
http://ai.baidu.com
http://ai.sogou.com/
https://intl.cloud.tencent.com
Engines
There are five engines available.
Tencent Cloud OCR
This API is sponsored by Tencent Cloud and Aceessibility Research Association, with a quota of 15000 per day.
This engine support 19 languages.
• Chinese-English mix
• Japanese
• Korean
• Spanish
• French
• German
• Portuguese
• Vietnamese
• Malay
• Russian
• Italian
• Dutch
• Swedish
• Finnish
• Danish
• Norwegian
• Hungarian
• Thai
• Latin
Here is the settings of this engine.
• Language: Text language for recognition. Auto detection by default.
OCR space
This one is a paid API with free quota provided by OCR Space
It supports 24 languages
• Arabic
• Bulgarian
• Chinese(Simplified)
• Chinese(Traditional)
• Croatian
• Czech
• Danish
• Dutch
• English
• Finnish
• French
• German
• Greek
• Hungarian
• Korean
• Italian
• Japanese
• Polish
• Portuguese
• Russian
• Slovenian
• Spanish
• Swedish
• Turkish
Here are settings for this engine:
• Language: text language for recognition. English by default.
• Detect image orientation: if set to true, the API autorotates the image correctly.
• Scale image for better quality: if set to true, the API does some internal upscaling. This can improve the OCR result significantly, especially for low-resolution PDF scans.
• Optimize for table recognition: if set to true, the OCR logic makes sure that the parsed text result is always returned line by line. This switch is recommended for table OCR, receipt OCR, invoice processing and all other type of input documents that have a table like structure.
If you want to use your own key, you also need to specify API Key.
You can get your own free API key by registering onOCR space
Here is a simple guide.
Find the link "Register for free API key"
Click on it and you will find a form to fill in.
The form asks you to enter the following data
• Email Address
• First Name
• Last Name
• How do you plan to use the OCR API?
After filling it and submit. You may also need to pass a captcha
Then you will receive a confirmation e-mail
Find the link named "Yes, subscribe me to this list." in that e-mail. Access that link and you will receive API key by e-mail soon.
Microsoft Azure OCR
This engine uses OCR API in Microsoft Azure Cognitive Services Computer Vision.
It supports 24 languages including
• Chinese Simplified
• Chinese Traditional
• Czech
• Danish
• Dutch
• English
• Finnish
• French
• German
• Greek
• Hungarian
• Italian
• Japanese
• Korean
• Norwegian
• Polish
• Portuguese
• Russian
• Spanish
• Swedish
• Turkish
• Arabic
• Romanian
• Serbian Cyrillic
• Serbian Latin
• Slovak
Here are settings for this engine:
• Language: text language for recognition. Auto detection by default.
• Detect image orientation: if set to true, the API autorotates the image correctly.
If you use your own key, you should get a subscription key for using Microsoft Computer Vision API from the link below:
Step 1: Create an account on Azure website
Please note that the key must be created for the Computer Vision API. The first "GET API key" button you encounter with single key navigation. Currently Microsoft provides the option to create a trial key for 7 days. You can also sign up for a free azure account for more trail. Signing up requires a credit card. If you already have a subscription account, you can skip this step.
Step 2: Deploy Cognitive Services
Now you have an azure account.
First login on Azure Portal
Wait until you get the message Portal is Ready you are logged into azure portal.
Find the link called All resources after All services button and activate it.
Wait until you get the message Blade All resources are ready , your focus will be an edit box, then press shift tab find a menu item called add and activate it.
Wait until you get the message Search the Marketplace, type Cognitive Services and press down arrow.
Wait until you get the message List of options Cognitive Services one of five, then press enter.
Wait until you get the message Blade Cognitive Services is ready press tab or b to find a button named Create activate it.
Wait until you get the message Blade Create is ready, your focus will be an edit box, type a name for this resource. Note that Your resource name can only include alphanumeric characters, '', '-', and can't end with '' or '-'.
I choose NVDA_OCR.
Press tab to go to Subscription combo box. Usually you can leave it as is.
Press tab to go to Location combo box. Choose one close to your current location.
Be sure to remember this since location is required in engine configuration.
Press tab to go to Pricing tie combo box. Usually a free tie like F0 is adequate. If that is not enough you can choose other tier after reading full pricing details in View full pricing details link.
Press tab to go to Create new Resource group edit box. You should create one if you do not have any Resource group. Press tab find Create new button.
Then press tab go to Create Button to create this resource.
Wait until you get the message Deployment succeeded.
Then find Go to resource button sometimes you need go up to activate Notifications button before you can find Go to resource button.
Wait until you get the message Blade Quick Start is busy.
Find the link named keys, then activate it.
Wait until you get the message Blade Manage keys is ready.
Find edit box named key 1 or key 2. The content of that edit box is the API key required in engine configuration. Press Ctrl-C to copy it for engine configuration
Then you can fill in these two settings required if you use your own API key.
• Azure resource Region: the region you choose when deploying Cognitive Services in Azure Portal.
• API key: the key you get after successfully deploying Cognitive Services in Azure Portal, KEY 2 is recommended.
Baidu OCR
This one is also a paid API with free quota provided by Baidu.
Baidu OCR supports 10 languages including
• Chinese and English mixture
• English
• Portuguese
• French
• German
• Italian
• Spanish
• Russian
• Japanese
• Korean
This engine can also get position of every character
Here are its settings:
• 
Get position of every character allows you to do more precise operation on some inaccessible application. Enabling this will make recognition slightly slower.
• 
Use Accurate API: if is enabled will use a different endpoint. That accurate endpoint takes longer time but has higher quality and (If you use your own API key its price is also higher).
It has four endpoints with separate quota limit.
• Basic OCR without any information about text location. Currently 50000 times a day.
• Basic OCR with information about text location. Currently 500 times a day.
• Accurate OCR without any information about text location. Currently 500 times a day.
• Accurate with information about text location. Currently 50 times a day.
If you press the gesture which only read result, you are using endpoints without any information about text location.
If you press the gesture which shows an result viewer, you are using endpoints with information about text location.
Though it provides a quite generous free quota, its website is Chinese only and not quite accessible.
Tencent AI OCR
This API is free to use with frequency limit about two query per second.
If you want to bypass the limit you can register your own API key. The website of this API is Chinese only and not quite accessible.
There is no information about language support in the document. According to my test Chinese and English and their mixture is supported.
There is no additional configuration for this API.""", "https://addons.nvda-project.org/files/get.php?file=oid-dev"],
	"Weather Plus":["2017.3 to beyond", """• This plugin adds local temperature and forecasts to 24 hours up to 2 additional days and hourlyforecast for NVDA.
• Copyright (C) Adriano Barbieri
• Released under the GNU GPL (General Public License) v2
• Weather Plus works through the use and presence of the following services:
• https://www.weatherapi.com/
• http://www.geonames.org/
• http://veloroutes.org/elevation/
• http://www.nvda.it/
USAGE:
• Press NVDA+w to get the information about current temperature and weather conditions.
• Press NVDA+shift+W to get 24 hours forecast and forecast up to 2 days.
• Press NVDA+shift+W twice to get hourlyforecast of temperature and atmospheric conditions.
• Press NVDA+shift+control+w to set a temporary city.
• Press NVDA+shift+control+alt+w to open the Weather Plus settings dialog.
• Press NVDA+alt+w to get the date and time, when the weather report was updated.
• Press control+shift+w to toggle between Fahrenheit, Celsius or Kelvin temperature scales.
Weather Plus setup:
• You must set the Weather Plus addon before its first use! Go to the Preferences submenu, Weather Plus Settings submenu and choose one of the following options:
• Set and Manage Your Cities... - Displays or allows to set the current city from a list.
• Set a temporary city... - Displays and allows to set one temporary city from a list if available.
• Documentation - Opens the help file for the current language.
• Check for Update... - Notifies about the availability of the new version.
To add a new city: press the following item:
• Set and Manage Your Cities... - Displays or allows to set the current city from a list.
• The following message is displayed only for the first time! Settings Preset None F1: help placing, F2: last TAB selection, F3: list and edit box, F4: control duration Weather Forecast, F5: volume controls.
• In the edit box, enter a City or choose one from the list, if available. Note: The F5 key is available if the sound effects are activated.
• After pressing enter on the item "Set and Manage Your Cities...", you will find other buttons as follows:
• Test - Test the validity of the city and find the data of it.
• Add - Adds the current city into your list. This button can be activated if you select a city from the list, when the city entered passed the test.
• Details - Displays information about the current city. This button is activated if you select a city from the list, or it has passed the test.
• Define - Allows you to define the area, in order to adapt the sound effects. This button can be activated if the audio effects are installed and activated, and you select a city from the list.
• Preset - Presets a city as the default, will be used every time you restart the plugin. This button is activated if you select a city previously inserted in the list and not preset, or it has passed the test.
• Remove - Deletes the current city from your list. This button can be activated if you select a city previously inserted in the list.
• Rename - Rename the current city. This button can be activated if you select a city previously inserted in the list.
• Import new cities... - This button allows you to import cities from the another list of cities with the extension *.zipcodes; you can select the city you want to import, by turning on the checkbox associated with it.
• Export your cities... - It allows you to save the cities in the specified file with the extension *.zipcodes. This button is activated if you have added and saved at least one city into the list.
• hourly forecast setting... - This button allows you to choose the contents of the hourly forecast report.
• Scale of temperature measurement: Use the radio button to select between Celsius (by default), Fahrenheit and Kelvin.
• Degrees shown as: Use the radio button to select between: Celsius - Fahrenheit - Kelvin (by default) C - F - K or Unspecified.
• Combo box: Weather Forecasts up to days: 1; you can choose between 1 to 3 (1 days by default)
• Combo box: API response language: English, en; you can choose the language of the weather conditions text.
• To perform the following actions, toggle the following checkboxes:
• Copy the weather report and weather forecast, including city details to clipboard; checkbox not checked (by default)
• Enable audio effects (only for the current weather conditions); this checkbox also allows you to manage the installation of sound effects; if the sound effects are installed and the checkbox is activated, the F5 key and the volume setting becomes available.
• There will also be available an additional checkbox: "Use only weather effects".
• You can change the overall volume or change the last heard sound effect and filter out the others sounds in your environment. Checkbox is not checked by default.
• Use only weather effects - This option is available if sound effects are enabled; if is enabled, allows to listen only weather effects such as rain, wind, thunder, etc., filtering out all environmental ones. (unchecked by default)
• Enable the reading of the hours in 24-hour format. - If this checkbox is unchecked, announces the time in 12-hour format for example, 12 AM - 12 PM. Checkbox is checked (by default)
• Enable help buttons in the settings window; checkbox checked (by default)
• Read wind information; checkbox not checked (by default). If this checkbox is enabled, you can also activate the following checkboxes:
• Add wind direction; indicates the provenance of the wind. Checkbox checked (by default)
• Add speed of the wind; indicates the speed in kilometers or miles per hour. Checkbox checked (by default)
• Add speed in meters per second of the wind; checkbox checked (by default)
• Add wind gust speed of the wind; checkbox checked (by default)
• Add perceived temperature; checkbox checked (by default)
• Read atmospherical information; checkbox not checked (by default). If enabled, you can also check the following checkboxes:
• Add humidity value; indicates the humidity in percent. Checkbox checked (by default)
• Add visibility value; indicate in kilometres or miles the distance visible. Checkbox checked (by default)
• Add atmospheric pressure value; indicates the atmospheric pressure in millibars or inches of mercury. If it's checked, enable an additional checkbox that allows you to indicate the pressure in millimeters of mercury. Checkbox checked (by default)
• Add status of barometric pressure; check box checked (by default)
• Add cloudiness value; check box checked (by default)
• Add precipitation value; check box checked (by default)
• Add ultraviolet radiation value; check box checked (by default)
• Read astronomical information; indicates the time of sunrise and sunset and the time of moonrise and moonset. Checkbox not checked (by default)
• Use the comma to separate decimals; if enabled, uses the comma as a decimal separator, otherwise, use the point. Checkbox not checked (by default)
• Check for upgrade; if is activated this alerts when there is an update of the addon. Checkbox checked (by default)
• Press the OK button to confirm the action or the Cancel button to cancel the action.
• If you have modified the cities list, by pressing "Cancel", you will be remembered and you can still save it. Note: your settings will be save in the file named:
• "Weather.ini": startup settings of Weather Plus.
• "Weather.volumes": custom audio volume levels, regardless of the overall volume.
• "Weather.zipcodes": list of cities with their zip code and definitions.
• "Weather.default": Your default city.
• "Weather_searchkey": search key saved.""", "https://addons.nvda-project.org/files/get.php?file=wetp"],
	"BrowserNav":["2018.1 / 2019.1", """BrowserNav addon for NVDA
This add-on provides NVDA users powerful navigation commands in browser mode. For example, with BrowserNav you can find vertically aligned paragraphs, that is paragraphs with the same horizontal offset. This can be used to read hierarchical trees of comments or malformed HTML tables. You can also find paragraphs written in the same font size or style. BrowserNav also provides new QuickNav commands: P for next paragraph and Y for next tab.
Usage in browsers
BrowserNav can be used to navigate by horizontal offset from the left edge of the screen, by font size, or by font style.
• When navigating by horizontal offset, you can easily find paragraphs that are vertically aligned on the page. IN particular, you can press NVDA+Alt+DownArrow or UpArrow to jump to the next or previous paragraph that has the same offset. For example, this can be useful when browsing hierarchical trees of comments (e.g. on reddit.com) to jump between first level comments and skipping all the higher level comments.
• When navigating by font size, you can easily find paragraphs written in the same font size, or smaller/greater font size.
• You can also navigate by font size with the constraint of same font style.
BrowserNav works in any browser supported by NVDA.
Keystrokes:
• NVDA+Alt+UpArrow or DownArrow: Jump to previous or next paragraph with the same horizontal offset or font size.
• NVDA+alt+LeftArrow: Jump to previous paragraph with lesser offset or greater font size.
• NVDA+Alt+RightArrow: Jump to next paragraph with greater offset or smaller font size.
• NVDA+O: Switch rotor setting between horizontal offset, font size, font size with font style.
• P or Shift+P: Jump to next or previous paragraph.
• Y or Shift+Y: Jump to next or previous tab.
Source code
Source code is available at https://github.com/mltony/nvda-browser-nav.""", "https://addons.nvda-project.org/files/get.php?file=browsernav"],
	"Outlook extended":["2018.3 and beyond", """This addon improves the use of Microsoft Outlook by vocalizing some commands and adding extra commands.
Commands
• Alt+1 to Alt+9, Alt+0, Alt+-, Alt+=: Reports the header field 1 to 12 in a message, calendar item or task window. If pressed twice, moves the focus to this field if possible. If pressed three times, copies its content to the clipboard.
• NVDA+shift+I (desktop layout) / NVDA+control+shift+I (laptop layout): Reports the information bar in a message, calendar item or task window. If pressed twice, moves the focus to it. If pressed three times, copies its content to the clipboard.
• NVDA+shift+A (desktop layout) / NVDA+control+shift+A (laptop layout): Reports the number and the names of attachments in a message window. If pressed twice, moves the focus to it.
• NVDA+shift+M (desktop layout) / NVDA+control+shift+M (laptop layout): Moves the focus to the message body.
• Control+Alt+Left and Control+Alt+Right: in the address book search result list, navigates between the fields of the currently selected line.
• Control+Q: in the message list, marks the selected message or group of messages as read.
• Control+U: in the message list, marks the selected message or group of messages as unread.
Notes
All the gestures can be modified in the NVDA command gestures dialog. You may want to modify them especially in the following situations:
• The default gestures to mark messages as read or unread are the ones for Outlook english version. If they differ from the ones of your Outlook local version, you will have to change them accordingly.
• The default gestures to read headers correspond to Alt combined with the keys of the first row of the alpha-numeric keyboard. You may need to re-map the gestures tor read header 11 and 12 if they do not match your local keyboard layout.""", "https://addons.nvda-project.org/files/get.php?file=outlookextended"],
	"Training Keyboard commands":["unknown", """This addon is aimed to train NVDA commands in a game like way, for either keyboard layout modes desktop or laptop layout.
All commands data is scraped from keyCommands.html file in locale documentation folder in NVDA.
This addon does not have any default gesture or shortcut.
You have to assign a specific gesture to it via: NVDA menu>preferences>inputGestures>trainingKeyboardCommands.
Usage
• You choose the keyboard layout mode you want to train, and begin play
• A question or command and it's description will be displayed, and you have to pick the right related keys or answer
• If you have chose the right answer, your score wi be added one point
• If the answer was wrong, the score will not change, and go on with no loose
• At any time, if you want to exit, you will be asked if you want to save the remaining questions for next round
• If in a later time you choose a layout wit saved questions, you will be asked if you want to resume the remaining questions from previous round
• Answering all questions, about 95 for each layout, you will be declared a winner deserving NVDA addon's cup.""", "https://addons.nvda-project.org/files/get.php?file=trainingkbdcmd"],
	"Columns Review":["2017.3 and beyond", """Columns Review is an add-on to enhance NVDA experience with lists.
Its features include:
• customizable actions on column header and/or content (available actions are read, copy, spell and show in browse mode);
• ability to cycle between columns in ten-by-ten intervals;
• simplified header management (mouse clicks);
• on-demand reading of relative current item position (i.e.: item 7 of 10);
• customizable gestures with or without numpad;
• "0 items" announcement when list is empty (not working in Win8/10 folders, unfortunately);
• say all support;
• report of selected items (amount and item names);
• list search (with item multiselection, if checked/supported).
Gestures
Default keys for columns, headers and position are NVDA+control, but you can customize them from add-on settings (not "Input gestures" dialog!).
Note that your keyboard could have problems processing some key combinations, so try all add-on gestures and adjust them for better results.
See also add-on preferences for numpad mode, keyboard layout (without numpad), and the four available actions for columns.
• NVDA+control+digits from 1 to 0 (keyboard mode) or from 1 to 9 (numpad mode): by default, read the chosen column if pressed once, copy it if pressed twice;
• NVDA+control+numpadMinus (numpad mode): like NVDA+control+0 in keyboard mode, read or copy the 10th, 20th, etc column;
• NVDA+control+- (keyboard mode, EN-US layout): in a list with 10+ columns, change interval and process columns from 11 to 20, from 21 to 30, and so on (change last char according to your layout, from settings);
• NVDA+control+numpadPlus (numpad mode): like previous command;
• NVDA+control+enter (numpadEnter in numpad mode): open header manager;
• NVDA+control+delete (numpadDelete in numpad mode): read relative current item position (i.e.: item 7 of 10);
• Arrows and NVDA+tab (in empty list): repeat "0 items" message;
• NVDA+downArrow (desktop layout) or NVDA+a (laptop layout): start say all (this gesture depends on original one under "Input gestures"/"System caret");
• NVDA+shift+upArrow (desktop layout) or NVDA+shift+s (laptop layout): report amount and names of current selected list items (like previous command for customization);
• NVDA+control+f: open find dialog (not customizable);
• NVDA+f3: find next occurrence of previously entered text (not customizable);
• NVDA+shift+f3: find previous occurrence (not customizable).
Support
This add-on provide a general support for more common lists (see below), and some specific applications. Main author (Alberto Buffolino) cannot guarantee compatibility/functionality for those applications he not uses, like Outlook and Windows Mail, but he'll be happy to collaborate with their users or accept a pull request for them.
Lists supported are:
• SysListView32;
• DirectUIHWND (present in 64-bit systems);
• WindowsForms10.SysListView32.* (applications that use .NET);
• multi-column treeview like as that presents in RSSOwlnix;
• Mozilla table (tipically, Thunderbird message list, thread-grouping supported).""", "https://addons.nvda-project.org/files/get.php?file=cr"],
	"TextNav":["unknown", """TextNav allows you to find text that you want to read on a web page in just a single keystroke. More precisely, it adds a keystroke to jump to next or previous text paragraphs - that is a paragraph containing one or more sentences. This feature might be useful to quickly find the textual part of a web page or to skip over menus, advertisements and other not important page elements.
Keystrokes:
• Alt+Shift+Down arrow: Go to next text paragraph.
• Alt+Shift+Up arrow: Go to previous text paragraph.""", "https://addons.nvda-project.org/files/get.php?file=textnav"],
	"AudioChart":["unknown", """AudioChart add-on for NVDA allows you to play excel time series as a continuous sound.
Usage
Select a cell or a column of cells containing time series in Microsoft Excel.
Keystrokes
• NVDA+A: Play audio chart.
• NVDA+A twice quickly: Show calibration dialog window. In laptop layout, press NVDA+Control+Shift+A instead.
Source code
     https://github.com/mltony/nvda-audio-chart/""", "https://addons.nvda-project.org/files/get.php?file=audiochart"],
	"BluetoothAudio":["unknown", """Bluetooth Audio is an NVDA add-on that improves sound quality when working with bluetooth headphones or speakers.
Most bluetooth devices enter standby mode after a few seconds of inactivity. That means that when NVDA starts speaking again, the first split second of sound will be lost. Bluetooth Audio add-on prevents bluetooth devices from entering standby mode by constantly playing a silent sound, that is inaudible to a human ear.
Warning: using Bluetooth Audio add-on might reduce battery life of your bluetooth device.""", "https://addons.nvda-project.org/files/get.php?file=btaudio"],
	"Calibre":["unknown", """An NVDA add-on with some accessibility enhancements for the interface of Calibre eBook Management
• F10 brings the focus to the toolbar. Then you can navigate it with standard keys (tab and arrows); enter to activate item and key applications to display the context menu; escape to exit the toolbar.
• F12 search the current book in Google
• NVDA+Alt+End says the total of books in the current library view and the number of books selected
• NVDA+Control+H open the context menu for settings of the current column
• I in library view reads the book information.
Keystrokes can be customized in Preferences of NVDA > Input gestures when calibre are open. Also you can define in preferences the way NVDA reads the table headers in the library (rows and columns, columns only or none).
Take a look at the documentation of Calibre for know more Keyboard shortcuts.
Covered by the GNU General Public License. See the file COPYING.txt for more details.""", "https://addons.nvda-project.org/files/get.php?file=cae"],
	"ToolbarsExplorer":["unknown", """This add-on makes easier to use toolbars in applications, providing an exploration model derived by object navigation, with simplified gestures.
Commands
• Alt+applications: starts toolbars exploration
(you can remap it via NVDA gesture manager, under Object navigation).
During exploration, following gestures are available:
• Left/right arrow: moves to previous/next toolbar;
• Up/down arrow: scrolls up/down items in current toolbar;
• Enter: activates toolbar or its item;
• Space: simulates left mouse click on toolbar or its item;
• Applications/shift+F10: simulates right mouse click on toolbar or its item;
• Escape: exits from exploration.
Additionally, you can perform actions on toolbars or its items using any gesture provided by NVDA, as exactly as when you move to objects with standard object navigation.
Notes
Exploration is terminated explicitly pressing escape, and implicitly:
• performing an action on toolbar or its item (with space, applications/shift+F10, enter);
• pressing a gesture that moves out of current toolbar objects (alt, windows, tab, NVDA+F1, object navigation gestures, etc).
Other gestures not containing alt, windows or escape (as h, 1, shift, shift+h, control+z) simply does nothing.
Suggestions
• The add-on may fail in Mozilla applications the first time after add-on installation/update; please restart NVDA and Mozilla applications to resolve;
• In LibreOffice, best configuration is probably default or single toolbar, set it on view menu/toolbar position.""", "https://addons.nvda-project.org/files/get.php?file=tbx"],
	"Input Lock":["unknown", """Do you have kids or pets at home? Do you have a cat and It likes very much climbing your table and walking over your keyboard? Do you accidentally move the mouse to random parts in the screen while using your laptop? Then Input Lock is for you! You will be able to leave your computer alone and turned on without risk.
Once installed, you will be able to lock your keyboard, touch screen, if your laptop has one, mouse and Braille display.
Usage
This addon adds two extra gestures to NVDA. By default they are unassigned, so you will have to configure them from Input gestures dialog. Read the NVDA User Guide for more information.
When you press the toggle input lock gesture, NVDA will say "Input locked". Your input devices will be blocked until you press the same gesture again. In that moment, NVDA will say "Input unlocked" and everything will work as usual.
If you press the toggle mouse block gesture, your mouse will be locked. Press this command again to unlock it. While mouse is locked, you can use NVDA gestures to move it, and click with left and right buttons, but You can't move the mouse itself. Mouse clicks can also be disabled from Input lock category in NVDA settings dialog (NVDA 2018.2 and later) or from add-on settings dialog for older versions, available under preferences menu. In addition, from these settings you can control wether mouse locks when NVDA is started or not.
Note: when mouse clicks are blocked, you can't use any NVDA gestures to work with the mouse.
Limitations and known problems
Input Lock has the following known problems:
• The shortcuts control+alt+del and windows+l can be used even when the keyboard is locked.
• NVDA unlocks the keyboard and other input methods when the computer wakes up from standby mode or the session is restored from the Windows lock screen.
• On some laptops, the touchpad still accepts user input after mouse is blocked.""", "https://addons.nvda-project.org/files/get.php?file=inputlock"],
	"Add-on Updater":["2021.3 +", """This add-on brings NVDA Core issue 3208 to life: ability to check for, download, and apply add-on updates.
To check for updates after installing this add-on, go to NVDA menu/Tools/Check for add-on updates. If updates are available, a list of add-on updates will be shown, with each entry consisting of description, current version, and the new version. Select Update, and NVDA will download and apply updates in sequence, with a prompt to restart your NVDA shown afterwards.
The following add-ons provide built-in update feature and thus updates will not be checked via this add-on:
• Braille Extender
• WeatherPlus
IMPORTANT NOTES:
• This is a proof of concept add-on. Once the relevant feature is included in NVDA, this add-on will be discontinued.
• If the new add-on updates specify a compatibility range (minimum and last tested NVDA versions) and if the NVDA version you are running does not fall within the compatibility range according to NVDA, add-on updating will not proceed.
• Not all add-ons come with development releases. If you are not getting updates after choosing to install development versions of an add-on, switch to stable channel for affected add-ons.
• On some systems (particularly computers joined to a corporate domain), add-on update check functionality may not work properly, therefore add-on updates must be downloaded manually.
Version 22.02
• NVDA 2021.3 or later is required.
• On Windows 10, add-on update toast notifications are localized.
Version 22.01
• NVDA 2021.2 or later is required.
• On server systems running Windows Server 2016 and later, add-on updates will be presented in a dialog instead of using toast notifications.
Version 21.10
• It is again possible to check for add-on updates on some systems, notably after a clean Windows installation.
Version 21.09
• NVDA 2021.1 or later is required.
• on Windows 10 and later, it is possible to select add-on update notification between a toast message and an update dialog. This can be configured from Add-on Updater settings found in NVDA Settings screen.
• Add-on Updater will no longer check minimum Windows release information for add-ons as add-ons such as Windows App Essentials provide better Windows compatibility information.
Version 21.07
• On Windows 10 and later, a toast notification will be shown when add-on updates are available. Note that you cannot click this notification - you must open NvDA menu/Tools/Check for add-on updates to review updates.
• When legacy add-ons dialog is shown at startup, you can now review legacy add-ons and reasons just like add-on updates.
• Improved add-on update check internals, including use of add-on metadata collection provided by the community to validate add-on compatibility. Among other things, this eliminates add-on releases for adding update checks for new add-ons.
Version 21.05
• NvDA will no longer play error tones if trying to check updates while using NVDA 2021.1 alpha snapshots, caused by changes to wxPython GUI toolkit.
Version 21.03
• NVDA 2020.4 or later is required.
• NVDA will present an error dialog if errors occur while checking for add-on updates such as loss of Internet connection.
Version 20.11
• NVDA 2020.3 or later is required.
• Resolved more coding style issues and potential bugs with Flake8.
• NVDA will no longer play error tones or appear to do nothing when using the add-on while NVDA is running from source code. A message about this fact will be recorded in the log instead.
Version 20.07
• NVDA 2020.1 or later is required.
• If one or more legacy add-ons (such as Screen Curtain) are installed, Add-on Updater will present a message asking you to disable or uninstall the add-ons listed.
• You can now save, reload, or reset Add-on Updater settings by pressing Control+NVDA+C, Control+NVDA+R once, or Control+NVDA+R three times, respectively.
Version 20.06
• Resolved many coding style issues and potential bugs with Flake8.
Version 20.04
• NVDA will no longer appear to do nothing or play error tones when trying to update add-ons through Add-on Updater.
• Resolved an issue where "check for add-on updates" item wasn't present in NVDA Tools menu.
Version 20.03
• NVDA 2019.3 or later is required.
• When installing add-on updates, Add-on Updater will no longer check for compatibility range. NVDA itself will check add-on compatibility.
Version 19.11
• When add-on updates are available, NVDA will announce how many updates are available.
Version 19.09
• Requires NVDA 2019.2 or later.
• Timeout errors seen when attempting to download some add-on updates (notably add-on files hosted on GitHub) has been resolved.
Version 19.04
• Requires NVDA 2019.1 or later.
• When installing add-on updates, both minimum and last tested versions will be checked.
Version 19.01
• Requires NVDA 2018.4 or later.
• Improved responsiveness when checking for add-on updates.
• Made the add-on more compatible with Python 3.
Version 18.12.2
• Python 3 ready.
• Fixed compatibility with recent NVDA alpha snapshots where add-on updates would not download.
Version 18.12.1
• Added localizations.
Version 18.12
• Updates for disabled add-ons can be checked. They will stay disabled after updating them.
• During updates, if an add-on requires specific NVDA version and/or Windows release, these will be checked, and if one of these does not match, an error message will be shown and update will be aborted, resulting in no changes to already installed add-on version.
• When automatic update check is enabled and when updates are ready, NVDA will present the updates list instead of asking if you wish to review updates.
Version 18.10
• Initial stable release (still marked as proof of concept).""", "https://addons.nvda-project.org/files/get.php?file=nvda3208"],
	"Access8Math":["unknown", """This NVDA addon provides the function of reading math content. Although the original NVDA already equipped this feature by applying MathPlayer, some functions still needed to be improved, such as not providing or incomplete specific language translation, not providing specific language navigation and browsing and many more.
Navigation interactive mode can segment a math content into smaller partial fragments for speaking, and select the read fragment and method through a series of keyboard key operations. This function can better understand the structure and items of long math content. The hierarchical relationship with the item.
Reading feature
• Read math content written in MathML in web browser(Mozilla Firefox, Microsoft Internet Explorer and Google Chrome) or read Microsoft Word math content written in MathType. (MathPlayer installed only)
• Interaction: Press space or enter on the MathML math object to enter navigation interactive mode. It means you can browse part of the sub-content in the math content and move between sub-contents or zoom the size of the sub-content
• 
Pressing "Space" in math content to open "Access8Math interaction window" which contains "interactive" and "copy" button.
• interaction: Into math content to navigate and browse. Also, you can partially explore the subparts in expression and move or zoom the content between the subpart.
• copy: Copy MathML object source code.
• 
Text review: Press the numeric keyboard 1-9 during navigation to read the mathematical content of the serialized text word by word and line by line
• Analyze the overall mathematical meaning of the content: analyze the structure of MathML, and when it meets a specific rule, read it aloud in the mathematical meaning of the rule
• Analyze the mathematical meaning of the content item: When navigating and browsing, it will prompt the meaning of the content under its upper content. For example, there are two score items, and moving between them will enroll the item as the denominator or numerator
navigation interactive mode command：
• "Down Arrow": Zoom in on a smaller subpart of the math content.
• "Up Arrow": Zoom out to a larger subpartthe of the math content .
• "Left Arrow": Move to the previous math content.
• "Right Arrow": Move to the next math content.
• "Home": Move back to the top.(Entire math content)
• "Ctrl+c": Copy object MathML source code
• "Numpad 1~9": Reading the math content into serialized text using NVDA Reviewing Text.
• "ESC": Exit the navigation mode.
Writing feature
Writing mixed content (text content and mathematical content):
write mixed content
Use delimiter(start delimiter "(" and end delimiter ")", LaTeX block) to determine the area between the text content and the mathematical content, that is, the data in LaTeX block is mathematical content (LaTeX), and the data outside LaTeX block is text content.
Press alt+h in edit field to convert an HTML document with mixed text data and mathematical data and can be reviewed or exported. The data in the LaTeX block will be converted to MathML for presentation with normal text.
• review: Open the converted HTML document through a program that opens the .HTML extension by default.
• export: Pack the converted HTML document into a zip file.
Press alt+m key in edit field to pop up the markup command window, select "LaTeX" and press enter, the LaTeX block will be added to the current cursor and the cursor will be automatically moved into it for quick input the content.
Press alt+l key in edit field to pop up the LaTeX command window, select the LaTeX command item to be added and press enter to add the corresponding LaTeX syntax at the current cursor and automatically move the cursor to the appropriate input point for quick Enter the content.
LaTeX command window
• Select the LaTeX command item and press f1~f12 to set the shortcut
• Select the LaTeX command item and press d to remove the shortcut that has been set
• Select the LaTeX command item and press enter to add the corresponding LaTeX syntax at the current cursor
Edit cursor navigation move
• In edit field, press alt+left arrow key to move to the start point of the previous data block
• In edit field, press alt+down key without moving, but only read the content of the current data block
• In edit field, press alt+right arrow key to move to the start point of the next data block
• In edit field, press alt+home to move to the start point of the current data block
• In edit field, press alt+end to move to the end point of the current data block
Edit cursor navigation move and select
• In the editing area, press alt+shift+left arrow key to move to the previous data block and select
• In the editing area, press alt+shift+down key to move to the current data block and select
• In the editing area, press alt+shift+right arrow to move to the next data block and select
Press alt+s in edit field to turn on or off the shortcut mode. When the shortcut mode is on, press f1~f12 to quickly insert LaTeX syntax. When the shortcut mode is on, press shift+f1~f12 to read out the LaTeX commands currently bound to the shortcut.
In edit field and the cursor is in the LaTeX block, press alt+i to enter navigation interactive mode
Press NVDA+shift+space in edit field to turn on or off the edit single letter navigation mode. When the edit single letter navigation mode is turned on, you can move the edit cursor with single letter navigation
The following keys by themselves jump edit cursor to the next available block, while adding the shift key causes them to jump edit cursor to the previous block:
• l: move to the next LaTeX block
• t: move to the next text block
mixed content example: The solution of the quadratic equation in one variable (ax2+bx+c=0) is (\frac{-b\pm\sqrt{b2-4ac}}{2a}).
settings
All Access8Math menus are centralized in tools -> Access8Math.
read feature settings
• 
General Settings dialog:
• Language: Access8Math speaking language
• Item interval time: Setting pause time between items. Values from 1 to 100, the smaller the value, the shorter the pause time, and the greater the value, the longer the pause time.
• Showing Access8Math interaction window when entering interaction mode: Whether to show "Access8Math interaction window" when pressing the space key on the math object.
• Analyze the mathematical meaning of the content: perform semantic analysis on the mathematical content, and when it meets a specific rule, using that rule to speak.
• Reading pre-defined meaning in dictionary when navigating in interactive mode: When the pattern is definied in the dictionary, use dictionary to read the meaning of subpart in the upper layer part.
• Reading of auto-generated meaning when navigating in interactive mode: When the pattern is not difined or incomplete in dictionary, use automatic generation function to read the meaning of subpart in the upper layer part.
• Using a beep to alert no move: When navigating in interactive mode, It will hint by beep. If it is not checked, it will hint by speaking "no move".
• Using NVDA+gesture to active action: Whether shortcut key needs to be added with NVDA key when write mixed content in edit field
• 
Rule Settings dialog box: select whether rules are actived.
localization
• "Unicode dictionary" allows customizing the reading method for each symbol text.
• "Mathematics Rules" allows customizing the reading method for each type of mathematics.
• "Add a new language" can add languages: that were not originally provided in the built-in. After adding, there will be more newly added language families in the general settings and can be used to define the reading method through the "unicode dictionary" and "mathematics rules" to reach localization
Math Rules
Access8Math establishes 46 mathematical rules according to the mathematical type and logic to decide the reading math method and order. According to different local math reading logic, the math reading text and order can be changed. The method is as follows:
Edit: After entering the "math rule", the window lists 46 math rules. Choose any math rule and select the "Edit" to enter the editing entry.
The "editing entry" can be divided into two major blocks, the "Serialized ordering" and the "Child role".
• Serialized ordering: Math rule is divided into multiple blocks according to the reading order. In this area, the reading order of child node and the delimitation text of start, inter- and the end can be changed. Taking the fractional rule mfrac as an example, this rule is divided into five reading blocks. The order 0, 2, and 4 represent the initial prompt, the project segmentation prompt, and the end prompt, respectively, and the meanings text can be changed in each field. Order 1 and 3 adjust the reading sequence of child node which can be changed in the drop-down menu.
• Child role: The next-level sub-item of the mathematical rule. Taking the fractional rule mfrac as an example, the rule contains the numerator and the denominator. The sub-content in the upper sub-content meaning can be changed in the child-node role field.
Example: You can check the reading method of this math rule after editing. After clicking, a math content is preset the corresponding math rules for confirming whether the reading method is as expected.
Recover default: Restores the list of math rules to their initial presets.
Import: Import math rules files, which can be used to load math rules files.
Export: Save the math rules file to the specified path to share or keep.
example
Math contents in Wiki are all written by MathML.
• Quadratic equation: https://en.wikipedia.org/wiki/Quadratic_equation
• Matrix multiplication: https://en.wikipedia.org/wiki/Matrix_multiplication
• Cubic function: https://en.wikipedia.org/wiki/Cubic_function
Quadratic equation
• LaTeX: (ax2+bx+c=0)
• MathML: -b±b2-4ac2a
github: https://github.com/tsengwoody/Access8Math
Please report any bugs or comments, thank you!
Access8Math v3.0 Update
• Write mathematical content in AsciiMath
• Write mathematical content in LaTeX
• Writing mixed content (text content and mathematical content)
• Use shortcut keys to move the cursor to different types of blocks in edit field
• Use command menu to select commands in edit field
• Set shortcuts in the LaTeX command menu
• Review and export content in edit field to HTML
Access8Math v2.6 Update
• Auto entering interactive mode when showing Access8Math interaction window.
• You can choose how to hint no movement in interactive mode: beep or speech 'no move' two way.
• The content of the current item will be repeated again When there is no movement.
Access8Math v2.5 Update
• Adding Russian translation of rules and UI. Thanks to the translation work of Futyn-Maker.
• Fixing compound symbol translation failed bug.
• Removing duplicates of lowercase letters and added general uppercases in en unicode.dic(0370~03FF).
Access8Math v2.4 Update
• Fix bug.
Access8Math v2.3 Update
• Compatibility with Python3
• refactoring module and fix code style
• Adding one symbol vector rule
Access8Math v2.2 Update
• fix bug incorrect speech when a single node has more characters.
• Fix compatibility issue in NVDA 2019.2, thanks to pull requests of CyrilleB79.
• Fix bug in unicode dict has duplicate symbols.
• Add translations in French, thanks to the translation work of CyrilleB79.
• Adjust keyboard shortcut.
Access8Math v2.1 Update
• In "General Settings", you can set whether "Access8Math interaction window" is automatically displayed when entering interactive mode.
• In interactive mode, "interaction window" can be displayed manually via ctrl+m when "interaction window" are not showed.
• Fix multi-language switching bug.
• Add translations in Turkish, thanks to the translation work of cagri (çağrı doğan).
• Compatibility update for nvda 2019.1 check for add-on`s manifest.ini flag.
• Refactoring dialog window source code.
Access8Math v2.0 Update
• Add multi-language new-adding and customizing settings,and add three windows of "unicode dictionary", "math rule", "New language adding"
• The "unicode dictionary" can customize the reading way of each math symbolic text.
• "math rule" can customize the reading method and preview the modification through the sample button before completed.
• "New language adding" allows adding language not provided in the built-in system. The newly language will be added to the general settings, and multi-language customization can be achieved through reading definition of "unicode dictionary" and "mathematical rules".
• improved in interactive mode, you can use the number keys 7~9 to read sequence text in the unit of line.
Access8Math v1.5 update log
• In "general setting" dialog box add setting pause time between items. Values from 1 to 100, the smaller the value, the shorter the pause time, and the greater the value, the longer the pause time.
• Fix setting dialog box can't save configure in NVDA 2018.2.
Access8Math v1.4 update log
• Adjust settings dialog box which divided into "general setting" and "rules setting" dialog box. "General Settings" is the original "Access8Math Settings" dialog box, and "Rule Settings" dialog box is for selecting whether specific rules are enabled.
• 
New rules
• vector rule: When there is a "⇀" right above two Identifier, the item is read as "Vector...".
• frown rule：When there is a " ⌢ " right above two Identifier, the item is read as "frown...".
• 
Fix bug.
Access8Math v1.3 update log
• 
New rule
• positive rule: Read "positive" rather than "plus" when plus sign in first item or its previous item is certain operator.
• square rule: When the power is 2, the item is read as "squared".
• cubic rule: When the power is 3, the item is read as "cubed".
• line rule: When there is "↔" right above two Identifier, the item is read as "Line ...".
• line segment rule: When there is "¯" right above two Identifier, the item is read as "Line segement ...".
• ray rule: When there is a "→" right above two Identifier, the item is read as "Ray ..."
• 
Add interaction window: Pressing "Space" in math content to open "Access8Math interaction window" which contains "interaction" and "copy" button.
• interaction: Into math content to navigate and browse.
• copy: Copy MathML object source code.
• 
Add zh_CN UI language(.po).
• Adjust inheritance relationship between rules to ensure proper use of the appropriate rules in conflict.
• Fix bug.
Access8Math v1.2 update log
• 
New rule
• negative number rule: Read 'negative' rather than 'minus sign' when minus sign in first item or its previous item is certain operator.
• integer add fraction rule: Read 'add' between integer and fraction when fraction previous item is integer.
• 
Program architecture improve
• add sibling class
• add dynamic generate Complement class
• 
Fix bug
Access8Math v1.1 update log
• In navigation mode command, "Ctrl+c" copy object MathML source code.
• 
Settings dialog box in Preferences:
• Language: Access8Math reading language on math content.
• Analyze the mathematical meaning of content: Semantically analyze the math content, in line with specific rules, read in mathematical meaning of that rules.
• Read defined meaning in dictionary: When the pattern is definied in the dictionary, use dictionary to read the meaning of subpart in the upper layer part.
• Read of auto-generated meaning: When the pattern is not difined or incomplete in dictionary, use automatic generation function to read the meaning of subpart in the upper layer part.
• 
Add some simple rule. Single rules are simplified versions of various rules. When the content only has one single item, for better understanding and reading without confusion, you can omit to choose not to read the script before and after the content.
• Update unicode.dic.
• Fix bug.""", "https://addons.nvda-project.org/files/get.php?file=access8math"],
	"Text Information":["unknown", """This add-on allows for getting information based on selected text. Simply select something and use a keystroke to get information. You should, hopefully, be presented with something that fits the context.
note: This package is distributed under the terms of the GNU General Public License, version 2 or later. Please see the file COPYING.txt for further details.
keystrokes
note: These keystrokes asume your using the english keyboard layout, and might not work otherwise. If there's a problem, first try changing them in the input gestures dialog.
• NVDA+; (semicolon): provides information based on the text that's selected
• NVDA+SHIFT+; (semicolon): provides information about text on the clipboard
• NVDA+control+; (semicolon): speaks the last reported information. Press twice to get it displayed in a dialog.
supported services
Currently, the following features are supported:
• IP address information using the IPInfoDB API. An API key is provided, however I by no means guarantee it'll always work. You can generate your own, and enter it at the top of init.py, replacing the old one.
• english dictionary definitions from the princeton wordnetweb. Note: these definitions are not the best, and the database lacks definitions for simple words, e.g. could, you, etc.
• ISBN lookups via the google books API
• credit card type verification
Note: Regular expressions are used to verify data. There are currently some that aren't used, phone numbers and emails. This might be changed in the future.
contributing
Contributions are appreciated. You can either submit a PR, or get in contact with the following info:
twitter: @cartertemm
email: crtbraille@gmail.com""", "https://addons.nvda-project.org/files/get.php?file=txtinfo"],
	"SentenceNav":["unknown", """SentenceNav is an NVDA add-on that allows you to read text by sentences, as opposed to by paragraphs or words.
Please note that "Jump to next  paragraph with text" feature has been move to TextNav add-on that needs to be installed separately.
Keystrokes
• Alt+Down arrow: Go to next sentence.
• Alt+Up arrow: Go to previous sentence.
• NVDA+Alt+S: Speak current sentence.
• Alt+Windows+Down arrow: Go to next phrase.
• Alt+Windows+Up arrow: Go to previous phrase.""", "https://addons.nvda-project.org/files/get.php?file=sentencenav"],
	"BrailleExtender":["2019.3 and beyond", """BrailleExtender is an NVDA add-on that provides various features at braille level. Currently, the following features are implemented:
• reload two favorite braille display with shortcuts.
• automatic review cursor tethering in terminal role like in PuTTY, Powershell, bash, cmd.
• auto scroll.
• switch between several input/output braille tables.
• mark the text with special attributes through dot 7, dot 8 or both.
• use two output braille tables simultaneously.
• display tab signs as spaces.
• reverse forward scroll and back scroll buttons.
• say the current line during text scrolling either in review mode, or in focus mode or both.
• translate text easily in Unicode braille and vice versa. E.g.: z <--> ⠵.
• convert cell description to Unicode braille and vice versa. E.g.: 123 <--> ⠇.
• lock braille keyboard.
• launch an application/URL with gesture.
• braille dictionaries.
• type with one-hand from braille keyboard.
• display undefined characters from braille tables (including emojis) using altenative representations.
• enter any character from braille keyboard (including emojis).
• skip blank lines during text scrolling.
• and much more!
For some braille displays, it extends the braille display commands to provide:
• offer complete gesture maps including function keys, multimedia keys, quick navigation, etc.;
• emulate modifier keys, and thus any keyboard shortcut;
• offer several keyboard configurations concerning the possibility to input dots 7 and 8, enter and backspace;
• add actions and quick navigation through a rotor.
Once the add-on is installed, read the documentation and go through the settings using the BrailleExtender submenu (located in the NVDA menu).
Let's explore some common features
Representation of undefined characters
The extension allows you to customize how an undefined character should be represented within a braille table. To do so, go to the — Representation of undefined characters — settings. You can choose between the following representations:
• Use braille table behavior (no description possible)
• Dots 1-8 (⣿)
• Dots 1-6 (⠿)
• Empty cell (⠀)
• Other dot pattern (e.g.: 6-123456)
• Question mark (depending on output table)
• Other sign/pattern (e.g.: ??)
• Hexadecimal
• Hexadecimal, HUC8
• Hexadecimal, HUC6
• Decimal
• Octal
• Binary
You can also combine this option with the “describe the character if possible” setting.
Notes:
• To distinguish the undefined set of characters while maximizing space, the best combination is the usage of the HUC8 representation without checking the “Show punctuation/symbol name for undefined characters if available” option.
• To learn more about the HUC representation, see https://danielmayr.at/huc/
• Keep in mind that definitions in tables and those in your table dictionaries take precedence over character descriptions, which also take precedence over the chosen representation for undefined characters.
Getting Current Character Info
This feature allows you to obtain various information regarding the character under the cursor using the current input braille table, such as: the HUC8 and HUC6 representations; the hexadecimal, decimal, octal or binary values; A description of the character if possible; the Unicode braille representation and the braille pattern dots.
Pressing the defined gesture associated to this function once shows you the information in a flash message and a double-press displays the same information in a virtual NVDA buffer.
On supported displays the defined gesture is ⡉+space. No system gestures are defined by default.
For example, for the '&' character, we will get the following information:
&: 0x26, 38, 0o46, 0b100110
and (AMPERSAND [Po])
⢿ (1234568)
⣥⣺⡧, ⠿⠺⠏⠏
Advanced braille input
This feature allows you to enter any character from its HUC8 representation or its hexadecimal/decimal/octal/binary value. Moreover, it allows you to develop abbreviations. To use this function, enter the advanced input mode and then enter the desired pattern. Default gestures: NVDA+Windows+i or ⡊+space (on supported displays). Press the same gesture to exit this mode. Alternatively, an option allows you to automatically exit this mode after entering a single pattern. If you want to enter a character from its HUC8 representation, simply enter the HUC8 pattern. Since a HUC8 sequence must fit on 3 or 4 cells, the interpretation will be performed each time 3 or 4 dot combinations are entered. If you wish to enter a character from its hexadecimal, decimal, octal or binary value, do the following:
. 1Enter ⠼
. 2
Specify the basis as follows:
• ⠭ or ⠓: for a hexadecimal value
• ⠙: for a decimal value
• ⠕: for an octal value
• ⠃: for a binary value
. 3
Enter the value of the character according to the previously selected basis.
. 4Press Space to validate.
For abbreviations, you must first add them in the dialog box — Advanced input mode dictionary —. Then, you just have to enter your abbreviation and press space to expand it. For example, you can define the following abbreviations: "⠎⠺" with "sandwich", "⠋⠛⠋⠗" to "🇫🇷".
Here are some examples of sequences to be entered for given characters:
Character
HUC8
Hexadecimal
Decimal
Octal
Binary
👍 (thumbs up)
⣭⢤⡙
⠭1f44d or ⠓1f44d
⠙128077
⠕372115
⠃11111010001001101
😀 (grinning face)
⣭⡤⣺
⠭1f600 or ⠓1f600
⠙128512
⠕373000
⠃11111011000000000
🍑 (peach)
⣭⠤⠕
⠭1f351 or ⠓1f351
⠙127825
⠕371521
⠃11111001101010001
🌊 (water wave)
⣭⠤⠺
⠭1f30a or ⠓1f30a
⠙127754
⠕371412
⠃11111001100001010
Note: the HUC6 input is currently not supported.
One-hand mode
This feature allows you to compose a cell in several steps. This can be activated in the general settings of the extension's preferences or on the fly using NVDA+Windows+h gesture by default (⡂+space on supported displays). Three input methods are available.
Method #1: fill a cell in 2 stages on both sides
With this method, type the left side dots, then the right side dots. If one side is empty, type the dots correspondig to the opposite side twice, or type the dots corresponding to the non-empty side in 2 steps.
For example:
• For ⠛: press dots 1-2 then dots 4-5.
• For ⠃: press dots 1-2 then dots 1-2, or dot 1 then dot 2.
• For ⠘: press 4-5 then 4-5, or dot 4 then dot 5.
Method #2: fill a cell in two stages on one side (Space = empty side)
Using this method, you can compose a cell with one hand, regardless of which side of the Braille keyboard you choose. The first step allows you to enter dots 1-2-3-7 and the second one 4-5-6-8. If one side is empty, press space. An empty cell will be obtained by pressing the space key twice.
For example:
• For ⠛: press dots 1-2 then dots 1-2, or dots 4-5 then dots 4-5.
• For ⠃: press dots 1-2 then space, or 4-5 then space.
• For ⠘: press space then 1-2, or space then dots 4-5.
Method #3: fill a cell dots by dots (each dot is a toggle, press Space to validate the character)
In this mode, each dot is a toggle. You must press the space key as soon as the cell you have entered is the desired one to input the character. Thus, the more dots are contained in the cell, the more ways you have to enter the character.
For example, for ⠛, you can compose the cell in the following ways:
• Dots 1-2, then dots 4-5, then space.
• Dots 1-2-3, then dot 3 (to correct), then dots 4-5, then space.
• Dot 1, then dots 2-4-5, then space.
• Dots 1-2-4, then dot 5, then space.
• Dot 2, then dot 1, then dot 5, then dot 4, and then space.
• Etc.""", "https://addons.nvda-project.org/files/get.php?file=brlext"],
	"IndentNav":["unknown", """This add-on allows NVDA users to navigate by indentation level or offset of lines or paragraphs. In browsers it allows to quickly find paragraphs with the same offset from the left edge of the screen, such as first level comments in a hierarchical tree of comments. Also while editing source code in many programming languages, it allows to jump between the lines of the same indentation level, as well as quickly find lines with greater or lesser indentation level.
Usage in browsers
IndentNav can be used to navigate by offset from the left edge of the screen. IN particular, you can press NVDA+Alt+DownArrow or UpArrow to jump to the next or previous paragraph that has the same offset. For example, this can be useful when browsing hierarchical trees of comments (e.g. on reddit.com) to jump between first level comments and skipping all the higher level comments.
Strictly speaking, IndentNav can be used in any application, for which NVDA provides a tree interceptor object.
Keystrokes:
• NVDA+Alt+UpArrow or DownArrow: Jump to previous or next paragraph with the same offset.
• NVDA+alt+LeftArrow: Jump to previous paragraph with lesser offset.
• NVDA+Alt+RightArrow: Jump to next paragraph with greater offset.
Usage in text editors
IndentNav can also be useful for editing source code in many programming languages. Languages like Python require the source code to be properly indented, while in many other programming languages it is strongly recommended. With IndentNav you can press NVDA+Alt+DownArrow or UpArrow to jump to next or previous line with the same indentation level. You can also press NVDA+Alt+LeftArrow to jump to a parent line, that is a previous line with lower indentation level. In Python you can easily find current function definition or class definition. You can also press NVDA+Alt+RightArrow to go to the first child of current line, that is next line with greater indentation level.
If your NVDA is set to express line indentation as tones, then IndentNav will quickly play the tones of all the skipped lines. Otherwise it will only crackle to roughly denote the number of skipped lines.
Keystrokes:
• NVDA+Alt+UpArrow or DownArrow: Jump to previous or next line with the same indentation level within the current indetnation block.
• NVDA+Alt+Control+UpArrow or DownArrow: Force-jump to previous or next line with the same indentation level. This command will jump to other indentation blocks (such as other Python functions) if necessary.
• NVDA+alt+LeftArrow: Jump to parent - that is previous line with lesser indentation level.
• NVDA+Alt+RightArrow: Jump to first child - that is next line with greater indentation level within the same indentation block.""", "https://addons.nvda-project.org/files/get.php?file=indentnav"],
	"Mozilla Apps Enhancements":["unknown", """This add-on provides NVDA enhancements for Mozilla aps.
Firefox
• NVDA+A (desktop) or NVDA+Control+A (laptop) Reads the page address. If pressed twice quickly, copies it to clipboard.
• NVDA+End (desktop) or NVDA+Shift+End (laptop) Reads the status bar. If pressed twice quickly, copies it to clipboard.
• NVDA+F8 Shows a list of opened tabs. If pressed twice quickly, shows buttons of tool bar.
• NVDA+Control+N Reads the last notification and it takes the system focus to it if it is possible. By pressing two times quickly shows the history of notifications.
• NVDA+F6 Brings the focus to the document.
Thunderbird
• In a message window:
• Control+Shift+(1-4) Reads the sender and recipients of the message. If pressed twice quickly, opens the options menu.
• Control+Shift+5 Reads the subject of the message.
• Control+Shift+6 Reads date of the message.
• Control+Shift+A Brings the focus to the list of attachments, if any. (These scripts are also available in the list of messages if you activate the preview pane.)
• In the bar of fast filtering:
• Press down Arrow to display more options, enter to check/unchek the selected option.
• In messages list:
• If the preview pane is active, press NVDA+downArrow (desktop) or NVDA+A (laptop) to read the message without leaving the list.
• Control+NVDA+1-9 moves between columns.
• NVDA+H Displays a dialog in which you can change the order of the columns in the message list.
Keystrokes can be customized in Preferences of NVDA > Input gestures when Firefox or Thunderbird are open.""", "https://addons.nvda-project.org/files/get.php?file=moz"],
	"sayCurrentKeyboardLanguage":["unknown", """This addon was created following a request from a member on the nvda-addons mailing list.
It provides a keyboard shortcut, NVDA + F4, which allows to retrieve and give the language of the current keyboard.
If pressed twice, gives the default language of the system.
At the first version of this module, it had been proposed as simple globalPlugin to paste in the configuration directory of NVDA, it was then transformed into addon.
Notes
If the NVDA + F4 keyboard shortcut conflicts with another command, you can change it by going to the Preferences menu of NVDA, in the "Input gestures" submenu.
You will then find the script in the "System status" category.
Compatibility
• This add-on is compatible with the versions of NVDA ranging from 2014.3 until 2019.3.""", "https://addons.nvda-project.org/files/get.php?file=ckbl"],
	"Object Location Tones":["2019.3 and beyond", """• Note: this add-on is deprecated and will become end of life in 2021.
After installing this add-on and restarting NVDA (or when you enable this add-on), as you navigate to different controls, you'll hear tones to indicate where the object is located on screen. To turn object location tones off, uninstall or disable this add-on from add-ons manager.
Important notes:
• If using Audio Themes or similar add-ons, it is advised to disable Object Location Tones add-on.
• If a control is offscreen, tones will not be played.""", "https://addons.nvda-project.org/files/get.php?file=objLoc"],
	"Lambda Add-On for NVDA":["unknown", """This project is an appModule for the LAMBDA Software. It has been inspired by the work of Peter Lecky at the Comenius University. LAMBDA (Linear Access to Mathematic for Braille Device and Audio-synthesis) is a software that helps blind people to read and write math using a braille display and/or a speech synthesizer. LAMBDA is the result of an EU-Project. For more information about LAMBDA please visit https://www.lambdaproject.org/.
The current version of the addon has braille tables for Italian and Spanish languages and its interface is available in most of the NVDA's official languages, because it is translated by the NVDA translations community. If you are a non-italian user of LAMBDA and you would like to contribute with the porting of the braille table in your language, feel free to contact the author (see below) or subscribe the project mailing list.
Please note: This addon has been developed by Alberto Zanella as a voluntary activity. Nor the author or the contributors are involved in selling and / or development of the software Lambda. If you need more information about Lambda, or you need support on how to use it, please contact your local distributor. If you are encountering any difficulties when using or installing this addon, please contact the author or use the "Issues" link on the Github project page.
Official Github Repository
Addon Features:
Speech support:
• Dialogs and menus are properly reported;
• Natural speech support for math formulas using the Lambda math engine, i.e. "compound root 3 sep compound root 3 x plus 24, close compound root, minus 3 equals 0";
• implemented the Reading by character, words, lines and Say All;
• Speaks when a block of text is selected or extended (using CTRL+B and SHIFT+CTRL+B);
• Speaks when moving in the text editor using standard Windows commands and Lambda-specific commands;
• Both Extended and Short speech modes are supported (you can select it using the Tools menu in Lambda);
• Special dialogs like structure mode, calculator, and matrix window are now correctly reported and NVDA reads correctly when moving the cursor around or when new text is typed ;
• Typing echo uses the Lambda text processor, so symbols and markers will be correctly reported.
Braille support:
• The addon installs (inside the user profile directory) and activates a custom braille table. This table may be different for different languages. Custom braille tables were made from ones in the Lambda plugin for JAWS (jbt file). Then symbols and markers are represented using the same dots patterns;
• The addon creates an NVDA profile for a standard braille configuration. By this, the output is set to the custom braille table only when the Lambda application is active;
• Dialogs and menus are properly reported in braille;
• The content of the editor is correctly rendered in braille and the user is able to move using braille scrolling keys or cursor routing keys;
• Starting from the addon version 1.1.0, there are two ways in which the text in the Lambda editor is rendered: "Flat mode" and "non-Flat Mode". When the "Flat mode" is on, NVDA will use the Display Model to retrieve information from the editor and to determine the caret position. This is specially beneficial when the user needs to move around on the screen, even in white spaces. When the "Flat Mode" is set to "off", text rendering on the braille display is more stable, since NVDA uses Windows API to retrieve it. However when the the caret is moved in white spaces next to the end of the line of text, the braille display does not follow the real cursor as long as a non-white space is added by the user.
The "flat mode" is active by default. You can toggle "flat mode" on or off by pressing NVDA+SHIFT+F.
We strongly recommend to disable the Flat Mode if you are using custom DPI in Windows (Custom sizing option), especially when you have screen settings with more than 96 dpi (larger than 100%).
• The structure of dialog boxes is easier, repeated information has been removed;
• The selection will be marked properly using dots 7 and 8, and marking is properly refreshed while standard Windows commands (SHIFT+ARROWS) or Lambda specific commands (CTRL+B, CTRL+SHIFT+B) are pressed.
Before starting to use this addon.
This addon creates an NVDA profile named "lambda" which is associated with the "lambda.exe" application. The profile automatically sets all braille options: the custom braille table, the focus tethering and flat mode settings.
If a previous profile with the same name is present in your system, the addon will not override it and you have to manually adjust your configuration profile.
To stave off this situation, if you have specific settings you'd like to preserve, you can use the "Revert LAMBDA Profile Wizard". The shortcut to start this tool is NVDA+alt+r (when focused in LAMBDA).
An easy option is also to delete old versions of the "lambda" profile after the installation of the addon. To do so, open the NVDA menu, select the "Configuration profiles" menu Item and press ENTER.
In the Configuration profiles dialog, you'll be able to locate and delete the "lambda" profile. The profile will be re-created the next time the Lambda application is started.
Deleting the "lambda" profile should be an easy solution also when the addon runs into any problem. For instance, if the braille table is not properly set, instead of manually configuring the profile, you can simply delete it. The addon will create a new one the next time you'll load the Lambda editor.
Each time the Lambda editor is started, this addon checks if a profile with the name "lambda" exists. If it doesn't, it automatically generates a profile with the following form:
filename : userData\profiles\lambda.ini :

[braille]
    readByParagraph = False
    tetherTo = focus
    translationTable = path-to-the-addon-brailleTable-dir\tableName

[lambda]
    brailleFlatMode = True
Where :
• path-to-the-addon-brailleTable-dir : is the absolute path of the addon directory + "\brailleTables"
• tableName : depends on the active NVDA language. Currently only the italian and Spanish braille tables, "lambda-ita.utb" and "lambda-esp.utb" respectively, is present.
Addon Keyboard Shortcuts:
• NVDA+Shift+f: Toggle braille flat mode on or off;
• NVDA+alt+r: Open the "Revert LAMBDA Profile Wizard";
• NVDA+d: Duplicate lines (use this instad of control+d).
Known issues:
Due to a bug present in LAMBDA, the add-on provides an extra-logic that reports white spaces. This logic may fail in the following situations:
• When words like "space", "spazio" "Espacio" etc. are inserted into the text, they may be reported by NVDA as the local NVDA language translation.
• Blank lines are not reported by the LAMBDA speech engine. The user will hear the translation of the word "space" instead. This could be both a blank line or a line containing only the word "space".
Useful tips
This is a set of tips that will help you on using the addon in a more eficient way.
• Character-by-character reporting: Normally, when working with maths you would like NVDA to report things you're writing character by character. To do this, there are a couple of simple steps: ensure to have the focus on the LAMBDA's window or one of its variants (the six dots representation, for example); press NVDA+2 (number two) or navigate to NVDA menu>Preferences>Keyboard settings and check the box to Speak typed characters; go to LAMBDA>Options>Voice paramethers and ensure the checkbox "echo" is ON, otherwhise NVDA won't receive anything from the speech engine while you are typing. And done, NVDA will speak written characters, but don't worry, only in LAMBDA or its special windows, the settings for the rest of applications will be left as they were.
Addon mailing list:
To report bugs, suggestions or if you want to contribute you can subscribe the Addon Group (in English). You can subscribe from the website: https://groups.io/g/lambda-nvda.""", "https://addons.nvda-project.org/files/get.php?file=lambda"],
	"Speak Passwords":["2019.3", """This addon allows NVDA to speak typed characters and words while typing into password fields. However, navigation in password fields is unchanged.
Usage
Passwords are spoken automatically when this addon is installed, controlled by "Speak typed characters" and "Speak typed words".
To stop passwords from being spoken, disable Speak typed characters/words or disable/uninstall the add-on.""", "https://addons.nvda-project.org/files/get.php?file=spp"],
	"Clipspeak":["2018.3 / 2019.3", """Clipspeak is an addon that allows NVDA to automatically announce clipboard operations (such as cut, copy and paste), along with other common editing operations such as select all, undo and redo. In order to prevent announcement in inappropriate situations, Clipspeak performs checks on the control and the clipboard in order to make an informed decision as to whether such an announcement is necessary. Because of this, Clipspeak's announcements may be inaccurate. By default, Clipspeak's gestures are mapped to those commonly used by English versions of Windows, I.E.:
• CTRL+A: Select all
• CTRL+Z: Undo
• CTRL+Y: Redo
• CTRL+X: Cut
• CTRL+C: Copy
• CTRL+V: Paste
If these are not the shortcuts commonly used for these tasks on your version of Windows, you will need to remap these gestures in the input gestures configuration.""", "https://addons.nvda-project.org/files/get.php?file=cs"],
	"Review Cursor Copier":["unknown", """This NVDA add-on provides various commands for copying the text under the review cursor to the clipboard. Currently, the following commands are implemented:
• Copy the line under the review cursor
• Copy the word under the review cursor
• Copy from the start of the current line to the review cursor
• Copy from the review cursor to the end of the current line
• Copy from the start of the current word to the review cursor
• Copy from the review cursor to the end of the current word
None of these commands have key bindings by default. Please use the input gestures dialog located under the NVDA settings menu to set them. All of the commands provided by this add-on can be found under the "text review" category. More information about setting and modifying input gestures can be found in the NVDA user guide.
License
This work is licensed under the GNU General Public License, version 2.""", "https://addons.nvda-project.org/files/get.php?file=rccp"],
	"Mush Client":["unknown", """This add-on enhances the mush Client for use with NVDA.
From the add-on description:
This add-on provides the following accessibility improvements for Mush Client:
. 1The NVDA navigator object is now automaticly set to the output window of Mush Client in order to make reviewing output easier.
. 2Two new hotkeys (NVDA-8 and NVDA-9) toggle the "speech interrupt for typed characters" and "speech interrupt for enter key" settings respectively.
. 3Additionally, NVDA-Enter and numbpad-Enter will set the position of the NVDA navigator object to the last line of text in the output window and speak it.
. 4The "report Dynamic Content Changes", "caret moves review cursor", "speech interrupt for typed characters", and "speech interrupt for enter key" settings are now automatically saved to a separate configuration file when the Mush Client window loses focus and restored when it receives focus again.
Note: since most people will be using Mush Client with a speech plugin for auto-speaking incoming text, NVDA's "report Dynamic Content Changes" setting is disabled by default to avoid speaking incoming lines twice. If you want to turn on the automatic speaking of incoming lines by NVDA, toggle this setting on with the NVDA-5 hotkey.""", "https://addons.nvda-project.org/files/get.php?file=mush"],
	"mIRC":["unknown", """This is an enhanced version of the mIRC app module that comes with NVDA.
From add-on description:
This add-on is an enhanced version of the mIRC App Module included in NVDA.
. 1The NVDA navigator object is now automaticly set to the output window of mIRC in order to make reviewing output easier.
. 2Two new hotkeys (NVDA-8 and NVDA-9) toggle the "speech interrupt for typed characters" and "speech interrupt for enter key" settings respectively.
. 3Additionally, NVDA-Enter and numbpad-Enter will set the position of the NVDA navigator object to the last line of text in the output window and speak it.
. 4The "report Dynamic Content Changes", "caret moves review cursor", "speech interrupt for typed characters", and "speech interrupt for enter key" settings are now automaticly saved to a special configuration file when the mIRC window loses focus and restored when it receives focus again.
Note: NVDA's "report Dynamic Content Changes" setting is enabled by default. If you use a speech system for mIRC such as Talking IRC or mIRC With Speech, toggle this setting off with the NVDA-5 hotkey to prevent incoming lines from being spoken twice.""", "https://addons.nvda-project.org/files/get.php?file=mirc"],
	"ObjPad":["2020.1 / 2020.4", """This add-on provides quick commands to manage objects on screen, including navigation and other possibilities.
Commands
• Control+NVDA+TAB: Steps through arrow key modes (see below for details).
Arrow key modes
The add-on provides four ways to use arrow keys:
• Classic (or normal mode): use arrow keys to move cursor.
• Object nav: use arrow keys to move to next/previous/parent/first child objects.
• Web: use arrow keys to cycle through elements and move between them.
• Scan mode: use arrow keys to move through objects on screen regardless of hierarchy.
The following commands are available with arrow keys set to object nav:
• Right arrow: next object.
• Left arrow: previous object.
• Up arrow: parent object.
• Down arrow: first child object.
• SPACE or ENTER: activate.
With web mode active (elements are normal or moving by object, link, form field, heading, frame, table, list, landmark):
• Right arrow: next element.
• Left arrow: previous element.
• Up arrow: previous element type.
• Down arrow: next element type.
• SPACE or ENTER: activate.
With scan mode active:
• Down arrow: next object or the next line.
• Up arrow: previous object or previous line.
• Right arrow: review next character.
• Left arrow: previous character.
• Control+right arrow: next word.
• Control+left arrow: previous word.
• SPACE or ENTER: activate.""", "https://addons.nvda-project.org/files/get.php?file=objPad"],
	"Report Symbols":["2019.3 +", """This add-on allows to listen the typed symbols (non alphanumeric or blank characters), even when the speaking of typed characters is turned off in NVDA.
It's based on the old ReportSymbols add-on, developed by the same author. You should uninstall it to use this version.
Preferences menu
• Report Symbols settings: Allows to set preferences for the speaking of typed symbols.
Note: A gesture to open this dialog can be assigned from NVDA menu, Preferences submenu, Input gestures dialog, Configuration category.""", "https://addons.nvda-project.org/files/get.php?file=rsy-o"],
	"StationPlaylist":["2021.2 +", """This add-on package provides improved usage of StationPlaylist Studio and other StationPlaylist apps, as well as providing utilities to control Studio from anywhere. Supported apps include Studio, Creator, Track Tool, VT Recorder, and Streamer, as well as SAM, SPL, and AltaCast encoders.
For more information about the add-on, read the add-on guide.
IMPORTANT NOTES:
• This add-on requires StationPlaylist suite 5.30 or later.
• If using Windows 8 or later, for best experience, disable audio ducking mode.
• Starting from 2018, changelogs for old add-on releases will be found on GitHub. This add-on readme will list changes from version 21.10 (2021) onwards.
• While Studio is running, you can save, reload saved settings, or reset add-on settings to defaults by pressing Control+NVDA+C, Control+NVDA+R once, or Control+NVDA+R three times, respectively. This is also applicable to encoder settings - you can save and reset (not reload) encoder settings if using encoders.
مفاتيح الاختصار
Most of these will work in Studio only unless otherwise specified.
• Alt+Shift+T من نافذة الاستوديو: للإعلان عن الوقت المنقضي للمسار أو التراك المشغل حاليا.
• Control+Alt+T (مسح بإصبعين لأسفل بنمط SPL) من نافذة الاستوديو: للإعلان عن الوقت المتبقي للمسار أو التراك المشغل حاليا.
• NVDA+Shift+F12 (two finger flick up in SPL touch mode) from Studio window: announces broadcaster time such as 5 minutes to top of the hour. Pressing this command twice will announce minutes and seconds till top of the hour.
• Alt+NVDA+1 (two finger flick right in SPL mode) from Studio window: Opens alarms category in Studio add-on configuration dialog.
• Alt+NVDA+1 from Creator's Playlist Editor and Remote VT playlist editor: Announces scheduled time for the loaded playlist.
• Alt+NVDA+2 from Creator's Playlist Editor and Remote VT playlist editor: Announces total playlist duration.
• Alt+NVDA+3 from Studio window: Toggles cart explorer to learn cart assignments.
• Alt+NVDA+3 from Creator's Playlist Editor and Remote VT playlist editor: Announces when the selected track is scheduled to play.
• Alt+NVDA+4 from Creator's Playlist Editor and Remote VT playlist editor: Announces rotation and category associated with the loaded playlist.
• Control+NVDA+f from Studio window: Opens a dialog to find a track based on artist or song name. Press NVDA+F3 to find forward or NVDA+Shift+F3 to find backward.
• Alt+NVDA+R من نافذة الاستوديو: لخطوات إعدادات الإعلان عن البحث في المكتبة
• Control+Shift+X من نافذة الاستوديو: لخطوات إعدادات ميقات البرايل.
• Control+Alt+left/right arrow (while focused on a track in Studio, Creator, Remote VT, and Track Tool): Move to previous/next track column.
• Control+Alt+Home/End (while focused on a track in Studio, Creator, Remote VT, and Track Tool): Move to first/last track column.
• Control+Alt+up/down arrow (while focused on a track in Studio, Creator, Remote VT, and Track Tool): Move to previous/next track and announce specific columns.
• Control+NVDA+1 through 0 (while focused on a track in Studio, Creator (including Playlist Editor), Remote VT, and Track Tool): Announce column content for a specified column (first ten columns by default). Pressing this command twice will display column information on a browse mode window.
• Control+NVDA+- (hyphen while focused on a track in Studio, Creator, Remote VT, and Track Tool): display data for all columns in a track on a browse mode window.
• NVDA+V while focused on a track (Studio's playlist viewer only): toggles track column announcement between screen order and custom order.
• Alt+NVDA+C while focused on a track (Studio's playlist viewer only): announces track comments if any.
• Alt+NVDA+0 from Studio window: Opens the Studio add-on configuration dialog.
• Alt+NVDA+P from Studio window: Opens the Studio broadcast profiles dialog.
• Alt+NVDA+F1: Open welcome dialog.
الأوامر غير المعينة
The following commands are not assigned by default; if you wish to assign them, use Input Gestures dialog to add custom commands. To do so, from Studio window, open NVDA menu, Preferences, then Input Gestures. Expand StationPlaylist category, then locate unassigned commands from the list below and select "Add", then type the gesture you wish to use.
• التحول إلى نافذة الأستديو من أي برنامج آخر.
• نمط التحكم في تطبيق SPL.
• Announcing Studio status such as track playback from other programs.
• Announcing encoder connection status from any program.
• نمط SPL المساعد من الأستوديو.
• الإعلان عن الوقت متضمن الثواني من SPL Studio.
• الإعلان عن درجة الحرارة
• الإعلان عن عنوان المسار التالي إذا كان مجدول.
• الإعلان عن عنوان المسار المشغل حاليا
• تحديد المسار الحالي لبدأ تحليل وقت المسار
• إجراء تحليل وقت المسار
• Take playlist snapshots.
• البحث عن نص بأعمدة محددة
• البحث عن مسارات تقع بين معدل وقت معين عبر باحث عن معدلات الوقت.
• تشغيل أو تعطيل حالة بث البيانات بسرعة
Additional commands when using encoders
The following commands are available when using encoders:
• F9: connect the selected encoder.
• F10 (SAM encoder only): Disconnect the selected encoder.
• Control+F9: Connect all encoders.
• Control+F10 (SAM encoder only): Disconnect all encoders.
• F11: ينتقل بين تشغيل وتعطيل الرجوع لنافذة الاستوديو بعد الاتصال بالخادم.
• shift+F11: ينتقل بين تشغيل وتعطيل إمكانية تشغيل أول مسار بعد الاتصال بالخادم.
• Control+F11: التبديل بين تشغيل وتعطيل المراقبة الخلفية للتشفير المحدد.
• Control+F12: opens a dialog to select the encoder you have deleted (to realign encoder labels and settings).
• Alt+NVDA+0 and F12: Opens encoder settings dialog to configure options such as encoder label.
فضلا عن ذلك, إتاحة أوامر لمراجعة الأعمدة وتشمل:
• Control+NVDA+1: موقع التشفير
• Control+NVDA+2: encoder label.
• Control+NVDA+3 من sam encoder: تنسيق التشفير.
• Control+NVDA+3 from SPL and AltaCast Encoder: Encoder settings.
• Control+NVDA+4 from SAM Encoder: Encoder connection status.
• Control+NVDA+4 from SPL and AltaCast Encoder: Transfer rate or connection status.
• control+nvda+5 من تشفير SAM: وصف حالة الاتصال
مساعد نمط أوامر SPL
This layer command set allows you to obtain various status on SPL Studio, such as whether a track is playing, total duration of all tracks for the hour and so on. From any SPL Studio window, press the SPL Assistant layer command, then press one of the keys from the list below (one or more commands are exclusive to playlist viewer). You can also configure NVDA to emulate commands from other screen readers.
The available commands are:
• A: التشغيل الآلي.
• C (Shift+C in JAWS layout): Title for the currently playing track.
• C (JAWS layout): Toggle cart explorer (playlist viewer only).
• D (R in JAWS layout): Remaining duration for the playlist (if an error message is given, move to playlist viewer and then issue this command).
• E: Metadata streaming status.
• Shift+1 through Shift+4, Shift+0: Status for individual metadata streaming URL's (0 is for DSP encoder).
• F: Find track (playlist viewer only).
• H: مدة الموسيقى للساعة الحالية.
• Shift+H: Remaining track duration for the hour slot.
• I (L in JAWS layout): Listener count.
• K: Move to the marked track (playlist viewer only).
• Control+K: Set the current track as the place marker track (playlist viewer only).
• L (Shift+L in JAWS layout): Line in.
• M: الميكروفون
• N: لتشغيل المسار التالي.
• P: حالة التشغيل (المسار يعمل أم متوقف).
• shift+P: حدة المسار الحالي.
• R (Shift+E in JAWS layout): Record to file enabled/disabled.
• shift+r: مراقبة حالة التقدم في البحث بالمكتبة.
• S: Track starts (scheduled).
• Shift+S: Time until selected track will play (track starts in).
• T: Cart edit/insert mode on/off.
• U: وقت الاستوديو
• W: حالة التقس ودرجة الحرارة إذا كانت معدة.
• y: حالة قائمة التشغيل المعدلة.
• F8: Take playlist snapshots (number of tracks, longest track, etc.).
• Shift+F8: Request playlist transcripts in numerous formats.
• F9: Mark current track for start of playlist analysis (playlist viewer only).
• F10: Perform track time analysis (playlist viewer only).
• f12: الانتقال بين الملف الحالي وملف لم يتم تعريفه من قبل.
• F1: نمط المساعدة
• shift+f1: فتح دليل المستخدم على الإنترنت
نمط التحكم في تطبيق SPL
هو عبارة عن نمط يزودك بمجموعة من المفاتيح كي تتمكن من التحكم في التطبيق من أي مكان. اضغط أمر نمط التحكم في SPL وسينطق NVDA, "نمط التحكم في Station PlayList Studio." اضغط أي من الأوامر التي سيلي ذكرها للتحكم في مختلف إعدادات الاستوديو بالتطبيق كالتحكم في تشغيل أو تعطيل الميكروفون, أو تشغيل المسار التالي.
والأوامر التي يتيحها هذا النمط هي:
• P: Play the next selected track.
• U: Pause or unpause playback.
• S: Stop the track with fade out.
• T: Instant stop.
• M: Turn on microphone.
• Shift+M: Turn off microphone.
• A: Turn on automation.
• Shift+A: Turn off automation.
• L: Turn on line-in input.
• Shift+L: Turn off line-in input.
• R: Remaining time for the currently playing track.
• Shift+R: Library scan progress.
• C: Title and duration of the currently playing track.
• Shift+C: Title and duration of the upcoming track if any.
• E: Encoder connection status.
• I: Listener count.
• Q: Studio status information such as whether a track is playing, microphone is on and others.
• Cart keys (F1, Control+1, for example): Play assigned carts from anywhere.
• H: Layer help.
Track and microphone alarms
By default, NVDA will play a beep if five seconds are left in the track (outro) and/or intro, as well as to hear a beep if microphone has been active for a while. To configure track and microphone alarms, press Alt+NVDA+1 to open alarms settings in Studio add-on settings screen. You can also use this screen to configure if you'll hear a beep, a message or both when alarms are turned on.
الباحث عن المسارات
If you wish to quickly find a song by an artist or by song name, from track list, press Control+NVDA+F. Type or choose the name of the artist or the song name. NVDA will either place you at the song if found or will display an error if it cannot find the song you're looking for. To find a previously entered song or artist, press NVDA+F3 or NVDA+Shift+F3 to find forward or backward.
ملحوظة: الباحث عن المسارات حساس لحالة الأحرف.
مستكشف التنويهات
وفقا لإصدار البرنامج, يتيح لك برنامج SPL تعيين مفتاح ل96 تنويه. يتيح لك NVDA سماع أي تنويه معين لهذه الأوامر.
To learn cart assignments, from SPL Studio, press Alt+NVDA+3. Pressing the cart command once will tell you which jingle is assigned to the command. Pressing the cart command twice will play the jingle. Press Alt+NVDA+3 to exit cart explorer. See the add-on guide for more information on cart explorer.
تحليل وقت المسار
للحصول على مدة المسارات المحددة لتشغيلها, قم بتحديد المسار الحالي لبدأ عملية تحليل الوقت (من مساعد spl اضغط على f9), ثم اضغط على f10 بعد الانتهاء من التحديد.
Columns Explorer
By pressing Control+NVDA+1 through 0, you can obtain contents of specific columns. By default, these are first ten columns for a track item (in Studio: artist, title, duration, intro, outro, category, year, album, genre, mood). For playlist editor in Creator and Remote VT client, column data depends on column order as shown on screen. In Studio, Creator's main track list, and Track Tool, column slots are preset regardless of column order on screen and can be configured from add-on settings dialog under columns explorer category.
Track column announcement
You can ask NVDA to announce track columns found in Studio's playlist viewer in the order it appears on screen or using a custom order and/or exclude certain columns. Press NVDA+V to toggle this behavior while focused on a track in Studio's playlist viewer. To customize column inclusion and order, from column announcement settings panel in add-on settings, uncheck "Announce columns in the order shown on screen" and then customize included columns and/or column order.
Playlist snapshots
You can press SPL Assistant, F8 while focused on a playlist in Studio to obtain various statistics about a playlist, including number of tracks in the playlist, longest track, top artists and so on. After assigning a custom command for this feature, pressing the custom command twice will cause NVDA to present playlist snapshot information as a webpage so you can use browse mode to navigate (press escape to close).
Playlist Transcripts
Pressing SPL Assistant, Shift+F8 will present a dialog to let you request playlist transcripts in numerous formats, including in a plain text format, an HTML table or a list.""", "https://addons.nvda-project.org/files/get.php?file=spl"],
	"mp3DirectCut":["unknown", "unknown", "https://addons.nvda-project.org/files/get.php?file=mp3dc"],
	"Crash Hero":["unknown", "Note: this add-on is primarily useful for developers, or people running test versions of NVDA. Use this add-on to let NVDA prompt you for more information after a crash. ", "https://addons.nvda-project.org/files/get.php?file=crh-dev"],
	"Tip of the Day":["unknown", """This addon is supposed to help you learn how to use NVDA by giving you tips every day.
instructions:
Once the addon is installed, when NVDA reboots for the first time, it will ask you to select how comfortable with using NVDA you are. You should select your comfort level, for example if you are a novice with computers, select beginner.
Then, NVDA will show you a tip of the day. You can press the forward and back buttons to change what tip you are seeing, and then press close or escape when you are done. To find these buttons, you can press tab once the dialog is up until you find the buttons, and press enter or space to press them. When you are done, either press escape from the edit field, or press the close button. To get a tip at any time, select the tip of the day option from the NVDA menu.
To change your comfort level with your computer so the addon can give you more targeted tips, select the tip of the day option from the NVDA preferences menu. The add-on will ask you how comfortable you are with NVDA once the add-on is installed and when NVDA reboots.""", "https://addons.nvda-project.org/files/get.php?file=tod"],
	"SpeechPlayer in Espeak":["unknown", """SpeechPlayer in Espeak
A hybrid of speechPlayer and eSpeak, containing the Edward voice.""", "https://addons.nvda-project.org/files/get.php?file=spie"],
	"Golden Cursor":["2019.3 and beyond", """This add-on allows you to move the mouse using a keyboard and save mouse positions for applications.
Key commands
• Control+NVDA+L: view saved mouse positions for an application if any.
• Shift+NVDA+l: save a tag or a label for the current mouse position in the currently focused application.
• Windows+NVDA+C: change mouse movement unit.
• Windows+NVDA+R: toggle mouse restriction.
• Windows+NVDA+S: toggle reporting of mouse position in pixels.
• Windows+NVDA+J: move mouse to a specific x and y position.
• Windows+NVDA+P: report mouse position.
• Windows+NVDA+M: sswitch mouse arrows on or off.
• Windows+NVDA+arrow keys (or just arrow keys if mouse arrows is on): move mouse.
Note: these gestures can be reassigned via NVDA's Input Gestures dialog under Golden Cursor """, "https://addons.nvda-project.org/files/get.php?file=gc"],
	"Day of the week":["unknown", """This add-on allows you to know the day related to a particular date. It adds a submenu in the NVDA Tools menu named Day of the week, containing 2 items:
• 
The first one named Search a day, opens a dialog composed of 3 controls:
• A listbox to choose or type your date;
• An OK button to display a messageBox containing your day;
• And the Cancel button to close the dialog.
• 
The second one named dayOfTheWeek add-on settings opens the parameters of the add-on to specify whether you want to report labels for date fields or not, it is composed of the following elements:
• Enable accessibility of the date selector;
• 
Level of the announces of labels, you will then have 3 choices:
• Long (it's the default choice);
• Short (for short announcements);
• Off (to disable labels announcements).
• 
Enable announcement of the current date field value only, when moving vertically;
• An OK button to save your configuration;
• A Cancel button to cancel and close the dialog.""", "https://addons.nvda-project.org/files/get.php?file=dw"],
	"VLC Media Player":["unknown", """This addon provides some accessibility features for VLC Media Player.
1. Allows navigating through the playback controls using Tab and Shift+Tab. To activate a selected control press enter.
2. Reads status bar information (press I). The gesture can be set up in NVDA preferences.
3. Says elapsed time when moving back and forward using VLC keystrokes: Control plus left/right arrow to skip 1 minute and Shift plus left/right arrows to skip 5 seconds. You can set the verbosity in the NVDA preferences. You can also assign a keyboard shortcut to toggle it.
4. Announces state when change random mode (key R) and repeat mode (key L).
5. 
There are some layered windows and panels that NVDA is not able to focus it automatically when they are displayed. Press Control+Tab to try to bring them to the front.
6. 
Important note: This addon is optimized for versions of VLC 3.0 and higher; it will not work correctly with earlier versions.
7. Covered by the GNU General Public License. See the file COPYING.txt for more details.""", "https://addons.nvda-project.org/files/get.php?file=vlc"],
	"Windows App Essentials":["2021.2 +", """Note: Originally called Windows 10 App Essentials, it was renamed to Windows App Essentials in 2021 to support Windows 10 and future releases such as Windows 11. Parts of this add-on will still refer to the original add-on name.
This add-on is a collection of app modules for various modern Windows apps, as well as enhancements and fixes for certain controls found in Windows 10 and later.
The following app modules or support modules for some apps are included (see each app section for details on what is included):
• Calculator
• Cortana
• Mail
• Maps
• Microsoft Solitaire Collection
• Modern keyboard (emoji panel/dictation/voice typing/hardware input suggestions/clipboard history/modern input method editors)
• Notepad (Windows 11)
• People
• Settings (system settings, Windows+I)
• Weather
• Miscellaneous modules for controls such as Start Menu tiles
Notes:
• This add-on requires Windows 10 21H1 (build 19043) or later and is compatible with Windows 11.
• Although installation is possible, this add-on does not support Windows Enterprise LTSC (Long-Term Servicing Channel) and Windows Server releases.
• Some add-on features are or will be part of NVDA screen reader.
• For entries not listed below, you can assume that features are part of NVDA, no longer applicable as the add-on does not support unsupported Windows releases such as old Windows 10 versions, or changes were made to Windows and apps that makes entries no longer applicable.
• Some apps support compact overlay mode (always on top in Calculator, for example), and this mode will not work properly with portable version of NVDA.
For a list of changes made between each add-on releases, refer to changelogs for add-on releases document.
General
• NVDA can announce suggestion count when performing a search in majority of cases, including when suggestion count changes as search progresses. This is now part of NVDA 2021.3.
• In addition to UIA event handlers provided by NVDA, the following UIA events are recognized: drag complete, drop target dropped, layout invalidated. With NVDA's log level set to debug, these events will be tracked, and for UIA notification event, a debug tone will be heard if notifications come from somewhere other than the currently active app. Events built into NVDA such as name change and controller for events are tracked from an add-on called Event Tracker.
• When opening, closing, reordering (Windows 11), or switching between virtual desktops, NVDA will announce active virtual desktop name (desktop 2, for example).
• NVDA will no longer announce Start menu size text when changing screen resolutions or orientation.
• When arranging Start menu tiles or Action Center quick actions with Alt+Shift+arrow keys, NVDA will announce information on dragged items or new position of the dragged item.
• Announcements such as volume/brightness changes in File Explorer and app update notifications from Microsoft Store can be suppressed by turning off Report Notifications in NVDA's object presentation settings.
Calculator
• NVDA will no longer announce graphing calculator screen message twice.
• In Windows 10, history and memory list items are properly labeled.
Cortana
• Textual responses from Cortana are announced in most situations.
• NVDA will be silent when talking to Cortana via voice.
Mail
• When reviewing items in messages list, you can now use table navigation commands to review message headers. Note that navigating between rows (messages) is not supported.
Maps
• NVDA plays location beep for map locations.
• When using street side view and if "use keyboard" option is enabled, NVDA will announce street addresses as you use arrow keys to navigate the map.
Microsoft Solitaire Collection
• NVDA will announce names of cards and card decks.
Modern keyboard
This includes emoji panel, clipboard history, dictation/voice typing, hardware input suggestions, and modern input method editors for certain languages. When viewing emojis, for best experience, enable Unicode Consortium setting from NVDA's speech settings and set symbol level to "some" or higher. When pasting from clipboard history in Windows 10, press Space key instead of Enter key to paste the selected item. NVDA also supports updated input experience panel in Windows 11.
• In Windows 10, when an emoji group (including kaomoji and symbols group) is selected, NVDA will no longer move navigator object to certain emojis.
• Added support for updated input experience panel (combined emoji panel and clipboard history) in Windows 11.
• In Windows 11, it is again possible to use the arrow keys to review emojis when emoji panel opens.
Notepad
This refers to Windows 11 Notepad version 11 or later.
• NVDA will announce status items such as line and column information when report status bar command (NVDA+End in desktop layout, NvDA+Shift+End in laptop layout) is performed.
• NVDA will no longer announce entered text when pressing Enter key from the document.
People
• When searching for contacts, first suggestion will be announced, particularly if using recent app releases.
Settings
• Certain information such as Windows Update progress is reported automatically, including Storage sense/disk cleanup widget and errors from Windows Update.
• Progress bar values and other information are no longer announced twice.
• Odd control labels seen in certain Windows installations has been corrected.
• NVDA will announce the name of the optional quality update control if present (download and install now link in Windows 10, download button in Windows 11).
• In Windows 11, breadcrumb bar items are properly recognized.
Weather
• Tabs such as "forecast" and "maps" are recognized as proper tabs (patch by Derek Riemer).
• When reading a forecast, use the left and right arrows to move between items. Use the up and down arrows to read the individual items. For example, pressing the right arrow might report "Monday: 79 degrees, partly cloudy, ..." pressing the down arrow will say "Monday" Then pressing it again will read the next item (Like the temperature). This currently works for daily and hourly forecasts.""", "https://addons.nvda-project.org/files/get.php?file=w10"],
	"Ventrilo":["unknown", "This add-on enhances support for Ventrilo chat client. ", "https://addons.nvda-project.org/files/get.php?file=vent"],
	"Easy Table Navigator":["2019.3 to 2021.1", "https://addons.nvda-project.org/files/get.php?file=etn"],
	"Clock and calendar Add-on for NVDA":["2019.3 +", """This add-on enables the advanced clock, alarm timer and calendar functionality for NVDA.
You can configure NvDA to announce time and date in formats other than what Windows provides by default. Additionally, you can obtain the current day, week number, as well as the remaining days before the end of the current year, and you can also set automatic time announcement on specified interval. There's also a stopwatch and Alarm timer features built-in to the add-on that lets you time your tasks, such as copying files, installing programs, or cooking meals.
Notes:
• if you install the add-on as an update, during the installation process, the wizard detects if the old configuration is compatible with the new one and offers to correct it before installing, then you'll just have to validate the OK button to confirm that.
• On Windows 10 and later, you can use Alarms and Clock app to manage stopwatch and timers.
مفاتيح الاختصار
• NVDA+F12: get current time
• NVDA+F12 pressed twice quickly: get current date
• NVDA+F12 pressed three times quickly: reports the current day, the week number, the current year and the remaining days before the end of the year
• NVDA+Shift+F12: enter clock layer
Unassigned commands
The following commands are not assigned by default; if you wish to assign them, use Input Gestures dialog to add custom commands. To do so, open NVDA menu, Preferences, then Input Gestures. Expand Clock category, then locate unassigned commands from the list below and select "Add", then enter the gesture you wish to use.
• Elapsed and remaining time before the next alarm. pressing this gesture twice quickly will cancel the next alarm.
• Stop currently playing alarm sound.
• Display schedule alarms dialog box.
Layered commands
To use layered commands, press NVDA+Shift+F12 followed by one of the following keys:
• S: Starts, resets or stops the stopwatch
• R: Resets stopwatch to 0 without restarting it
• A: gives the elapsed and remaining time before the next alarm
• T: opens schedule alarms dialog.
• C: Cancel the next alarm
• Space: Speaks current stopwatch or count-down timer
• p: If an alarm is too long, allows to stop it
• H: List all layered commands (Help)
Configuration and usage
To configure clock functionality, open NvDA menu, Preferences, then Settings, and configure the following options from Clock panel:
• Time and date display format: use these combo boxes to configure how NVDA will announce time and date when you press NVDA+F12 once or twice quickly, respectively.
• Interval: choose the time announcement interval from this combo box (off, every 10 minutes, 15 minutes, 30 minutes, or every hour).
• Time announcement (enabled if interval is not off): choose between speech and sound, sound only, or speech only.
• Clock chime sound (enabled if interval is not off): select the clock chime sound.
• Quiet hours (enabled if interval is not off): select this checkbox to configure quiet hours range when automatic time announcement should not occur.
• Quiet hours time format (enabled if quiet hours is enabled): select how quiet hours options are presented (12-hour or 24-hour format).
• Quiet hours start and end times: select hour and minute range for quiet hours from hours and minutes combo boxes.
To schedule alarms, open NVDA menu, Tools, then select Schedule Alarms. The dialog contents include:
• Alarm duration in: select alarm/timer duration between hours, minutes, and seconds.
• Duration: enter alarm duration in the unit specified above.
• Alarm sound: select the alarm sound to be played.
• Stop and pause buttons: stop or pause a long alarm sound.
Click OK, and a message will inform you the curretnly selected alarm duration.""", "https://addons.nvda-project.org/files/get.php?file=cac"],
	"Dual Voice":["unknown", "This add-on allows you to use two synthesizers or voices to read text in your chosen voice language. ", "https://sourceforge.net/projects/dualvoice/files/latest/download"],
	"Clip Contents Designer":["2019.3 +", """This add-on is used to add text to the clipboard, which can be useful when you want to join sections of text together ready for pasting. The clipboard content can also be cleared an shown in browse mode.
Keyboard commands
• NVDA+windows+c: Add selected text, Unicode braille characters which represent MathML objects, or the string which has been marked with the review cursor, to the clipboard.
• NVDA+windows+x: Clear clipboard contents.
• Not assigned: Copies to (or cuts from) the clipboard, with the possibility of being asked for a previous confirmation.
• Not assigned: Shows the clipboard text as HTML in browse mode, or announces if clipboard is empty or has contents which can't be presented in a browseable message, for instance if files or folders are been copied from Windows Explorer.
• Not assigned: Shows the textual clipboard contents as plain text in browse mode, or announces if clipboard is empty or has contents which can't be presented in a browseable message, for instance if files or folders are been copied from Windows Explorer.
Clip Contents Designer settings
This panel is available from NVDA's menu, Preferences submenu, Settings dialog.
It contains the following controls:
• Type the string to be used as a separator between contents added to the clipboard: Allows to set a separator which can be used to find the text segments once the entire added text is pasted.
• Add text before clip data: It's also possible to choose if the added text will be appended or prepended.
• Select the actions which require previous confirmation: You can choose, for each action available, if it should be performed inmediately or after confirmation. Available actions are: add text, clear clipboard, emulate copy and emulate cut.
• Request confirmation before performing the selected actions when: You can select if confirmations will be requested always, just if text is contained in the clipboard, or if clipboard is not empty (for example if you've copied a file, not text).
• Format to show the clipboard text as HTML in browse mode: If you're learning HTML markup language, you may choose Preformatted text in HTML or HTML as shown in a web browser, to have an idea of how your HTML code will be rendered by NVDA in a browser. The difference between preformatted and conventional HTML is that the first option will preserve consecutive spaces and line breaks, and the second one will compact them. For example, write some HTML tags like h1, h2, li, pre, etc., select and copy the text to clipboard, and use clipContentsDesigner add-on to show the text in a browseable message.
• Maximum number of characters when showing clipboard text in browse mode: Please, be aware that increasing this limit may produce issues if the clipboard contains large strings of text. The default limit is 100000 characters.
Notes:
• Confirmations won't be requested when a message box of NVDA is still opened. In those cases, actions will be inmediately performed.
• Emulate copy and emulate cut commands mean that, when these features are enabled, the add-on will take control of control+c and control+x. This will allow to select if a confirmation should be requested before performing the actions corresponding to these keystrokes.
Changes for 15.0
• The command to add text to clipboard is again presented in the input gestures dialog.
• Fixed gestures to copy and cut with Persian keyboard, thanks to Mohammadhosein Ghezelsofla.
Changes for 14.0
• Compatible with NVDA 2021.1.
Changes for 13.0
• Fixed an issue in visual layout of the settings panel, thanks to Cyrille Bougot.
• Improved documentation.
• Added a Clip Contents Designer category to assign input gestures to all commands available for this add-on.
• Fixed bugs when using emulate copy in browsers if focus mode is active.
• You can assign different gestures to show the clipboard textual contents as raw text or formatted in HTML. The Format to show the clipboard text in the settings panel has being modified accordingly, to select the two options available for HTML format.
Changes for 12.0
• Fixed bugs when using emulate copy in applications like LibreOffice Writer.
Changes for 11.0
• Now it's possible to add text marked with the review cursor using standard commands of NVDA (NVDA+f9 and NVDA+f10). NVDA+windows+f9 is no longer used, for a better integration with the new NVDA+shift+f9 command.
• Requires NVDA 2019.3 or later.
Changes for 10.0
• Fixed a bug in the dialog used to show the clipboard text, when its title contains non latin characters.
• Fixed a bug when using the emulate cut and copy features with an Arabic keyboard layout. This has been fixed by Abdel, added as an add-on author.
Changes for 9.0
• Added the possibility of showing the clipboard text in browse mode.
• Added an option to choose if confirmations will be required if clipboard is not empty, for instance, if files or folders are been copied.
• Requires NVDA 2018.4 or later.
Changes for 8.0
• The add-on settings are shown in the corresponding category of the NVDA Settings dialog.
• Requires NVDA 2018.2 or later.
• If needed, you can download the last version compatible with NVDA 2017.3.
Changes for 7.0
• In the dialog to configure the Emulate copy and Emulate cut functionalities at installation, if you choose no, the commands for these features will be removed, so that you can restore the normal behavior for control+c and control+x.
Changes for 6.0
• Added options to choose if available actions should be performed after confirmation.
• Added Emulate copy and Emulate cut commands, which could be assigned from the Input gestures dialog.
• Added a dialog to configure the Emulate copy and Emulate cut functionalities at installation. This allows to add the control+c and control+x commands to copy and cut, and be asked if you want to replace the clipboard contents when pressing these keystrokes.
• Fixed documentation for script_add (Windows+NVDA+c).
Changes for 5.0
• The visual presentation of the dialog has been enhanced, adhering to the appearance of the dialogs shown in NVDA.
• Requires NVDA 2016.4 or later.
Changes for 4.0
• Add-on settings are managed from NVDA configuration, so that standard profiles can be used to save different separators, and it's not needed to copy the settings for importing at reinstallation.
• Now it's possible to choose if the added text will be appended or prepended, using the Add text before clip data check box from the Clip Contents Designer settings dialog.""", "https://addons.nvda-project.org/files/get.php?file=ccd"],
	"Enhanced Touch Gestures":["2021.2 +", """This add-on provides additional touchscreen gestures for NVDA. It also provides a set of gestures for easier browse mode navigation.
Note: this add-on requires NVDA 2021.2 or later running on a touchscreen computer with Windows 8.1, 10 or 11.
Commands
Available everywhere
• 4 finger double tap: toggle input help mode.
• Four finger flick right: toggle touch keyboard (usually enables it).
• Four finger flick left: toggle dictation (Windows+H; Windows 10 Version 1709 or later).
Object mode
• 3 finger flick down: read current window.
• 3 finger flick left: report object with focus.
• 3 finger flick right: report current navigator object.
• 4 finger flick up: report title of the current window.
• 4 finger flick down: report status bar text.
Web touch mode
This touch mode, available in browse mode, allows you to navigate the document by selected element. To switch to web mode, from browse mode documents, perform 3 finger tap. From this mode, flicking up or down with one finger cycles through available element navigation modes, while flicking right or left with one finger moves to next or previous chosen element, respectively. Once you move away from browse mode documents, object touch mode is used.
Synth settings touch mode
You can use this mode to quickly change synthesizer settings such as choosing a voice and changing volume. In this mode, use two finger flick left or right to move between synth settings and use two finger flick up and down gestures to change values. This gestures mirrors that of synth settings ring commands on the keyboard.
Version 21.10
• NVDA 2021.2 or later is required due to changes to NVDA that affects this add-on.
Version 21.08
• Initial support for Windows 11.
Version 21.01
• NVDA 2020.3 or later is required.
• On Windows 10 Version 1709 and later, doing a four finger flick left will toggle dictation (Windows+H).
• Remove dedicated touch interaction support toggle command from the add-on.
• As touch interaction support can be toggled from NVDA's touch interaction settings panel, a dedicated Enhanced Touch Gestures settings panel has been removed.
Version 20.09
• Removed ability to let NVDA turn off touch interaction for up to ten seconds (touch command passthrough).
• Removed coordinate announcement beep feature.
Version 20.07
• Added a keyboard command to toggle touch interaction or enable/disable touch passthrough (Control+Alt+NVDA+T).
• As NVDA 2020.1 and later includes a touch command to perform right mouse click (one finger tap and hold), the command has been removed from this add-on. AS a result, NVDA 2020.1 or later is required.
• The ability to let NVDA turn off touch interaction for up to ten seconds (touch command passthrough) is deprecated. In the future this feature will toggle touch interaction instead.
• In NVDA development snapshots, due to touch interaction feature changes, touch command passthrough feature and Enhanced Touch Gestures settings panel will be disabled. The command used to enable touch command passthrough will toggle touch interaction instead.
• Coordinate announcement beep feature is deprecated and will be removed in a future add-on release.
• Coordinate announcement beep will not be heard while using touch keyboard.
• NVDA will no longer appear to do nothing or play error tones while exploring modern input facility such as emoji panel via touch.
• NVDA will present an error message if touch keyboard cannot be activated (four finger flick right).
Version 20.06
• Resolved many coding style issues and potential bugs with Flake8.
Version 20.04
• Right mouse click gesture (one finger tap and hold) is now part of NVDA 2020.1.
Version 20.01
• NVDA 2019.3 or later is required.
• Touch support toggle command (including touch passthrough) will no longer function if touch support is turned off completely.
Version 19.11
• Added input help messages for additional touch commands.
Version 19.09
• Touch support can now be disabled from everywhere, not just from profiles other than normal profile.
Version 19.07
• Internal changes to support future NVDA releases.
Version 18.12
• Internal changes to support future NVDA releases.
Version 18.08
• Compatible with NVDA 2018.3 and future versions.
Version 18.06
• Add-on settings is now found in new multi-category NVDA Settings screen under "Enhanced Touch Gestures" category. As a result, NVDA 2018.2 is required.
• Fixed compatibility issues with wxPython 4.
Version 18.04
• Resolves an issue where touch interaction category in NVDA Settings panel may cause error sounds to be heard due to changes made from this add-on.
Version 18.03
• NVDA 2018.1 is required.
• Because NVDA 2018.1 comes with touch typing checkbox, the checkbox is no longer included in this add-on.
Version 17.12
• Requires NVDA 2017.4. Specifically, this add-on can now handle configuration profile switches.
• As NVDA 2017.4 includes screen orientation announcement, this feature is no longer part of this add-on.
• Added a hidden checkbox in Touch Interaction dialog to completely disable touch support (available if profiles other than normal configuration is active).
• If using NVDA 2018.1 or later, Touch Interaction dialog will be listed twice under NVDA's preferences menu. The second item is the dialog that comes with the add-on.
• In Touch Interaction dialog for the add-on, touch typing mode is no longer shown if using NVDA 2018.1 or later.
Version 17.10
• Due to support policy from Microsoft, Windows 8 (original release) is no longer supported.
• NVDA will no longer announce screen orientation twice when running NVDA 2017.4 development snapshots.
Version 17.07.1
• Added an option in touch interaction dialog to manually toggle touch passthrough without use of a timer.
• With manual passthrough mode off, if touch passthrough is turned on before the passthrough duration expires, touch interaction would be enabled.
Version 17.07
• Added a new dialog named Touch Interaction under NVDA's preferences menu to configure how NVDA works with touchscreens.
• After installing this version, when pressing keys on the touch keyboard, one must double tap the desired key. You can switch back to the old way by enabling touch typing from Touch Interaction dialog.
• Added a command (unassigned) to allow NVDA to ignore touch gestures for up to 10 seconds.
• Added an option in Touch Interaction dialog to allow NVDA to pause touch interaction between 3 to 10 seconds in order to perform touchscreen gestures directly (as though NVDA is not running; default is 5 seconds).
• Added debug logging messages when performing right clicks (tap and hold) to be recorded in the NVDA log (requires NVDA 2017.1 or later).
• Due to changes made when playing screen coordinates, NVDA 2017.1 or later is required.
Version 17.03
• Fixed an issue where coordinate announcement beep did not play or an error tone played instead when using NVDA 2017.1 or later.
Version 16.12
• Web touch mode works in Microsoft Edge, Microsoft Word and others where browse mode is used.
• Added lists and landmarks to web touch mode elements.
Version 16.06
• Initial stable version.""", "https://addons.nvda-project.org/files/get.php?file=ets"],
	"NV Speech Player. A Klatt-based speech synthesis engine written in c++":["2019.3 +", """NV Speech Player is a free and open-source prototype speech synthesizer that can be used by NVDA. It generates speech using Klatt synthesis, making it somewhat similar to speech synthesizers such as Dectalk and Eloquence.
Licence and copyright
NV Speech Player is Copyright (c) 2014 NV Speech Player contributors NV Speech Player is covered by the GNU General Public License (Version 2). You are free to share or change this software in any way you like as long as it is accompanied by the license and you make all source code available to anyone who wants it. This applies to both original and modified copies of this software, plus any derivative works. For further details, you can view the license online at: http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
Background
The 70s and 80s saw much research in speech synthesis. One of the most prominent synthesis models that appeared was a formant-frequency synthesis known as Klatt synthesis. Some well-known Klatt synthesizers are Dectalk and Eloquence. They are well suited for use by the blind as they are extremely responsive, their pronunciation is smooth and predictable, and they are small in memory footprint. However, research soon moved onto other forms of synthesis such as concatinative speech, as although this was slower, it was much closer to the human voice. This was an advantage for usage in mainstream applications such as GPS units or telephone systems, but not necessarily so much of an advantage to the blind, who tend to care more about responsiveness and predictability over prettiness.
Although synthesizers such as Dectalk and Eloquence continued to be maintained and available for nearly 20 years, now they are becoming harder to get, with multiple companies saying that these, and their variants, have been end-of-lifed and will not be updated anymore.
Concatinative synthesis is now starting to show promise as a replacement as the responsiveness and smoothness is improving. However, most if not all of the acceptable quality synthesizers are commercial and are rather expensive.
Both Dectalk and Eloquence were closed-source commercial products themselves. However, there is a substantial amount of source code and research material on Klatt synthesis available to the community. NV Speech Player tries to take advantage of this by being a modern prototype of a Klatt synthesizer, in the hopes to either be a replacement for synthesizers like Dectalk or Eloquence, or at least restart research and conversation around this synthesis method.
The eSpeak synthesizer, itself a free and open-source product has proved well as a replacement to a certain number of people in the community, but many people who hear it are extremely quick to point out its "metallic" sound and cannot seem to continue to use it. Although the authors of NV Speech Player still prefer eSpeak as their synthesizer of choice, they would still hope to try and understand better this strange resistance to eSpeak which may have something to do with eSpeak's spectral frequency synthesis verses Klatt synthesis. It may also have to do with the fact that consonants are also gathered from recorded speech and can therefore be perceived as being injected into the speech stream.
Implementation
The synthesis engine itself is written in C++ using modern idioms, but closely following the implementation of klsyn-88, found at http://linguistics.berkeley.edu/phonlab/resources/
eSpeak is used to parse text into phonemes represented in IPA, making use of existing eSpeak dictionary processing. eSpeak can be found at: http://espeak.sourceforge.net/
The Klatt formant data for each individual phoneme was collected mostly from a project called PyKlatt: http://code.google.com/p/pyklatt/ However it has been further tweaked based on testing and matching with eSpeak's own data.
The rules for phoneme lengths, gaps, speed and intonation have been coded by hand in Python, though eSpeak's own intonation data was tried to be copied as much as possible.
Building NV Speech Player
You will need: - Python 3.7: http://www.python.org - SCons 3: http://www.scons.org/ - Visual Studio 2019 Community
To build: run scons
After building, there will be a nvSpeechPlayer_xxx.nvda-addon file in the root directory, where xxx is the git revision or hardcoded version number. Installing this add-on into NVDA will allow you to use the Speech Player synthesizer in NVDA. Note everything you need is in the add-on, no extra dlls or files need to be copied.""", "https://addons.nvda-project.org/files/get.php?file=nvsp"],
	"Quick Books 2014 support":["unknown", """This add-on makes it possible to use NVDA with the Intuit Quickbooks 2014 accounting software.
Features
• Automatic enabling of QuickBooks accessibility mode.
• Labeling of many input fields.
• Tracking of focus and highlighting for lists such as the Chart of Accounts.
• Correct control type identification of custom check boxes, radio buttons and buttons.
• Automatic reporting of messages in custom message dialogs.""", "https://addons.nvda-project.org/files/get.php?file=qb-dev"],
	"TeamViewer":["unknown", """This add-on improves accessibility of TeamViewer with NVDA.
It's based on TeamViewerNVDASupport add-on, developed by the same author. You should uninstall that old add-on to use this one, since both have common keystrokes and features.
Tested on TeamViewer 9, trial version.
Key Commands:
• nvda+shift+C: Copies the ID and current password to the clipboard, so that they can be pasted and sent via chat for example when remote control is required.
• control+tab and control+shift+tab: Switch to other tab in the TeamViewer main dialog.
Changes for 2.0
• Add-on help is available from the Add-ons Manager.""", "https://addons.nvda-project.org/files/get.php?file=tv"],
	"Bit Che":["unknown", """Bit Che is a simple tool that quickly searches popular bit torrent sites for files. You can get more information about this program at this page.
This NVDA addon improves the accessibility of the software. It adds the following features:
• Makes the search results list accessible.
• Enables you to use the Application key to activate the context menu on the focused result.
Notes
• You can use the up and down arrow keys to focus the search result which should be interacted with.
• When the first search performed after starting Bit Che is finished, the first result will be focused, though it may not be selected properly. NVDA will speak the selected result. Use the usual commands or the arrow keys to ensure the right item is selected before performing other actions.
Key Commands
• Application key, or shift+f10, open context menu for search result item.""", "https://addons.nvda-project.org/files/get.php?file=bc"],
	"Read Feeds":["2019.3 +", """This addon provides a straightforward way to read feeds in Atom or RSS formats using NVDA. The feeds will not be refreshed automatically. Below when we mention feeds, we mean both RSS and ATOM feeds.
Installation or Update
If you used a previous version of this addon, and there is an RSS or personalFeeds folder in your personal NVDA configuration folder, when installing the current version, a dialog will ask if you want to upgrade or install. Choose update to preserve your saved feeds and to continue using them in the new installed version of readFeeds.
Commands
Read Feeds menu
You can access the Read Feeds submenu from the nvda menu, Tools submenu, where the following menu options are available:
Feeds
Opens a dialog with the following controls:
• Filter by: An edit box to search previously saved feeds.
• A list of the saved feeds, focused when the dialog is opened.
• List of articles: Opens a dialog which presents the articles list from your current feed. Select the article you want to read and press Enter or Open web page of selected article button to open the corresponding page in your browser. Press About article button to open a dialog showing title and link of the selected article; from this dialog, you'll be able to copy this info to the clipboard.
• Open feed: Opens the selected feed in the default application.
• Open feed as HTML: Opens the selected feed in the default web browser. You will be able to show or hide publication dates and buttons to copy information about articles to clipboard.
• Copy feed address: Opens a dialog to confirm if you want to copy the feed address to clipboard.
• New: Opens a dialog with an edit box to enter the address of a new feed. If the address is valid and the feed can be saved, its name, based on the feed title, will appear at the bottom of the feeds list.
• Rename: Opens a dialog with an edit box to rename the selected feed.
• Delete: Opens a dialog to delete the selected feed after confirmation.
• Set default: Sets the selected feed as the default, so that its articles can be accessed with NVDA's gestures.
• Open folder containing a backup of feeds: Opens a folder which may contain a backup of feeds. This can be useful to explore and delete feeds which shouldn't be imported when the add-on is updated.
• Preferences: Opens the settings dialog for readFeeds, also available in NVDA's menu, Preferences, settings, readFeeds category.
• Close: Closes the Feeds dialog.
Notes
• If a feed named tempFeed is created, please rename it, as this file could be replaced when needed to create a feed whose name already exists.
• The feed set as the default can't be removed. The addressFile feed will be use as the default when the configuration is reset, so it can't be deleted.
• The Filter by edit box can be placed after the Open article button from NVDA's menu, Preferences, Settings, Read feeds category, or pressing the Preferences button of the Feeds dialog.
Copy feeds folder
Opens a dialog to choose a folder where you can save the personalFeeds directory of your feeds. By default the selected folder is the NVDA's configuration directory, which will create the personalFeeds directory.
Restore feeds
Opens a dialog to select a folder which replaces your feeds in the personalFeeds folder. Make sure you load a folder containing feeds URLs.
Keyboard commands
• Ctrl+Shift+NVDA+Space: Announces current article's URL. Pressing twice will open the web page.
• Ctrl+Shift+NVDA+8: Refreshes the selected feed and announces its most recent title.
• Ctrl+Shift+NVDA+I: Announces current feed title and link. Pressing twice will copy the title and related link to clipboard.
• Ctrl+Shift+NVDA+U: Announces previous feed title.
• Ctrl+Shift+NVDA+O: Announces next feed title.
Notifications
• When the title or URL have been copied.
• When unable to connect/refresh a feed, or the URL does not correspond to a valid feed.
• NVDA will display an error message if it was not possible to backup or restore the personalFeeds folder, and if a new feed cannot be created.
• The title of the articles list dialog displays the selected feed name and number of items available.""", "https://addons.nvda-project.org/files/get.php?file=rf"],
	"GoldWave":["2021.2 +", """This app module enhances access and usage of GoldWave audio editor.
Shortcuts
• NVDA+Shift+C: Toggles speaking of commands during audio editing.
• Control+Shift+P: Announces current track position.
• NVDA+Shift+R: Announces remaining time for the currently editing track.
• Control+NVDA+1: Announces the channel you are editing.
• Control+NVDA+2: Announces the total length of the audio file.
• Control+NVDA+3: announces a summary on audio selection information.
• Control+NVDA+4: Announces the zoom level.""", "https://addons.nvda-project.org/files/get.php?file=gwv"],
	"Emoticons":["2019.3 +", """Using this add-on, spoken text containing emoticon characters will be replaced by its more human friendly description.
For example: the sequence ":)" will be spoken as "smiling smiley", or for example NVDA will recognize the meaning of each emoji.
You can take advantage of the following features:
Insert Emoticon
Sometimes an image is worth a 1000 words: use the new emoji to liven up your instant message and to let your friends know how you’re feeling.
When you are unsure of the characters for a particular smiley, this addon enables you to select and insert it into your text such as in a chat.
Press NVDA+I, or from menu Tools -> Emoticons > Insert emoticon, to open a dialog with the provided emoticons or emoji.
This dialog allows you to choose an emoticon and to view the emoticons that interest you:
• An editable field allows you to filter the search for the desired emoticon among the emoticons available.
• Through a set of radio buttons, you can choose to view only emoji category (alt+E) or view only standard emoticon category (alt+s) or view all emoticons available (alt+A).
• In the list of emoticons (alt+L) are displayed on three columns respectively: the name of emoticon, the type of emoticon (standard emoticon or emoji), the corresponding character.
When you press OK, the characters for the chosen emoticon will be copied to your clipboard, ready for pasting.
Insert symbol
This dialog allows you to choose one of the symbols available in the Punctuation/symbol pronunciation dialog of NVDA. You can use the Filter edit box or the arrow keys to select an item from the symbols list. Then, press OK and the selected emoji or symbol will be copied to your clipboard, ready for pasting.
Emoticons dictionary
Emoticons add-on allows to have differents speech-dictionaries using configuration profiles.
This means that you can create or edit a specific speech-dictionary for each your custom profile.
From NVDA MENU, Preferences -> Speech dictionaries -> Emoticons dictionary, you can open a dialog to add or to edit available emoticons.
Saving your customizations, the new reading settings of emoticons will only apply to the profile you are currently editing.
For example, you may wish that NVDA spoken custom emoticons only in XxChat program, but not in other chat programs: you can do this by creating a profile for the XxChat application and assign to it a speech dictionary from Speech dictionaries menu, Emoticons dictionary option. See below for Emoticons settings in relation to the configuration profiles.
You can also export each custom speech-dictionary pressing "Save and export dictionary" button: in this way your speech-dictionaries will be saved in your user config folder, speechDicts/emoticons subfolder.
The exact name and location of the dictionary file will be based on the editing configuration profile, which will be shown in the title of the Emoticons dictionary dialog.
Emoticons settings
From menu Preferences -> Settings -> Emoticons opens a panel to configure the activation of your speech-dictionaries for each profile.
In Emoticons settings panel you can choose whether or not speech-dictionary should automatically activate when NVDA switches to the profile you are currently editing. By default it is disabled in normal configuration of NVDA and in all your new profiles.
Moreover, it's possible to determine if the add-on emojis should be spoken. This could be useful to preserve symbols speaking if emojis are included in NVDA's configuration.
If you may wish to keep clean your configuration folders, in this dialog it is also possible to choose if dictionaries not used (associated with non existing profiles) will be removed from the add-on when it is unloaded.
Key Commands:
These are the key commands available by default, you can edit those or add new key to open Emoticons settings panel or Emoticon Dictionary dialog:
• NVDA+E: speaking emoticons on/off, toggles between speaking text as it is written, or with the emoticons replaced by the human description.
• NVDA+I: show a dialog to select an emoticon you want to copy.
• Not assigned: show a dialog to select an NVDA's symbol you want to copy.
• Not assigned: open a browseable message showing the symbol where the review cursor is positioned, so that the whole description can be reviewed in browse mode.
• Not assigned: open a browseable message showing the symbol where the caret is positioned, so that the whole description can be reviewed in browse mode.
Note: On Windows 10, it's also possible to use the built-in emoji panel.""", "https://addons.nvda-project.org/files/get.php?file=emo"],
	"eMule":["2019.3 +", """This add-on helps to improve accessibility of eMule with nVDA. It also provides additional keyboard commands for moving in different windows and gives Useful information about eMule.
It's based on the eMuleNVDASupport add-on, developed by the same author. You should uninstall that old add-on to use this one, since both have common keystrokes and features.
Tested on eMule 0.50a.
Key Commands:
• control+shift+h: Moves focus and mouse to main toolbar.
• control+shift+t: Reads the current window.
• control+shift+n: Moves the focus to the Name field in the Find window.
• control+shift+p: In the Search window, moves focus and mouse to the list of search parameters, or edit field options.
• control+shift+b: Move the focus to the list in the current window. For example usable in the Search window, downloads in Transfer window, etc.
• control+shift+o: Move the focus to read-only edit boxes in the current window. For example the IRC received messages, available Servers, etc.
• control+NVDA+f: If the caret is located in a read only edit box, opens a find dialog to use the commands for searching text available in NVDA.
• control+shift+l: Moves the navigator object and mouse to the headers of the current list.
• control+shift+q: Reads the first object in the status bar; provides information about recent activity.
• control+shift+w: Reads the second object of the status bar; contains information about files and users on the current server.
• control+shift+e: Reads the third object of the status bar; useful to know the UpLoad/DownLoad speed.
• control+shift+r: Reads The fourth object of the status bar; reports on connecting of eD2K and Kad network.
Managing columns.
When within a list, you can move the caret between the rows and columns using alt+control+ Arrows. In this Add-on the following key commands are also available:
• nvda+control+1-0: Reads the first 10 columns.
• nvda+shift+1-0: Reads columns 11 to 20.
• nvda+shift+C: Copies the contents of the last read column to the clipboard.""", "https://addons.nvda-project.org/files/get.php?file=em"],
	"Focus Highlight":["unknown", """By drawing a colored rectangle, this addon enables partially sighted users, sighted educators, or developers to track the location of the nvda navigator object and the focused object/control.
The following colors are used by this addon:
• Green thin dashed-dotted line rectangle shows NVDA is in browse mode, and this is the navigator object.
• Red thin rectangle shows NVDA is in browse mode, and this is the focused object/control.
• Red thick rectangle shows NVDA is in browse mode, and this is both the navigator object and the focused object which are overlapping.
• Blue thick dotted line rectangle indicates NVDA is in focus mode, i.e., key types are passed to the control.
To toggle object tracking, press NVDA+Alt+P. You can assign other gestures using the Input Gestures dialog. Note that it works with NVDA 2018.3 or later. Otherwise, you should disable or uninstall the addon itself for disabling object tracking.
When Focus Highlight category of NVDA Settings dialog is available, following items can be used.
• Make focus mode the default: This checkbox is enabled by default. When it is unchecked, this add-on behaves same as version 5.6 or previous versions, i.e., if browse mode is not available for an app, the focus is shown using the thick red rectangle.
• 
Focus in focus mode, Focus in browse mode, Navigator object: Each of these groups contains Color, Thickness, and Style.
• Color: This edit field allows you to type the HTML color code, i.e., six-character hexadecimal number. For example, "ffffff" is white, "ff0000" is red, and so on. Note that "000000" can not be used.
• Thickness: This edit field allows you to type the thickness of the box. You can enter a value between 1 and 30.
• Style: The choices are Solid, Dash, Dot, Dash dot, and Dash dot-dot.
• 
Restore defaults: This button allows you to reset your settings to their original defaults.""", "https://addons.nvda-project.org/files/get.php?file=fh"],
	"NoBeepsSpeechMode":["unknown", "This add-on excludes beeps in the speech mode when pressing NVDA+s. You can only toggle between off or talk.", "https://addons.nvda-project.org/files/get.php?file=nb"],
	"Virtual Review":["2019.3 and beyond", """This Addon allows NVDA users to review a Window content in a text box, similar to window virtualization of JAWS for Windows. Note, however, that this is just a convenience for users and does not replace NVDA's excellent review modes and object navigation support.
Usage
Press NVDA+control+w to open the virtual revision Window. Then simply navigate the shown textbox as you do in any other text content. You can press Escape to close the virtual revision window.""", "https://addons.nvda-project.org/files/get.php?file=VR"],
	"placeMarkers":["2021.1 +", """This addon is used for saving and searching specific text strings or bookmarks. It can be used  on web pages or documents in NVDA's browse mode. It can also be used for saving or searching strings of text in multi-line controls; in this case, if it's not possible to update the caret, the corresponding string will be copied to the clipboard, so that it can be searched using other tools. The plugin saves the specified strings and bookmarks to files whose name is based on the title and URL of the current document. This addon is based on SpecificSearch and Bookmark&Search, developed by the same author. You should uninstall them to use this one, since they have common keystrokes and features.
Key Commands:
• control+shift+NVDA+f: Opens a dialog with an edit box that shows the last saved search; in this dialog you can also select the previously saved searches from a combo box or remove the selected string from the history using a checkbox. You can choose if the text contained in the edit box will be added to the history of your saved texts. Finally, choose an action from the next group of radio buttons (between Search next, Search previous or Don't search), and specify if NVDA will make a case sensitive search. When you press okay, NVDA will search for this string.
• control+shift+NVDA+k: Saves the current position as a bookmark. If you want to provide a name for this bookmark, select some text from this position before saving it.
• control+shift+NVDA+delete: Deletes the bookmark corresponding to this position.
• NVDA+k: Moves to the next bookmark.
• shift+NVDA+k: Moves to the previous bookmark.
• Not assigned: Shows the file name where the place markers data will be saved in browse mode, without an extension.
• alt+NVDA+k: Opens a dialog with the bookmarks saved for this document. You can write a note for each bookmark; press Save note to save changes. Pressing Delete you can remove the selected bookmark. Pressing OK you can move to the selected position.
• Not assigned: Saves a position as a temporary bookmark.
• Not assigned: Moves to the temporary bookmark for the current document.
• Not assigned: Finds the next occurrence of the last text searched for any specific document.
• Not assigned: Finds the previous occurrence of the last text searched for any specific document.
Place markers Submenu (NVDA+N)
Using the Place markers submenu under NVDA's Preferences menu, you can access:
• Specific search folder: opens a folder of specific searches previously saved.
• Bookmarks folder: Opens a folder of the saved bookmarks.
• Copy placeMarkers folder: You can save a copy of the bookmarks folder.
• Restore placeMarkers: You can restore your bookmarks from a previously saved placeMarkers folder.
Note: The bookmark position is based on the number of characters; and therefore in dynamic pages it is better to use the specific search, not bookmarks.""", "https://addons.nvda-project.org/files/get.php?file=pm"],
	"control Usage Assistant":["2021.2 +", "Use this add-on to find out how to interact with the focused control. Press NVDA+H to obtain a short help message on interacting with the focused control, such as checkboxes, edit fields and so on.", "https://addons.nvda-project.org/files/get.php?file=cua"],
	"Resource Monitor":["2021.2 +", """This add-on gives information about CPU load, memory usage and other resource usage information.
Shortcuts
• NVDA+Shift+E: presents used ram, average processor load, and battery info if available.
• NVDA+Shift+1: presents the average processor load and if multicore CPU's are present the load of each core.
• NVDA+Shift+2/5: presents the used and total space for both physical and virtual ram.
• NVDA+Shift+3: presents the used and total space of the static and removable drives.
• NVDA+Shift+4: presents battery percentage, charging status, remaining time (if not charging), and a warning if the battery is low or critical.
• NVDA+Shift+6: presents CPU Architecture 32/64-bit and Windows version and service pack numbers.
• NVDA+Shift+7: presents the system's uptime.
If you have NVDA 2013.3 or later installed, you can change these shortcut keys via input gestures dialog.
Usage notes
This add-on does not replace task manager and other system information programs for Windows. Also note the following:
• CPU usage is given for logical processors, not physical cores. This is noticeable for processors which uses Hyper-Threading where number of CPU's is twice the number of CPU cores.
• If there is heavy disk activity such as copying large files, there might be delays when obtaining disk usage information.
• This add-on requires Windows 7 Service Pack 1 or later.
Note on license: this add-on uses Psutil, licensed under 3-Clause BSD License which is compatible with GNU General Public License.""", "https://addons.nvda-project.org/files/get.php?file=rm"],
	"UnicodeBrailleInput":["unknown", """This add-on allows you to convert text from braille (E.G. 1345-1236-145-1) to Unicode braille characters. You can also convert text according to the currently selected input braille table.
The purpose of this specialized addon is to make it easier to help to improve liblouis tables and to add automatic tests for your language. With the addition of unicode braille table in NVDA 2017.3, this add-on is no longer required for this, as users can choose to input braille with the new table. However, this add-on can still aid in converting normal text to unicode braille according to a particular input table.
Usage
• Open a unicode aware text editor (for example Notepad++).
• Press NVDA+Ctrl+U or choose Unicode Braille Input found under NVDA tools menu.
• Select whether your input consists of braille dots (e.g. 1345-1236-145-1) or normal text according to the current braille table (e.g. Dutch (Netherlands).
• Type your braille text in numeric form or your normal text, respectively.
• Press OK.
• The required unicode characters will be copied to your clipboard ready for you to paste.""", "https://addons.nvda-project.org/files/get.php?file=ubi"],
	"instantTranslate":["unknown", """This add-on is used to translate selected and/or clipboard text from one language to another. This is done using the Google Translate service.
Configuring languages
To configure source, target and in case swap language, go to: NVDA Menu >> Preferences >> Instant Translate Settings.
There are two comboboxes labeled "Source language" and "Target language", and a checkbox to decide if it must copy the translation to clipboard.
In addition, if you selected auto option (the first choice) from "Source language" combobox, there are also a combobox labeled "Language for swapping" and a checkbox about the auto-swap.
The meaning of two first comboboxes and checkbox for copy is clear, but some words about the rest are necessary. Remember always that the explanations below assume the source language set on the auto option.
The "Language for swapping" combobox is useful when you swap via script (see below) the source and target language; in fact, a target language set on the auto option has no sense, so the addon sets it to value of combobox above.
So, imagine this situation: you usually translate into English (your main language), but sometimes (for example, when you write a document) you need to translate into Italian (your second language, suppose); you can set "Language for swapping" combobox to Italian, so you will translate from English to Italian without accessing directly to the addon settings. Obviously this function has a major or minor utility according to your more frequent needs.
Now, the auto-swap checkbox: it appears if and only if you set the auto option in "Source language" combobox, and is directly connected with "Language for swapping" combobox. If you activate it, then the addon tries to commute automatically from your source and target configuration to a configuration where target becomes the source language, and language selected in "Language for swapping" combobox is the new target language; extremely useful if the source language of the text you want translate is the target language.
A simple example: take again in mind the situation imagined previously; if you translate a text in a language different from English, there is no problem, you get the correct translation in English. But if you need to translate a text from English, normally you get a translation into English identical to original text, and this is a bit useless. Thanks to auto-swap function, however, assuming that you want to know how your text sounds into Italian, the addon commutes automatically the target language to Italian, so it returns a valid translation.
Anyway, this is a temporary configuration; if this option has no effect (it's experimental), try to commute manually to a stable configuration, using the gesture for swapping described below. It's experimental because in some situations (with short texts, typically), Google does not recognize the real source language correctly, and you have to swap languages manually via script, so to force the source language to be the previous target language (English in our example).
At least, in the speech settings parameters dialog (NVDA Menu >> Preferences >> Speech), you may want to check the "Automatic language switching (when supported)" option. This way, if you are using a multi-lingual synthesizer, the translation will be announced using the target language voice of the synthesizer.
Using
You can use this add-on in three ways:
1. Select some text using selection commands (shift with arrow keys, for example) and press associated key to translate. translation result will be read with synthesizer which you are using.
2. You can also translate text from the Clipboard.
3. Press the dedicated shortcut key to translate the last spoken text.
Shortcuts
All following commands must be pressed after modifier key "NVDA+Shift+t":
• T: Translate selected text,
• Shift+t: translate text from the Clipboard,
• S: swap source and target languages,
• A: announce current configuration,
• C: copy last result to clipboard,
• I: identify the language of selected text,
• L: translate the last spoken text,
• O: open translation settings dialog
• H: announces all available layered commands.""", "https://addons.nvda-project.org/files/get.php?file=it"],
	"dropbox":["2019.1 +", """This plugin add a shortcut to announce Dropbox status or open the Dropbox systray menu when pressed once or twice respectively. It also enhances DropBox item lists.
• Shortcut: NVDA+Alt+D
Changes for 4.6
• Specify NVDA 2021.1 compatibility
Changes for 4.4
• Python 3 compatibility
• Use the last addon template
• Repository change to be built with Appveyor
• Fixed wrong and removed unused shortcuts in the documentation
• Update the description in the documentation which still referenced the announcement of the version
Changes for 4.0
• Add-on help is available from the Add-ons Manager.
• The shortcut to get Dropbox status has been changed to Alt+NVDA+D to avoid conflict with audio ducking support.
Changes for 3.1
• Use another way to get cancel button and page tab. Now we don't have to focus them before using shortcuts.
• When changing the active tab, the focus move to the tab page so when pressing tab, the first item of the tab is activated instead of staying to the previous used tab even if it is not activated anymore.
• In the preferences dialog, it is now possible to press control+page up/down to switch between tabs. Control+tab and control+shift+tab still work.
• All localized manifest files should now be OK.
• Minor corrections.""", "https://addons.nvda-project.org/files/get.php?file=dx"],
	"Say Product Name and Version":["2017.3 +", """This NVDA add-on add a shortcut to announce product name and version of the foreground application, or copy these informations to the clipboard.
• Shortcut: NVDA+Shift+V
• Press it twice to copy product name and version to the clipboard.""", "https://addons.nvda-project.org/files/get.php?file=spnav"],
	"Speech History":["unknown", """An updated version of the Clip Copy add-on, initially created by Tyler Spivey.  The add-on allows you to review the most recent 100 items spoken by NVDA, as well as copy the selected item to the clipboard.  By default, use Shift+F11 to move back through the history, Shift+F12 to move forwards and F12 on its own to copy the selected item.  These hotkeys can be updated from within the Speech category of NVDA's Input gestures dialog.""", "https://addons.nvda-project.org/files/get.php?file=sps"],
	"Classic Selection":["unknown", """This addon reverts the behaviour of NVDA+f9 and NVDA+f10 that was introduced in NVDA 2016.3.
The old behaviour copies the selection to the clipboard on the first press of NVDA+f10, while the new one selects on the first press and copies on the second. The new behaviour has some disadvantages. Text can't be copied without being selected (and thus moving the cursor), where that's available. For places it's not (example the console), it adds an extra press of NVDA+f10.
The addon adds two new gestures under the Classic Selection category to start and end selection, which are bound to NVDA+f9 and NVDA+f10 by default.""", "https://addons.nvda-project.org/files/get.php?file=clsel"],
	"Switch synth":["unknown", """This addon allows easy switching of synthesizers via hotkeys. It is an improved version of my earlier switch_synth addon with an underscore, which must be uninstalled. Any preexisting synthesizer configurations will continue to work with this version.
There are 6 synthesizer slots, 1 through 6. By default, they are empty. Slots can be switched by pressing control+shift+NVDA+1 through control+shift+NVDA+6. Once a slot is switched to, its synthesizer and settings will be loaded if they exist. To save the current synthesizer and its settings to the currently active slot, press control+shift+NVDA+v.""", "https://addons.nvda-project.org/files/get.php?file=sws"],
	"NVDA Remote Support":["2019 +", "unknown", "https://nvdaremote.com/remote-2.4.nvda-addon"],
	"TeamTalk Classic":["unknown", "This add-on improves usage of TeamTalk with NVDA. ", "https://www.dlee.org/teamtalk/NVDA/TeamTalk%20Classic.nvda-addon"],
	"Easy Table Navigator":["2019.3 / 2021.1", """This plugin adds a layer command to use arrow keys to navigate table cells.
Currently supported tables are:
• Browse mode (Internet Explorer, Firefox, etc.).
• Microsoft Word.
Commands
• Toggles table navigator layer on and off (unassigned).""", "https://addons.nvda-project.org/files/get.php?file=etn"],
	"Newfon":["unknown", "Newfon is a synthesizer by Sergey Shishmintzev which supports the Russian and Ukrainian languages.", "https://www.nvaccess.org/files/nvda-addons/newfon.nvda-addon"],
	"OCR":["2019.3 and beyond", """Important: if you are using NVDA 2017.3 or later on Windows 10, please consider using built-in Windows 10 OCR.
Performs optical character recognition (OCR) to extract text from an object which is inaccessible. The Tesseract OCR engine is used. To perform OCR, move to the object in question using object navigation and press NVDA+r. You can set the OCR recognition language by going to the NVDA settings panel and selecting OCR settings. The keyboard shortcut can be reassigned from NVDA input gestures dialog in the "Miscellaneous" category.
Change log:
Changes for 2.1:
• When recognition is performed on an edit field it is now possible to navigate it with the system caret without moving focus from it and back again.
• Tesseract release info is no longer written to the focused console.
• When no text is recognized this fact is announced to the user.
• It is no longer possible to attempt recognition on an invisible object.
• WX is now used to capture images instead of Pillow.
Changes for 2.0:
• Compatibility with NVDA 2019.3 and later.
• It is possible to set different recognition languages for different configuration profiles.
• OCR settings can now be changed from NVDA settings dialog rather than from a separate dialog in the tools menu.""", "https://addons.nvda-project.org/files/get.php?file=ocr"],
	"Extended Winamp":["2020.1 and beyond", """This add-on extends the original Winamp app module found in NVDA with some extra functionality.
• S: toggle shuffle on/off
• R: toggle repeat on/off
• F5: mute playback
• F6: set playback volume to 25%
• F7: set playback volume to 50%
• F8: set playback volume to 100%
• Shift+Left arrow: pan Left
• Shift+Right arrow: pan Right
• Shift+Up arrow: pan Center
• Control+Shift+T: speaks total Track Length
• Control+Shift+E: speaks track Elapsed Time
• Control+Shift+R: speaks track Remaining Time
• Shift+R: Review the end of track "last 6 seconds by default"
• Control+R: Set the review time "in seconds" for use with Review End of Track command
• Shift+J: Set alternate jump time "in seconds"
• Control+Right arrow: alternate Jump Forward "6 seconds by default"
• Control+Left arrow: alternate Jump Backward "6 seconds by default"
Changes for 2.0
• Resolved many coding style issues and potential bugs with Flake8.
• Made compatible with NVDA 2021.1.
Changes for 1.2
• Updated Addon to work on NVDA 2019.3 and above.
• New languages: Croatian, Polish, Simplified Chinese.
Changes for 1.1
• New languages: Aragonese, Arabic, Dutch, German, Finnish, French, Galician, Hungarian, Italian, Japanese, Korean, Nepali, Portuguese (Brazil), Russian, Slovak, Slovenian, Spanish, Tamil, Turkish.
Changes for 1.0
• Initial Release""", "https://addons.nvda-project.org/files/get.php?file=ew"],
	"systrayList":["2019.3 and beyond", """This add-on allows you to read and activate icons on the system tray or the task bar, within a list box, for easy access and interaction to those items. With the add-on installed, press NVDA+f11 once for this dialog to pop-up with system tray elements, and press twice to display task bar elements, which are the currently running applications.
Note that you can access the windows system tray in any screen reader software using the Windows+B, and the task bar by pressing Windows+T. This plugin is only useful to make the transition from JAWS for Windows smoother and to avoid some tooltips that may pop-up when cycling through the system tray with the windows keyboard means.
Changes for 4.0 2020-01-03
• Requires NVDA 2019.3 or later.
• No more support for Windows versions earlier than Windows 7 Service Pack 1.
• Add-on has been renamed to "SysTrayList".
• Donation request dialog will no longer appear when installing or updating the add-on.
Changes for 3.2 2018-12-24
• More code changes to support Python 3.
Changes for 3.1 2018-11-24
• Internal changes to support future NVDA releases.
Changes for 3.0 2018-10-25
Support for Windows releases earlier than Windows 7 Service Pack 1 will end in 2019.
• Add-on is Python 3 compatible.
Changes for 2.0 2017-05-20
• Systray/taskbar dialog is now centered on screen.
• Fixed various user interface issues.
• New and updated translations.
Changes for 1.5 2015-mm-dd
• Corrected left/right click action.
• Add-on help is now available from add-ons manger.
• Translation updates.
Changes for 1.4 - 2013-01-19
• Requires NVDA 2012.3beta2 or greater.
• Add donation request to installation procedure
• Implemented taskbar support
• New translations: Arabic, Bulgarian, Dutch, Finnish, Galician, Greek, Hungarian, Italian, Japanese, Korean, Nepali, Norwegian, Polish, Brazilian Portuguese, Russian, Slovak, Tamil, Traditional Chinese Hong Kong.
Changes for 1.3 - 2012-05-25
• Converted to an add-on package
• French and Turkish Translations.
Changes for 1.2 - 2012-04.25
• Spanish and German translations. Thanks to all that contributed.
Changes for 1.1 - 2012-03-20
• Corrected a bug that was making it impossible to use the plugin when a gettext translation is not available
Changes for 1.0 - 2012-03-19
• Initial Release""", "https://addons.nvda-project.org/files/get.php?file=st"]
	}
# another dictionary for web pages for nvda addons, i made that because it's hard to edit the first dictionary and it take a long time to edit, so i made that, to do a function to add all links of pages to first dictionary.
dict2={
	"Sound Splitter":"https://addons.nvda-project.org/addons/soundSplitter.zh_CN.html",
	"Quick Notetaker":"https://addons.nvda-project.org/addons/quickNotetaker.\"lng\".html",
	"Ignore Blanks Indentation Reporting":"https://addons.nvda-project.org/addons/ignoreBlanksIndentationReporting.\"lng\".html",
	"Search With":"https://addons.nvda-project.org/addons/searchWith.\"lng\".html",
	"Event Tracker":"https://addons.nvda-project.org/addons/evtTracker.\"lng\".html",
	"PC Keyboard Braille Input for NVDA":"https://addons.nvda-project.org/addons/pcKbBrl.\"lng\".html",
	"Windows Magnifier":"https://addons.nvda-project.org/addons/winMag.\"lng\".html",
	"Direct Link":"https://addons.nvda-project.org/addons/directLink.\"lng\".html",
	"NVDA Unmute":"https://addons.nvda-project.org/addons/unmute.\"lng\".html",
	"Check Input Gestures":"https://addons.nvda-project.org/addons/checkGestures.\"lng\".html",
	"NVDAUpdate Channel Selector":"https://addons.nvda-project.org/addons/updateChannelSelector.\"lng\".html",
	"Proxy support for NVDA":"https://addons.nvda-project.org/addons/nvdaproxy.\"lng\".html",
	"WordNav":"https://addons.nvda-project.org/addons/wordNav.\"lng\".html",
	"Win Wizard":"https://addons.nvda-project.org/addons/winWizard.\"lng\".html",
	"Console Toolkit":"https://addons.nvda-project.org/addons/consoleToolkit.\"lng\".html",
	"Quick Dictionary":"https://addons.nvda-project.org/addons/quickDictionary.\"lng\".html",
	"Numpad Nav Mode":"https://addons.nvda-project.org/addons/numpadNavMode.\"lng\".html",
	"Zoom Accessibility Enhancements":"https://addons.nvda-project.org/addons/zoomEnhancements.\"lng\".html",
	"Kill NVDA":"https://addons.nvda-project.org/addons/killNVDA.\"lng\".html",
	"Time Zoner":"https://addons.nvda-project.org/addons/timeZoner.\"lng\".html",
	"Tony's enhancements":"https://addons.nvda-project.org/addons/tonysEnhancements.\"lng\".html",
	"Phonetic Punctuation":"https://addons.nvda-project.org/addons/phoneticPunctuation.\"lng\".html",
	"Percentage Checker":"https://addons.nvda-project.org/addons/percentageChecker.\"lng\".html",
	"Report Passwords":"https://addons.nvda-project.org/addons/reportPasswords.\"lng\".html",
	"Audio Themes":"https://addons.nvda-project.org/addons/AudioThemes.\"lng\".html",
	"Synth ring settings selector":"https://addons.nvda-project.org/addons/synthRingSettingsSelector.\"lng\".html",
	"Debug Helper":"https://addons.nvda-project.org/addons/debugHelper.\"lng\".html",
	"Notepad++":"https://addons.nvda-project.org/addons/notepadPlusPlus.\"lng\".html",
	"Beep Keyboard":"https://addons.nvda-project.org/addons/beepKeyboard.\"lng\".html",
	"Developer Toolkit":"https://addons.nvda-project.org/addons/developerToolkit.\"lng\".html",
	"Add-ons documentation":"https://addons.nvda-project.org/addons/addonsHelp.\"lng\".html",
	"Character Information":"https://addons.nvda-project.org/addons/charInfo.\"lng\".html",
	"Addon to count elements of selected text":"https://addons.nvda-project.org/addons/wordCount.\"lng\".html",
	"Online image describer":"https://addons.nvda-project.org/addons/onlineOCR.\"lng\".html",
	"Weather Plus":"https://addons.nvda-project.org/addons/Weather_Plus.\"lng\".html",
	"BrowserNav":"https://addons.nvda-project.org/addons/browsernav.\"lng\".html",
	"Outlook extended":"https://addons.nvda-project.org/addons/outlookExtended.\"lng\".html",
	"Training Keyboard commands":"https://addons.nvda-project.org/addons/trainingKeyboardCommands.\"lng\".html",
	"Columns Review":"https://addons.nvda-project.org/addons/columnsReview.\"lng\".html",
	"TextNav":"https://addons.nvda-project.org/addons/textnav.\"lng\".html",
	"AudioChart":"https://addons.nvda-project.org/addons/AudioChart.\"lng\".html",
	"BluetoothAudio":"https://addons.nvda-project.org/addons/BluetoothAudio.\"lng\".html",
	"Calibre":"https://addons.nvda-project.org/addons/calibre.\"lng\".html",
	"ToolbarsExplorer":"https://addons.nvda-project.org/addons/toolbarsExplorer.\"lng\".html",
	"Input Lock":"https://addons.nvda-project.org/addons/inputLock.\"lng\".html",
	"Add-on Updater":"https://addons.nvda-project.org/addons/addonUpdater.\"lng\".html",
	"Access8Math":"https://addons.nvda-project.org/addons/access8math.\"lng\".html",
	"Text Information":"https://addons.nvda-project.org/addons/textInformation.\"lng\".html",
	"SentenceNav":"https://addons.nvda-project.org/addons/sentenceNav.\"lng\".html",
	"BrailleExtender":"https://addons.nvda-project.org/addons/brailleExtender.\"lng\".html",
	"IndentNav":"https://addons.nvda-project.org/addons/indentNav.\"lng\".html",
	"Mozilla Apps Enhancements":"https://addons.nvda-project.org/addons/mozillaScripts.\"lng\".html",
	"sayCurrentKeyboardLanguage":"https://addons.nvda-project.org/addons/sayCurrentKeyboardLanguage.\"lng\".html",
	"Object Location Tones":"https://addons.nvda-project.org/addons/objLocationTones.\"lng\".html",
	"BGT Lullaby":"https://addons.nvda-project.org/addons/bgtLullaby.\"lng\".html",
	"Enhanced Aria":"https://addons.nvda-project.org/addons/enhancedAria.\"lng\".html",
	"Lambda Add-On for NVDA":"https://addons.nvda-project.org/addons/lambda.\"lng\".html",
	"Speak Passwords":"https://addons.nvda-project.org/addons/speakPasswords.\"lng\".html",
	"Clipspeak":"https://addons.nvda-project.org/addons/clipspeak.\"lng\".html",
	"Review Cursor Copier":"https://addons.nvda-project.org/addons/reviewCursorCopier.\"lng\".html",
	"Mush Client":"https://addons.nvda-project.org/addons/mushClient.\"lng\".html",
	"mIRC":"https://addons.nvda-project.org/addons/mirc.\"lng\".html",
	"ObjPad":"https://addons.nvda-project.org/addons/objPad.\"lng\".html",
	"Visual Studio":"https://addons.nvda-project.org/addons/visualStudio.\"lng\".html",
	"Report Symbols":"https://addons.nvda-project.org/addons/reportSymbols.\"lng\".html",
	"StationPlaylist":"https://addons.nvda-project.org/addons/stationPlaylist.\"lng\".html",
	"Tone Master":"https://addons.nvda-project.org/addons/toneMaster.\"lng\".html",
	"mp3DirectCut":"https://addons.nvda-project.org/addons/mp3DirectCut.\"lng\".html",
	"Crash Hero":"https://addons.nvda-project.org/addons/crashHero.\"lng\".html",
	"Tip of the Day":"https://addons.nvda-project.org/addons/tipOfTheDay.\"lng\".html",
	"SpeechPlayer in Espeak":"https://addons.nvda-project.org/addons/speechPlayerInEspeak.\"lng\".html",
	"Golden Cursor":"https://addons.nvda-project.org/addons/goldenCursor.\"lng\".html",
	"Day of the week":"https://addons.nvda-project.org/addons/dayOfTheWeek.\"lng\".html",
	"VLC Media Player":"https://addons.nvda-project.org/addons/vlc.\"lng\".html",
	"Windows App Essentials":"https://addons.nvda-project.org/addons/wintenApps.\"lng\".html",
	"Ventrilo":"https://addons.nvda-project.org/addons/ventrilo.\"lng\".html",
	"Easy Table Navigator":"https://addons.nvda-project.org/addons/easyTableNavigator.\"lng\".html",
	"Clock and calendar Add-on for NVDA":"https://addons.nvda-project.org/addons/clock.\"lng\".html",
	"Dual Voice":"https://addons.nvda-project.org/addons/dualvoice.\"lng\".html",
	"Clip Contents Designer":"https://addons.nvda-project.org/addons/clipContentsDesigner.\"lng\".html",
	"Enhanced Touch Gestures":"https://addons.nvda-project.org/addons/enhancedTouchGestures.\"lng\".html",
	"NV Speech Player. A Klatt-based speech synthesis engine written in c++":"https://addons.nvda-project.org/addons/nvSpeechPlayer.\"lng\".html",
	"Quick Books 2014 support":"https://addons.nvda-project.org/addons/quickBooks2014.\"lng\".html",
	"TeamViewer":"https://addons.nvda-project.org/addons/teamViewer.\"lng\".html",
	"Bit Che":"https://addons.nvda-project.org/addons/bitChe.\"lng\".html",
	"Read Feeds":"https://addons.nvda-project.org/addons/readFeeds.\"lng\".html",
	"GoldWave":"https://addons.nvda-project.org/addons/goldwave.\"lng\".html",
	"Emoticons":"https://addons.nvda-project.org/addons/emoticons.\"lng\".html",
	"eMule":"https://addons.nvda-project.org/addons/eMule.\"lng\".html",
	"Focus Highlight":"https://addons.nvda-project.org/addons/focusHighlight.\"lng\".html",
	"NoBeepsSpeechMode":"https://addons.nvda-project.org/addons/noBeepsSpeechMode.\"lng\".html",
	"Virtual Review":"https://addons.nvda-project.org/addons/virtualRevision.\"lng\".html",
	"placeMarkers":"https://addons.nvda-project.org/addons/placeMarkers.\"lng\".html",
	"control Usage Assistant":"https://addons.nvda-project.org/addons/controlUsageAssistant.\"lng\".html",
	"Resource Monitor":"https://addons.nvda-project.org/addons/resourceMonitor.\"lng\".html",
	"UnicodeBrailleInput":"https://addons.nvda-project.org/addons/unicodeBrailleInput.\"lng\".html",
	"instantTranslate":"https://addons.nvda-project.org/addons/instantTranslate.\"lng\".html",
	"dropbox":"https://addons.nvda-project.org/addons/dropbox.\"lng\".html",
	"Say Product Name and Version":"https://addons.nvda-project.org/addons/sayProductNameAndVersion.\"lng\".html",
	"Speech History":"https://addons.nvda-project.org/addons/speech_history.\"lng\".html",
	"Classic Selection":"https://addons.nvda-project.org/addons/classicSelection.\"lng\".html",
	"Switch synth":"https://addons.nvda-project.org/addons/switchSynth.\"lng\".html",
	"NVDA Remote Support":"https://addons.nvda-project.org/addons/nvdaremote.\"lng\".html",
	"TeamTalk Classic":"https://addons.nvda-project.org/addons/teamtalk.\"lng\".html",
	"Newfon":"https://addons.nvda-project.org/addons/newfon.\"lng\".html",
	"OCR":"https://addons.nvda-project.org/addons/ocr.\"lng\".html",
	"Extended Winamp":"https://addons.nvda-project.org/addons/extendedWinamp.\"lng\".html",
	"systrayList":"https://addons.nvda-project.org/addons/systrayList.\"lng\".html"
	}

print("adding links")
AddLinks()
print("links added successfuly")
print("making json object")
json_object=json.dumps(dict, indent=1)
print("building json object completed")
print("writing to file")
with open("addons/addons.json","w") as file:
	file.write(json_object)
print("completed")
