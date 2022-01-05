#!/bin/python3

import sys
import jsonpickle
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
	def __init__(self):
		self.entries = []
		self.forceEntryList = 1

def main(args):
	if (len(args) == 1):
		sys.exit("You need to provide a valid JSON file.")
	with open(args[1], mode="r", encoding="utf-8") as input_json:
		race_data = jsonpickle.decode(input_json.read())
		leaderboard = race_data["sessionResult"]["leaderBoardLines"]

		newEntryList = Entrylist()

		for carIndex, carEntry in enumerate(leaderboard):
			drivers = carEntry['car']['drivers']
			driversList = []
			for driverIndex, driver in enumerate(drivers):
				newDriver = Driver(driver)
				driversList.append(newDriver)
			newEntryListEntry = EntrylistEntry(driversList, carIndex + 1)
			newEntryList.entries.append(newEntryListEntry)

		# Write file
		filename = ("entrylist_" + datetime.now().strftime("%Y%m%d-%H%M%S") + 
			".json")
		with open(filename, 'w') as entrylistFile:
			entrylistFile.write(jsonpickle.encode(newEntryList, 
				make_refs=False, unpicklable=False))
			entrylistFile.close()

		input_json.close()
		sys.exit("Operation finished. New entrylist JSON file: " + filename)


if __name__ == "__main__":
	main(sys.argv)
