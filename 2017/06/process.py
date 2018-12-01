#!/usr/bin/python

import sys
import os.path

class Today:
	def __init__( self, filename ):
		self.debug = False
		self.filename = filename
		self.lines = None
		self.loadFileIntoLines( )

	def loadFileIntoLines( self ):
		with open( self.filename ) as f:
			self.lines = [ line.rstrip('\n') for line in f ]
		self.lines = map( int, self.lines[0].split())
		print "  {}: {} items loaded in.".format( self.filename, len( self.lines ))
		if( self.debug ):
			i = 0
			for l in self.lines:
				print "{}: {}".format( i, l )
				i = i+1

	def serializeList( self ):
		return ' '.join( map( str, self.lines ))


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

	def redistribute( self ):
		# get the max value
		mv = max( self.lines )

		# go to item with this value
		i = 0
		while self.lines[i] != mv:
			i=i+1

		#print "Max of {} at position {}".format( mv, i )
		# zero that item
		self.lines[i] = 0

		# now, redistribute
		while mv > 0:
			# adjust
			i = i+1
			i = i % len( self.lines)
			self.lines[i] = self.lines[i] + 1
			mv = mv -1
		
		

	def process( self, step ):
		solutions = []
		sl = self.serializeList()
		print "SER: {}".format( sl )
		
		solutions.append( self.serializeList())

		while True:
			# shuffle items
			self.redistribute()

			# get serialization
			sl = self.serializeList()
			print "{}: {}".format( len( solutions) , sl )

			# check if it's in the list
			if solutions.count( sl ) > 0:
				print "Already in list!"
				i = 0
				for sss in solutions:
					i = i + 1
					if sss == sl:
						loopsize = len( solutions ) - i+1
							
				break

			solutions.append( sl )

		print "{} steps".format( len( solutions ))
		i = 0
		for sll in solutions:
			print "{}>> {}".format( i, sll )
			i=i+1

		print "Part 1 answer is {} steps".format( i )
		print "Part 2 answer is {} loopsize".format( loopsize )


if __name__ == "__main__":
	datafiles = [
		'input.txt'
	#	'example.txt' 
		]

	for data in datafiles:
		print '---------------'
		d = Today( data )
		d.process( 2 )
