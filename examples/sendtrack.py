#!/usr/bin/env python
#
# PyMTP demo scripts
# (c) 2008 Nick Devito
# Released under the GPL v3 or later.
#

import sys
sys.path.insert(0, "../")

import pymtp
from ID3 import *

def usage():
	print "Usage: %s <source> <target> <parent>\n(The parent id can be 0 for the root directory)" % (sys.argv[0])

def main():
	if len(sys.argv) <= 3:
		usage()
		sys.exit(2)
		
	mtp = pymtp.MTP()
	mtp.connect()

	source = sys.argv[1]
	target = sys.argv[2]
	parent = int(sys.argv[3])

	id3data = ID3(source)

        metadata = pymtp.LIBMTP_Track()
	metadata.parent_id = parent;

        if (hasattr(id3data, 'artist')):
		metadata.artist = id3data.artist
	if (hasattr(id3data, 'title')):
		metadata.title = id3data.title
	if (hasattr(id3data, 'album')):
		metadata.album = id3data.album

	track_id = mtp.send_track_from_file(source, target, metadata)
	print "Created new track with ID: %s" % (track_id)
	mtp.disconnect()
		
if __name__ == "__main__":
	main()
