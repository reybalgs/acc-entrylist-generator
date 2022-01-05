# ACC Entrylist Generator

A util Python script for generating Assetto Corsa Competizione entrylists based on input JSON files (typically results).

## Usage

### Generate entrylist based on results leaderboard (for separate quali sessions, sprint qualifying)

Simply run the Python script while supplying the path of the leaderboards/results JSON as the first argument.

```
./acc-entrylist-gen.py <your_results_file>.json
```

### Shuffle the resulting entrylist

Pass the `-s` flag before the input file path, like so:

```
./acc-entrylist-gen.py -s <your_results_file>.json
```

### Reading (and shuffling) an existing entrylist

The script can also be used to shuffle an existing preformatted entrylist. This is useful in the case of shuffling a pre-created entrylist, in the case of having a randomized grid of a pre-set list of participants. Simply use the `-e` flag along with the `-s` flag before the filepath of your entrylist JSON file.

```
./acc-entrylist-gen.py -e -s <your_results_file>.json
```

Of course, you can omit the `-s` flag so it doesn't shuffle the order, but what's the point in that?

## Libraries

Uses jsonpickle. Install it on Ubunutu with: `sudo apt install python3-jsonpickle`.

