import json

def WriteJsonFile():
	ver=float(input("version:"))
	url=input("update url")
	print("getting description")
	f = open("description.txt", "r", encoding="utf-8")
	description=f.read()
	f.close
	print("getting changes")
	f=open("changes.txt", "r", encoding="utf-8")
	changes=f.read()
	f.close
	print("writing to dictionary")
	dict = {
		"version":ver,
		"url":url,
		"discription":description,
		"changes":changes
	}
	print("creating json object")
	json_object=json.dumps(dict, indent=4)
	print("writing to file")
	with open("info.json","w") as file:
		file.write(json_object)
		print("completed")
WriteJsonFile()