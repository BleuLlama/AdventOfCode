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
		originalList = map(chr, range(ord('a'), ord('p')+1))
		thelist = map(chr, range(ord('a'), ord('p')+1))

		print "----------------"
		m = 1000000000 % 63
		for a in range( 0, m ): #1000000000 ):
			#print "{}".format( self.a.data )
			#print "{} {}".format( a, thelist )

			print "{} {:.0%}".format( a, (float(a)/m) )

			if not cmp( originalList, thelist ):
				print "EQUAL AT {}".format( a )

			for i in self.a.data:
				cmd = i[:1]
				params = (i[1:]).split( '/' )
				if( cmd == 's' ):
					count = int( params[0] )
					while count > 0:
						#print 'S {}'.format( count )
						# pop() for end
						# pop(0) for front
						itm = thelist.pop() 
						thelist.insert(0,itm)
						count -= 1

				if( cmd == 'p' ):
					# stuff it!
					params[0] = thelist.index( params[0] )
					params[1] = thelist.index( params[1] )
					cmd = 'x'
				
				if( cmd == 'x' ):
					ia = int( params[0] )
					ib = int( params[1] )
					t = thelist[ ia ]
					thelist[ ia ] = thelist[ ib ]
					thelist[ ib ] = t
			
				#print "{} {}".format( cmd, params )
			print "{}".format( ''.join( thelist ) )

		print "{}".format( ''.join( thelist ) )
	# print "{}".format( ' '.join( wordlist ))

	# step 2 notes:
	# AHA!  1B loops was too long to compute 
	# and it gave the wrong answer
	# correct  ->  nlciboghmkedpfja
	# instead, modify the first to repeat forever,
	# when the pattern repeats, note the iterations (63)
	# instead of 1B loops, we just need to do 1B % 63
	# which ends up being 54 iterations

	# this way does NOT work since we have the "swap by letter" 
	# which can be in different places between iterations.
	def process2( self ):
		thelist = map(chr, range(ord('a'), ord('p')+1))
		# abcdefghij klmnop
		#            111111
		# 0123456789 012345
		# nlciboghjmfdapek
		# 
		xremap  = list( 'nlci bogh jmfd apek' )

		remap = [ 13, 11, 2, 8,
				1, 14, 6, 7,
				9, 12, 5, 3,
				0, 15, 4, 10 ]

		
		#for a in range( 0, 3300 ): #1000000000 ):
		#m = 1 000 000 000
		m = 1000000000
		m = 2
		for a in range( 0, m ):
			if a % 1000 == 0:
				print "{} {:.0%}".format( a, (float(a)/m) )
				sys.stdout.flush()
			remapped = []
			for r in range( 0, 16 ):
				remapped.append( thelist[ remap[r] ])
			thelist = remapped
			#print "{}".format( ''.join( remapped ) )
			
		print "{}".format( ''.join( thelist ) )
		#print "{}".format( ''.join( remapped ) )
		

if __name__ == "__main__":
	datas = [
		'input.txt'
	]
	d2 = [
		's1',
		's1,x3/4',
		's1,x3/4,pe/b',
	]

	for data in datas:
		d = Today( data )
		d.process( 1 )
		#d.process2( )
