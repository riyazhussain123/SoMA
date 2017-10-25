'''
Contains SoMA Core functions and classes
'''
from uuid import *
import json
from collections import namedtuple

class SoMAPost():
	def __init__(self,jsoncontent=None):
		self.uuid=uuid4()
		if jsoncontent==None:
			self.content=None
		else:
			self.attributes=json.loads(jsoncontent,object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
			self.dictionary=json.loads(jsoncontent)
