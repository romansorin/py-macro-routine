# py-macro-routine

A Python script to be run daily that opens a list of specified sites. Great for checking email, financials/balances, TODO list, trackers, etc. at a given point of the day at once with consistency.

## Usage
1. Create a list of sites to open (see sites.txt.example)
`$ cp sites.txt.example sites.txt`

2. Run with python3:
`$ python3 run_script.py`

If you want to support multiple contexts/environments, you can pass an argument to the command line to open the specified file:
```bash
$ cp sites.txt.example work_sites.txt
$ python3 run_script.py work
## This runs the script with the work_sites list, rather than the default sites list.
```

