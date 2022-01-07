import jsonpickle

from processor import Processor
from dataclasses import Driver, Entrylist, EntrylistEntry

class JSONProcessor(Processor):
	def __init__(self, isInputEntrylist=False, *args, **kwargs):
		super(JSONProcessor, self).__init__(*args, **kwargs)
		self.isInputEntrylist = isInputEntrylist
		
	def process_json(self, filePath: str):
		with open(filePath, mode="r", encoding="utf-8") as inputJson:
			if (self.isInputEntrylist):
				entrylistData = jsonpickle.decode(inputJson.read())
				self.newEntrylist.entries = entrylistData['entries']
			else:
				race_data = jsonpickle.decode(inputJson.read())
				leaderboard = race_data["sessionResult"]["leaderBoardLines"]

				for carIndex, carEntry in enumerate(leaderboard):
					drivers = carEntry['car']['drivers']
					driversList = []
					for driverIndex, driver in enumerate(drivers):
						newDriver = Driver(driver)
						driversList.append(newDriver)
					newEntryListEntry = EntrylistEntry(driversList, carIndex + 1)
					self.newEntrylist.entries.append(newEntryListEntry)

			inputJson.close()
			self.apply_processing()
			self.write_file()
