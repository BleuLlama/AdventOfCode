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
		for line in self.lines:

			print "{}: |{}|".format( count, line )
			stringnumbers = line.split()

			if( len( stringnumbers ) == 0 ):
				continue

			# convert them to numbers
			numbers = map( int, stringnumbers )

			minval = int( min( numbers ))
			maxval = int( max( numbers ))
			difval = maxval - minval

			print ""
			print "{} - {} = {}".format( maxval, minval, difval )
			accumulator = accumulator + difval

			count = count + 1

		print "------"
		print "Result: {}".format( accumulator )
			

if __name__ == "__main__":
	sample1= [
		'sample.txt',
	]
	sample2 = [
		'input.txt' ]

	for data in sample2:
		print '---------------'
		d = Day2( data )
		d.process()
