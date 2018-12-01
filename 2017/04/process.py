#!/usr/bin/python

import sys
import os.path

class Today:
	def __init__( self, filename ):
		self.filename = filename
		self.lines = None
		self.loadFileIntoLines( )

	def loadFileIntoLines( self ):
		with open( self.filename ) as f:
			self.lines = [ line.rstrip('\n') for line in f ]

# numbers = map( int, stringnumbers )

	def isItValid__P1( self, line ):
		words = line.split()
		for word in words:
			if words.count( word ) > 1:
				return False
		return True

	def isItValid( self, line ):
		newWords = []
		words = line.split()
		for word in words:
			newWords.append( ''.join( sorted( word )))

		print "{}".format( ' '.join( newWords ))

		for word in newWords:
			if newWords.count( word ) > 1:
				return False
		return True

	def process( self ):
		count = 1
		accumulator = 0
		for line in self.lines:

			if( len( line.strip() ) == 0 ):
				continue


			if self.isItValid( line ):
				accumulator = accumulator + 1
			else:
				print "{}: |{}|".format( count, line )

			# convert them to numbers
			count = count + 1

		print "------"
		print "Result: {}".format( accumulator )
			

if __name__ == "__main__":
	sample2 = [
		'input.txt' ]

	for data in sample2:
		print '---------------'
		d = Today( data )
		d.process()
