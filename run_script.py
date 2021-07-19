import webbrowser
import sys
import time

sites_file_name = "sites.txt"
sites_file = []

if len(sys.argv) > 1:
    sites_file_name = f"{sys.argv[1]}_sites.txt"

try:
    sites = open(sites_file_name, "r")
except FileNotFoundError:
    print(f"Specified file not found. Attempted to open {sites_file_name}")

for site in sites:
    site = site.strip()
    if len(site) > 0:
        webbrowser.open_new_tab(site)
