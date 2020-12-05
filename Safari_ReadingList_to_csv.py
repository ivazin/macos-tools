import os
import plistlib
import csv

BOOKMARKS_FILE  = os.path.join(os.environ['HOME'], 'Library/Safari/Bookmarks.plist')
OUTPUT_CSV_FILE = 'readinglist.csv'

# Load and parse the Bookmarks file
with open(BOOKMARKS_FILE, 'rb') as plist_file:
    plist = plistlib.load(plist_file)

# Look for the child node which contains the Reading List data.
# There should only be one Reading List item
children = plist['Children']

for child in children:
    if child.get('Title', None) == 'com.apple.ReadingList':
        reading_list = child

# Extract the bookmarks
bookmarks = reading_list['Children']

# Preparing the list of bookmarks with dates and titles
res = []
for b in bookmarks:
	res.append(
		[b.get('ReadingList', None).get('DateAdded', None),
		b.get('ReadingList', None).get('DateLastViewed', None),
		b.get('URLString', None),
		b.get('URIDictionary', None).get('title', None)]
		)

# Writing list to titled CSV
with open(OUTPUT_CSV_FILE, 'w') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    wr.writerow(['DateAdded', 'DateLastViewed', 'URLString', 'Title'])
    wr.writerows(res)
