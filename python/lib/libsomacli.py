'''
Contains functions and classes specific to the command line interface of SoMA
'''

import os,json, datetime
#from state import *
from datetime import *
from pygments import highlight, lexers, formatters
from termcolor import colored

def get_formatted_json(dictionary):
	formatted_json=json.dumps(dictionary,sort_keys=True, indent=4)
	return formatted_json
	
def get_color_json(dictionary):
	formatted_json=get_formatted_json(dictionary)
	colorful_json = highlight(unicode(formatted_json, 'UTF-8'), lexers.JsonLexer(), formatters.TerminalFormatter())
	return colorful_json
