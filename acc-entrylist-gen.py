#!/bin/python3

import sys
import json

def main(args):
	# Open the file
	if (len(args) == 1):
		sys.exit("You need to provide a valid JSON file.")
	with open(args[1], mode="r", encoding="utf-8") as input_json:
		race_data = json.load(input_json)
		print("Data loaded:")
		# print(json.dumps(json.loads(race_data).sessionResult.leaderBoardLines, sort_keys=True, indent=4))
		leaderboard = race_data["sessionResult"]["leaderBoardLines"]
		print(json.dumps(leaderboard, sort_keys=True, indent=2))
		input_json.close()
		sys.exit(0)


if __name__ == "__main__":
	main(sys.argv)
