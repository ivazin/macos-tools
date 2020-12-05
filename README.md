# My tools for macOS
## Safari_ReadingList_to_csv.py
Exports DateAdded, DateLastViewed (read or not), URL and Title for all links in ReadingList.
### Usage
For macOS Big Sur you need to allow Full Disk Access for yout Terminal:

System Preferences → Security & Privacy → Privacy → Full Disk Access → Terminal (tick ☑️ it).

Restart Terminal.

Command ot Export:
```bash
python3 Safari_ReadingList_to_csv.py
```
Generates:

```bash
readinglist.csv
```
in current folder.
