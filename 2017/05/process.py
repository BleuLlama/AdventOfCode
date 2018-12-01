#!/usr/bin/python

import sys
import os.path
sys.dont_write_bytecode = True
sys.path.append( '../libs' )
from libAOC import AOC

class Today:
	def __init__( self, filename ):
		self.debug = False
		self.filename = filename
		self.lines = None
		self.loadFileIntoLines( )

	def loadFileIntoLines( self ):
		with open( self.filename ) as f:
			self.lines = [ line.rstrip('\n') for line in f ]
		print "  {}: {} lines loaded in.".format( self.filename, len( self.lines ))


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

			
	def process( self, step ):
		pc = 0
		accumulator = 0
		# convert list of lines to a list of opcodes
		opcodes = map( int, self.lines )
		while pc >= 0 and pc < len( opcodes ):
			# 1. retrieve current value
			opcode = opcodes[pc]

			# x. Debug output
			print "Tick {}  PC {}   Data:{}".format( accumulator, pc, opcode )
			# 2. increment value at current pointer
			if step == 1:
				# step 1: always inc
				opcodes[pc] = opcodes[pc] + 1
			else:
				# step 2: dec or inc
				if opcode >= 3:
					opcodes[pc] = opcodes[pc] - 1
				else:
					opcodes[pc] = opcodes[pc] + 1

			# 3. adjust PC for original value
			pc = pc + opcode

			# 4. Increment accumulator (time tick)
			accumulator = accumulator+1

		if( self.debug ):
			i = 0
			for op in opcodes:
				print "{}: {}".format( i, op )
				i=i+1
			
		print "Result: {}".format( accumulator )

if __name__ == "__main__":
	datafiles = [
		'input.txt' ]
	junk = [
		'example.txt', ]

	for data in datafiles:
		#a = AOC( data )
		#a.loadFileIntoLines()
		#a.dumpLines()
		print '---------------'
		d = Today( data )
		d.process( 2 )
