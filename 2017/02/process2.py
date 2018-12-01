#!/usr/bin/python

import sys
import os.path

class Day2:
	def __init__( self, filename ):
		self.filename = filename
		self.lines = None
		self.loadFileIntoLines( )

	def loadFileIntoLines( self ):
		with open( self.filename ) as f:
			self.lines = [ line.rstrip('\n') for line in f ]



	def process( self ):
		count = 1
		accumulator = 0
		step = 2
		for line in self.lines:

			print "{}: |{}|".format( count, line )
			stringnumbers = line.split()

			if( len( stringnumbers ) == 0 ):
				continue

			# convert them to numbers
			numbers = map( int, stringnumbers )

			# step 1:
			aa = bb = change = 0
			if step is 1:
				aa = int( min( numbers ))
				bb = int( max( numbers ))
				change = bb - aa
			else :
				for s in numbers:
					for t in numbers:
						if s != t and ( s % t ) is 0:
							aa = s
							bb = t
				change = max( [ aa, bb ]) / min( [ aa, bb ])

			print "    {} ~ {} = {}".format( bb, aa, change )
			accumulator = accumulator + change

			count = count + 1

		print "------"
		print "Result: {}".format( accumulator )
			

if __name__ == "__main__":
	files = [
		'input.txt',
	]
	junk = [
		'sample.txt',
	 ]

	for data in files:
		print '---------------'
		d = Day2( data )
		d.process()
