#!/usr/bin/python

import sys
import os.path

class Day1:
	def __init__( self, fileOrString ):
		self.data = None
		self.loadFileIntoBuffer( fileOrString )

	def loadFileIntoBuffer( self, filename ):
		if os.path.isfile( filename ):
			print "Loading in file {}".format( filename )
			f = open( filename, 'r' )
			self.data = f.read()
			f.close
		else:
			print "Using immediate data."
			self.data = filename;
	

	def process( self ):
		if self.data is None:
			print "No data loaded."
			return

		print "Data: {}".format( self.data )

		firstVal = None
		lastVal = None
		accumulator = 0

		for ch in self.data:
			val = 0;
			if ch.isdigit():
				sys.stdout.write( ch )
				try:
					val = int( ch )
				except:
					print "Unexpected error:", sys.exc_info()[0]
				else:
					if firstVal is None:
						sys.stdout.write( '!' )
						firstVal = val

					if val == lastVal:
						sys.stdout.write( '+' )
						accumulator = accumulator + val

					lastVal = val

		print ""
		print "-----"

		# finally, check first and last
		if firstVal == lastVal:
			if firstVal != None:
				sys.stdout.write( '+' )
				accumulator = accumulator + firstVal

		print "Result: {}".format( accumulator )


if __name__ == "__main__":
	sampleInputs = [
		'1122', # -> 3
		'1111', # -> 4
		'1234', # -> 0
		'91212129', # - 9
	#]
	#sample2 = [
		'input.txt' ]

	for data in sampleInputs:
		print '---------------'
		d = Day1( data )
		d.process()
