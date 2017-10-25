'''
Contains SoMA Core functions and classes
'''
from uuid import *
import json
from collections import namedtuple


'''
SoMA Post objects store a JSON object as a named tuple as well as a dictionary, so that attributes can be referenced both in the dot notation as well as by key/value lookups. 
'''

class SoMAPost():
	def __init__(self,jsoncontent=None):
		self.uuid=uuid4()
		if jsoncontent==None:
			self.content=None
		else:
			#Got this nice little object factory like implementation from https://stackoverflow.com/questions/6578986/how-to-convert-json-data-into-a-python-object for the dot notation support
			self.attributes=json.loads(jsoncontent,object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
			#This just loads the same content into a dict as well
			self.dictionary=json.loads(jsoncontent)
		
