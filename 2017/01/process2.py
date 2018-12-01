#!/usr/bin/python

import sys
import os.path

class Today:
	def __init__( self, filename ):
		self.debug = False
		self.filename = filename
		self.items = None
		self.loadFileIntoLines( )

	def loadFileIntoLines( self ):
                if not os.path.isfile( self.filename ):
			self.items = self.filename
		else :
		    with open( self.filename ) as f:
			    self.items = [ line.rstrip('\n') for line in f ]

		self.items = list( self.items[0] )
		print "  {}: {} items.".format( self.filename, len( self.items ))


	# numbers = map( int, stringnumbers ) # call int( x ) on each x
	# z.count( y ) # count occurrences of Y in list Z
	# sortedword.append( ''.join( sorted( word ))) # sort letters in a word 
	# wordlist = line.split()  # split apart words to a list

	# print the word list with spaces between each item
	# print "{}".format( ' '.join( wordlist ))
	# for word in newWords: # for each word in the list of words
	# str.strip()	# remove extra whitespace from head and tail
	# str.strip( 'xy' ) # removes all 'x' and 'y'
	# len( object ) # number of items in the object (array, list)

			
	def process( self ):
		self.items = map( int, self.items ) # convert to ints
		l = len(self.items)
		accumulator = 0

		for i in range( 0, l ):
			aa = self.items[i]
			bb = self.items[ (i + (l/2)) % l ]
			#print "{}: {} {}".format( i, aa, bb )
			if aa is bb:
				accumulator = accumulator + aa

		if( self.debug ):
			i = 0
			for op in opcodes:
				print "{}: {}".format( i, op )
				i=i+1
			
		print "Result: {}".format( accumulator )

if __name__ == "__main__":
	items = [
		'12345',
		'12221',
		'1212',
		'1221',
		'123425',
		'123123',
		'12131415',
	#]
	#junk = [
		'input.txt' ]

	for data in items:
		print '---------------'
		d = Today( data )
		d.process()
