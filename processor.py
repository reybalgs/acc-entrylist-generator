import sys
import jsonpickle
import random

from datetime import datetime
from dataclasses import Entrylist

class Processor:
	def write_file(self):
		# Write file
		filename = ("entrylist_" + datetime.now().strftime("%Y%m%d-%H%M%S") + 
			".json")
		with open(filename, 'w') as entrylistFile:
			entrylistFile.write(jsonpickle.encode(self.newEntrylist, 
				make_refs=False, unpicklable=False))
			entrylistFile.close()

		sys.exit("Operation finished. New entrylist JSON file: " + filename)

	def apply_processing(self):
		if (self.isReverse):
			self.newEntrylist.entries = list(reversed(self.newEntrylist
				.entries))

		if (self.isShuffle):
			random.shuffle(self.newEntrylist.entries)
			for entryIndex, entry in enumerate(self.newEntrylist.entries):
				try:
					entry['defaultGridPosition'] = entryIndex + 1
				except:
					entry.defaultGridPosition = entryIndex + 1

	def __init__(self, isReverse=False, isShuffle=False):
		self.isReverse = isReverse
		self.isShuffle = isShuffle
		self.newEntrylist = Entrylist()