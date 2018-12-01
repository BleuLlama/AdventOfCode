#!/usr/bin/python

import sys
import os.path

class AOC:
	debug = False

	# parsed data
	data = None
	isFile = False

	def __init__( self, filename ):
		self.filename = filename

	# ------ LOAD DATA -------

	# file as data
	def loadFile( self ):
		# not found as a file, use immediate data
		if not os.path.isfile( self.filename ):
			self.data = self.filename
			return

		# it was a file, load it in
		f = open( self.filename, 'r' )
		self.data = f.read()
		f.close
		self.isFile = True

	# file as line list
	def loadFileIntoLines( self ):
		# not found as a file, use immediate data?
		if not os.path.isfile( self.filename ):
			self.data = self.filename
			return

		# load in all lined
		with open( self.filename ) as f:
			self.data = [ line.rstrip('\n') for line in f ]
		self.isFile = True

	def loadFileCSV( self ):
		# not found as a file, use immediate data?
		if not os.path.isfile( self.filename ):
			self.data = self.filename

		else:
			self.isFile = True
			# load in all lined
			with open( self.filename ) as f:
				self.data = [ line.rstrip('\n') for line in f ]

		if isinstance( self.data, list ):
			self.data = self.data[0]
		self.data = [x.strip() for x in self.data.split(',')]

	def load2D( self ):
		self.loadFileIntoLines()
		raster = []

		for line in self.data:
			raster.append( list( line ))

		self.data = raster

	def at( self, x, y ):
		if y >= len( self.data ):
			return None
		if x >= len( self.data[y] ):
			return None
		return self.data[y][x]

	# ------ process -------

	def extract( self, string, start='(', stop=')'):
		return string[string.index(start)+1:string.index(stop)]

	def dataLineToList( self ):
		self.data = list( self.data[0] )

	def dataLineCSVList( self ):
		self.data = [x.strip() for x in self.data[0].split(',')]

	def dataListToInts( self ):
		self.data = map( int, self.data )

	def min( self ):
		return min( self.data )

	def max( self ):
		return max( self.data )

	def serialize( self, theList, sepchar = None ):
		if sepchar == None:
			sepchar = ' '
		if theList == None:
			return "{}".format( sepchar.join( self.data ))
		return "{}".format( sepchar.join( theList ))

	def getC( self, theList, index ):
		return theList[ index % len( theList )]

	def setC( self, theList, index, value ):
		theList[ index % len( theList )] = value

	def reorgC( self, theList, start, count ):
		for x in range( 0, count/2 ):
			a = start+x
			b = start+count-x-1
			tempa = self.getC( theList, a )
			tempb = self.getC( theList, b )
			self.setC( theList, a, tempb )
			self.setC( theList, b, tempa )
		

	# ------ Output -------

	def write( self, s ):
		sys.stdout.write( s )

	# ------ Dump -------

	def dump( self, heading=None, lst=None ):

		if( heading == None ):
			heading = "self.data"
		if( lst == None ):
			lst = self.data

		print "---- {} ----".format( heading )
		i = 0
		if lst == None:
			print "no data."
			return

		for item in lst:
			print "{:3}: {}".format( i, item )
			i=i+1

		print "----"
		print "{}: {} items".format( heading, len( lst ))
		print

	def dumpDict( self, heading, lst ):
		print "---- {} ----".format( heading )
		for key, value in sorted( lst.items() ):
			print "{}: {}".format( key, value )
 
		print "----"
		print "{}: {} items".format( heading, len( lst ))
		print

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
