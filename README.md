# ACC Entrylist Generator

A utility Python script for generating Assetto Corsa Competizione entrylists based on input JSON files, typically results, but can also work on existing entrylists.

## Usage

This `.py` script will pretty much work from anywhere, though it is recommended that you copy and run it in the same directory as your input JSON files, for convenience. The output files are created in the same directory the script is in.

### Generate entrylist based on results leaderboard (for separate quali sessions, sprint qualifying)

Simply run the Python script while supplying the path of the leaderboards/results JSON as the first argument.

```
./acc-entrylist-gen.py <your_results_file>.json
```

These results JSON files are always generated in your server's `results` directory if you use `"dumpLeaderboards": 1` option in your server's `settings.json` file, as shown [in this guide](https://www.acc-wiki.info/wiki/Server_Configuration#Result_Files).

### Reading an existing entrylist

You can also use an existing entrylist to process in the script. This is done using the `-e` flag before your filepath, to tell the script that you are processing an existing entrylist. This is pretty much useless on its own, unless, you use one or more of the following flags:

### Reversing the grid order

Reverse grids are a really popular option for many leagues. Why make it hard for yourself, the organizer? Reverse the resulting entrylist with the `-r` flag so you can get an instant 

### Shuffling the grid

Pass the `-s` flag before the input file path, like so:

```
./acc-entrylist-gen.py -s <your_results_file>.json
```

This is useful in the case of shuffling a pre-created entrylist, in the case of having a randomized grid of a pre-set list of participants. Simply use the `-e` flag along with the `-s` flag before the filepath of your entrylist JSON file.

```
./acc-entrylist-gen.py -e -s <your_results_file>.json
```

**NOTE!** Shuffling always happens _after_ you reverse the grid order with `-r`. So using `-s` with `-r` will pretty much destroy the reversed grid order.

## Libraries

Uses jsonpickle. Install it on Ubunutu with: `sudo apt install python3-jsonpickle`.

