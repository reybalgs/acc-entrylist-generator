# ACC Entrylist Generator

A util Python script for creating entrylists based on input JSON files (typically results).

## Usage

### Generate entrylist based on results leaderboard (for separate quali sessions, sprint qualifying)

Simply run the Python script while supplying the path of the leaderboards/results JSON as the first argument.

```
./acc-entrylist-gen.py <your_results_file>.json
```

## Libraries

Uses jsonpickle. Install it on Ubunutu with: `sudo apt install python3-jsonpickle`.

## Planned features

Reverse grid functionality
