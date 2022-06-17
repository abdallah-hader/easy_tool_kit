import configparser
import os

spath=os.path.join(os.getenv("appdata"), "Easy Toolkit")
mp4Path=os.path.join(os.getenv("userprofile"), "Documents")
download_addons_path=os.path.join(os.getenv("userprofile"), "Documents")

defaults={
	"language":"en",
	"translatorsource":"arabic",
	"translatortarget":"english",
	"cfrom":None,
	"cto":None,
	"wikipedialang":"en",
	"city":None,
	"escapetoback":False,
	"hideclosebutton":False,
	"mp4path":mp4Path,
	"DownloadAddonsPath":download_addons_path,
	"confirmation_to_exit":True,
	"getcurrencyupdates":"False",
	"checkforupdatesatstartup":"True",
	"deltheitemdrawed":False
}

def s_to_b(what):
	if what=="True":
		return True
	elif what=="False":
		return False
	else:
		return what

def init_config():
	try:
		os.mkdir(spath)
	except FileExistsError:
		pass
	if not os.path.exists(os.path.join(spath, "settings.ini")):
		config=configparser.ConfigParser()
		config.add_section("settings")
		for k,v in defaults.items():
			config["settings"][k]=str(v)
		with open(os.path.join(spath, "settings.ini"),"w") as f:
			config.write(f)

def get(string):
	config=configparser.ConfigParser()
	try:
		config.read(os.path.join(spath, "settings.ini"))
		v=config["settings"][string]
		return s_to_b(v)
	except KeyError:
		new(string, defaults[string])
		return defaults[string]

def new(key, value):
	config = configparser.ConfigParser()
	try:
		config.read(os.path.join(spath, "settings.ini"))
		config["settings"][key] = str(value)
		with open(os.path.join(spath, "settings.ini"), "w") as f:
			config.write(f)
	except:
		pass