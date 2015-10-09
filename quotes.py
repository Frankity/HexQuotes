__module_name__ = "Quotes Adder Plugin"
__module_version__ = "0.5"
__module_description__ = "Add quotes as you want."
__author__ = "Douglas Brunal (AKA) Frankity"

import hexchat
import os.path 
import sqlite3
from os.path import expanduser
import datetime 
from time import gmtime, strftime

addonsfolder = '"' + expanduser("~") + "\\appdata\\roaming\\hexchat\\addons\\" + '"';
addonsfolder1 = expanduser("~") + "\\appdata\\roaming\\hexchat\\addons\\";
db = "quotes.db";

def viewdb():
	if os.path.isfile(addonsfolder1.replace('s\\"','s\\') + db):
		print '\00302' + "[DEBUG] There is a database, will be used..."
	else:
		print '\00302' + "[DEBUG] There is not a database, will be created..."
		makedb();
	return;

def makedb():
	connection = sqlite3.connect(addonsfolder1 + 'quotes.db')
	f = connection.cursor()
	f.execute('''CREATE TABLE quotes (id INTEGER PRIMARY KEY AUTOINCREMENT, datetime TEXT, content TEXT)''')
	connection.commit()
	connection.close()
	print '\00302' + "[DEBUG] Database and tables created successfully"
	return;

def insertdata(word):
		con = sqlite3.connect(addonsfolder1 + 'quotes.db')
		d = con.cursor()
		d.execute("SELECT id FROM quotes")
		omg = len([int(record[0]) for record in d.fetchall()])
		finalword = str(word)
		f1 = finalword.replace("'","")
		f2 = f1.replace(",","")
		f3 = f2.replace("addquote ", "")
		f4 = f3.replace("[","")
		f5 = f4.replace("]","")
		#for debug uncomment next line
		#print(f5)
		t = datetime.date.today()
		params = (omg + 1,str(strftime("%Y-%m-%d %H:%M:%S", gmtime())),f5)
		d.execute("INSERT INTO quotes VALUES (?,?,?)",params)
		con.commit()
		con.close()
		return;

def addquotes(word, word_eol, userdata):
	command = word[0]
	if len(word) < 2:
		print("You must set some text to add. eg: /QADD this is an example.")
	else:
		if command == "QADD":
			insertdata(word);
			hexchat.command('me ' + '\002' + '\00302'+ 'added a quote.')

def delquotes(word):
	# not implemented yet...
	pass

viewdb();

hexchat.hook_command("QADD",addquotes)
hexchat.hook_command("QDEL",delquotes)
hexchat.prnt(__module_name__ + ' version ' + __module_version__ + ' loadded.')

