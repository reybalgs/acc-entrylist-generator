#!/bin/python3

import sys

from json_processor import JSONProcessor
from csv_processor import CSVProcessor

def main(args):
	isInputEntrylist = ("-e" in args)
	isShuffle = ("-s" in args)
	isReverse = ("-r" in args)
	isCsv = ("-c" in args)

	if len(sys.argv) > 1:
		filePathArgIndex = len(sys.argv) - 1
	else:
		sys.exit("You need to provide a valid JSON or CSV file.")

	if (isCsv):
		processor = CSVProcessor(isReverse, isShuffle)
		processor.process_csv(args[filePathArgIndex])
	else:
		processor = JSONProcessor(isInputEntrylist, isReverse, isShuffle)
		processor.process_json(args[filePathArgIndex])

if __name__ == "__main__":
	main(sys.argv)
