#!/bin/python3

import sys
import json
import jsonpickle
from datetime import datetime

class Driver:
	def __str__(self) -> str:
		return ("Driver: " + self.firstName + " " + self.lastName + "\n" +
			"SteamID: " + self.playerID)

	def __init__(self, details):
		self.firstName = details['firstName']
		self.lastName = details['lastName']
		self.shortName = details['shortName']
		self.playerID = details['playerId']

class EntrylistEntry:
	def toJSON(self):
		return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

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
	# Open the file
	if (len(args) == 1):
		sys.exit("You need to provide a valid JSON file.")
	with open(args[1], mode="r", encoding="utf-8") as input_json:
		race_data = json.load(input_json)
		print("Data loaded:")
		# print(json.dumps(json.loads(race_data).sessionResult.leaderBoardLines, sort_keys=True, indent=4))
		leaderboard = race_data["sessionResult"]["leaderBoardLines"]
		# print(json.dumps(leaderboard, sort_keys=True, indent=2))
		print("cars:\n")

		newEntryList = Entrylist()

		for carIndex, carEntry in enumerate(leaderboard):
			drivers = carEntry['car']['drivers']
			print("Place: " + str(carIndex + 1))
			print("Car Model: " + str(carEntry['car']['carModel']))

			for driverIndex, driverEntry in enumerate(drivers):
				print("Driver #" + str(driverIndex) + ":")
				currDriver = Driver(driverEntry)
				print(currDriver)

			newEntryListEntry = EntrylistEntry(drivers, carIndex)
			# print(json.dumps(newEntryListEntry, sort_keys=True, indent=2))
			print(jsonpickle.encode(newEntryListEntry, make_refs=False, unpicklable=False))
			newEntryList.entries.append(newEntryListEntry)
			
			print("\n===\n")

		print("Finished entrylist:")
		print(jsonpickle.encode(newEntryList, make_refs=False, unpicklable=False))

		# Write file
		filename = "entrylist_" + datetime.now().strftime("%Y%m%d-%H%M%S") + ".json"
		with open(filename, 'w') as entrylistFile:
			entrylistFile.write(jsonpickle.encode(newEntryList, make_refs=False, unpicklable=False))
			entrylistFile.close()

		input_json.close()
		sys.exit("Operation finished. New entrylist JSON file: " + filename)


if __name__ == "__main__":
	main(sys.argv)
