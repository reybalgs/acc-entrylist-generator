#!/bin/python3

import sys
import jsonpickle
import random
from datetime import datetime

class Driver:
	def __init__(self, details):
		self.firstName = details['firstName']
		self.lastName = details['lastName']
		self.shortName = details['shortName']
		self.playerID = details['playerId']

class EntrylistEntry:
	def __init__(self, drivers: Driver, gridPos):
		self.drivers = drivers
		self.forcedCarModel = -1
		self.overrideDriverInfo = 0
		self.defaultGridPosition = gridPos

class Entrylist:
	def __init__(self, initEntries=None):
		self.entries = initEntries if initEntries else []
		self.forceEntryList = 1

def main(args):
	# Flag for tracking if the input is an entrylist, for shuffling
	isInputEntrylist = False
	# Flag to check if we're shuffling the resulting entrylist order
	isShuffle = False

	filePathArgIndex = 1

	if (len(args) == 1):
		sys.exit("You need to provide a valid JSON file.")
	if ("-e" in args):
		isInputEntrylist = True
	if ("-s" in args):
		isShuffle = True

	if len(sys.argv) > 2:
		filePathArgIndex = len(sys.argv) - 1

	with open(args[filePathArgIndex], mode="r", encoding="utf-8") as inputJson:
		if (isInputEntrylist):
			newEntryList = Entrylist()
			entrylistData = jsonpickle.decode(inputJson.read())
			newEntryList.entries = entrylistData['entries']
		else:
			race_data = jsonpickle.decode(inputJson.read())
			leaderboard = race_data["sessionResult"]["leaderBoardLines"]

			newEntryList = Entrylist()

			for carIndex, carEntry in enumerate(leaderboard):
				drivers = carEntry['car']['drivers']
				driversList = []
				for driver in enumerate(drivers):
					newDriver = Driver(driver)
					driversList.append(newDriver)
				newEntryListEntry = EntrylistEntry(driversList, carIndex + 1)
				newEntryList.entries.append(newEntryListEntry)

		if (isShuffle):
			random.shuffle(newEntryList.entries)
			for entryIndex, entry in enumerate(newEntryList.entries):
				try:
					entry['defaultGridPosition'] = entryIndex + 1
				except:
					entry.defaultGridPosition = entryIndex + 1

		# Write file
		filename = ("entrylist_" + datetime.now().strftime("%Y%m%d-%H%M%S") + 
			".json")
		with open(filename, 'w') as entrylistFile:
			entrylistFile.write(jsonpickle.encode(newEntryList, 
				make_refs=False, unpicklable=False))
			entrylistFile.close()

		inputJson.close()
		sys.exit("Operation finished. New entrylist JSON file: " + filename)


if __name__ == "__main__":
	main(sys.argv)
