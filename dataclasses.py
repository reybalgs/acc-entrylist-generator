class Driver:
	def __init__(self, details):
		self.firstName = details['firstName']
		self.lastName = details['lastName']
		self.shortName = details['shortName']
		self.playerID = details['playerId']

class EntrylistEntry:
	def __init__(self, drivers: Driver, gridPos, overrideDriverInfo=0,
			ballastKg=0, restrictor=0, isServerAdmin=0):
		self.drivers = drivers
		self.forcedCarModel = -1
		self.overrideDriverInfo = overrideDriverInfo
		self.defaultGridPosition = gridPos
		self.ballastKg = ballastKg
		self.restrictor = restrictor
		self.isServerAdmin = isServerAdmin

class Entrylist:
	def __init__(self, initEntries=None):
		self.entries = initEntries if initEntries else []
		self.forceEntryList = 1
