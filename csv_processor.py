import jsonpickle
import csv

from processor import Processor
from dataclasses import Driver, Entrylist, EntrylistEntry

class CSVProcessor(Processor):
	def __init__(self, *args, **kwargs):
		super(CSVProcessor, self).__init__(*args, **kwargs)

	def process_csv(self, filePath: str):
		with open(filePath, mode="r", encoding="utf-8") as inputCsv:
			csvReader = csv.DictReader(inputCsv)
			for row in csvReader:
				drivers = [Driver({
					"firstName": row["firstName"].strip(),
					"lastName": row["lastName"].strip(),
					"shortName": row["shortName"].strip(),
					"playerId": row["playerID"].strip(),
				})]
				newEntrylistEntry = EntrylistEntry(drivers, 
					int(row["defaultGridPosition"].strip()), 
					int(row["overrideDriverInfo"].strip()), 
					int(row["ballastKg"].strip()),
					int(row["restrictor"].strip()),
					int(row["isServerAdmin"].strip()))
				self.newEntrylist.entries.append(newEntrylistEntry)

			inputCsv.close()
			self.apply_processing()
			self.write_file()
