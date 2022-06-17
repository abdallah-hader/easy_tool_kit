import os
from settingsconfig import get
lang=get("language")

def help():
	try:
		os.startfile(os.path.join("docs", lang+"/doc.html"))
	except FileNotFoundError:
		os.startfile(os.path.join("docs", "en/doc.html"))
	except:
		pass
