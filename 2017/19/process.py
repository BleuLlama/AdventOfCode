#!/usr/bin/python

import sys
import os.path
sys.dont_write_bytecode = True
sys.path.append( '../libs' )
from libAOC import AOC

class Today:
	def __init__( self, d ):
		print "{}".format( d )
		self.a = AOC( d )
		self.a.load2D()

		#print "SER: {}".format( self.a.serialize())
		#if self.a.isFile:

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

	def tokenize( self, ch ):
		if ch == ' ':
			return None
		if ch >= 'A' and ch <= 'Z':
			return 'LETTER'
		if ch == '-':
			return 'EW'
		if ch == '|':
			return 'NS'
		if ch == '+':
			return 'CHANGEDIR'
		return '?'

	def process( self, step ):
		# 1. find entry point
		x = -1
		for i in range( 0, len( self.a.data[0] )):
			if self.a.data[0][i] == '|':
				x = i
		y = 0

		#          ^^ dy = -1
		# << dx=-1     dx=1 >>
		#          vv dy = 1

		# start by moving down
		dx = 0
		dy = 1

		# accumulator = 0;
		acc = []

		self.a.dump()
		print "Entry Point is {},{}".format( x, y )

		steps = 1
		while True:
			# 1. move
			x += dx
			y += dy
			ch = self.a.at( x, y )
			cht = self.tokenize( ch )


			# react
			if cht == None:
				# end of path
				break
			elif cht == 'LETTER':
				# letter! accumulate!
				print "letter!"
				acc.append( ch )
			elif cht == 'CHANGEDIR':
				# change direction!
				if dy == 0:
					print "turn to vertical!"
					# switch to vertical
					dx = 0
					north = self.a.at( x, y-1 )
					nt = self.tokenize( north )

					#south = self.a.at( x, y+1 )
					#st = self.tokenize( south )
					if nt == 'LETTER' or nt == 'NS':
						dy = -1
					else:
						dy = 1
				else:
					print "turn to horizontal!"
					# switch to horizontal
					dy = 0
					east = self.a.at( x+1, y )
					et = self.tokenize( east )
					#west = self.a.at( x-1, y )
					#wt = self.tokenize( west )
					if et == 'LETTER' or et == 'EW':
						dx = 1
					else:
						dx = -1
			steps += 1
			self.a.write( '.' )

		print "ACC: {}".format( self.a.serialize( acc, '' ))
		print "{} steps".format( steps )

if __name__ == "__main__":
	datas = [
		'input.txt'
	]
	d2 = [
		'sample.txt',
	]

	for data in datas:
		d = Today( data )
		d.process( 1 )
		#d.process2( )
