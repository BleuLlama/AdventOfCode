#!/usr/bin/python

import sys
import os.path
sys.dont_write_bytecode = True
sys.path.append( '../libs' )
from libAOC import AOC

class Today:
	def __init__( self, d ):
		print "{}".format( d )

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
                thelist = map(chr, range(ord('a'), ord('z')+1))
                thelist += map(chr, range(ord('A'), ord('Z')+1))

		print "{} {}".format( len( thelist ), thelist )

		for a in range( 0, len(thelist)):
			v = float( a )/(len(thelist)-1)* 255.0
			z = a * 5;
			print '{} -> {} {}'.format( thelist[a], v, z)

		



if __name__ == "__main__":
	datas = [
		'input.txt',
	]

	for data in datas:
		d = Today( data )
		d.process( 1 )
		#d.process2( )
