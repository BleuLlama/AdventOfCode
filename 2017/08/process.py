#!/usr/bin/python

import sys
import os.path
sys.dont_write_bytecode = True
sys.path.append( '../libs' )
from libAOC import AOC

class Today:
	def __init__( self, d ):
		self.a = AOC( d )
		self.a.loadFileIntoLines()
		#print self.a.serialize()


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

	registers = {}

	def get( self, r ):
		val = self.registers.get( r )
		if val == None:
			return 0
		return val

	def set( self, r, v ):
		self.registers[ r ] = v
	

	def process( self, step ):
		self.a.dump()

		maxValEver = 0
		for datum in self.a.data:
		 	cols = datum.split()
			# format is:
			# register op value IF comparereg comparison value
			
			treg = cols[0]
			opcode = cols[1]
			operand = int( cols[2] )

			creg = cols[4]
			copcode = cols[5]
			cval = int( cols[6] )

			# make all addition
			if( opcode == 'dec' ):
				operand *= -1

			print "{}".format( cols )
			print "  if( {} {} {} ) then {} += {}".format(
				creg, copcode, cval,
				treg, operand )

			cregval = self.get( creg )
			tregval = self.get( treg )
			if copcode == '==': 
				if cregval == cval: tregval += operand
			elif copcode == '!=':
				if cregval != cval: tregval += operand
			elif copcode == '>=':
				if cregval >= cval: tregval += operand
			elif copcode == '>':
				if cregval > cval: tregval += operand
			elif copcode == '<=':
				if cregval <= cval: tregval += operand
			elif copcode == '<':
				if cregval < cval: tregval += operand
			else:
				print "ERROR: UNKNOWN COMPARE {}".format( copcode )
			self.set( treg, tregval )

			# extra computations for Step 2:
			maxValNow = max( self.registers.values() )
			if maxValNow > maxValEver:
				maxValEver = maxValNow
			

		self.a.dumpDict( "Registers", self.registers )
		maxValNow = max( self.registers.values() )
		print "Step 1: Max(registers) = {}".format( maxValNow )
		print "Step 2: Max(ever)      = {}".format( maxValEver )

if __name__ == "__main__":
	datas = [
		'input.txt' ]
	junk = [
		'example.txt' ]

	for data in datas:
		d = Today( data )
		d.process( 1 )
