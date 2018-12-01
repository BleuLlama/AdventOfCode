#!/usr/bin/python

import sys
import os.path
sys.dont_write_bytecode = True
sys.path.append( '../libs' )
from libAOC import AOC

class Today:
	def __init__( self, d ):
		self.a = AOC( d )
		self.a.loadFileCSV()
		print "SER: {}".format( self.a.serialize())
		#if self.a.isFile:
		#	self.a.dataLineToList()

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

	def dumpList( self, theList ):
		for z in range( 0, len( theList )):
			print "{} -> {}".format( z, self.a.getC( theList, z ))

	def process( self, step ):
		circlist = range( 0, 256 )
		position = 0
		skip = 0
		for i in self.a.data:
			#position = position % 255
			i = int( i )
			# 1. twist ribbon
			print "pos {:4}  skp {:2}  swp {}".format( position, skip, i)
			self.a.reorgC( circlist, position, i )
			self.a.dump( "After {}".format( i ), circlist )
			# 2. move forward length changed
			position += i
			# 3. move forward skipsize
			position += skip
			# 4. skip increment
			skip += 1
			
		self.a.dump( "final string", circlist )

		print "Position: {} content: {}".format( position, self.a.getC( circlist, position ))
		print "    Skip: {}".format( skip )

		a = self.a.getC( circlist, 0 )
		b = self.a.getC( circlist, 1 )
		print "[0,1] = [{},{}] *= {}".format( a, b, a*b )

	def demotest( self, step ):
		circlist = range( 0, 5 )
		#self.a.dump( "Input string" )
		position = 0
		skip = 0
		for i in self.a.data:
			i = int( i )
			# 1. twist ribbon	
			self.a.reorgC( circlist, position, i )
			self.a.dump( "After {}".format( i ), circlist )
			# 2. move forward length changed
			position += i
			# 3. move forward skipsize
			position += skip
			# 4. skip increment
			skip += 1
			
		self.a.dump( "final string", circlist )
		print "should be: 3 4 2 1 [0]"
		print "Position: {} content: {}".format( position, self.a.getC( circlist, position ))
		print "    Skip: {}".format( skip )

	def workout( self, step ):
		circlist = range( 0, 6 )

		self.a.dump()
		self.a.dump( "Start: Circ List", circlist )

		self.a.reorgC( circlist, 1, 2 )
		self.a.dump( "Start: [1]-[2] swap Circ List", circlist )

		circlist = range( 0, 6 )
		self.a.reorgC( circlist, 1, 3 )
		self.a.dump( "Start: [1]-[3] swap Circ List", circlist )

		for z in range( 0, 5 ):
			print "{} -> {}".format( z, self.a.getC( circlist, z ))

		return

if __name__ == "__main__":
	datas = [
		'input.txt' 
	]

	d2 = [
		'3,4,1,5'
	]

	for data in datas:
		d = Today( data )
		d.process( 1 )
