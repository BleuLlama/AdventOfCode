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
		if self.a.isFile:
			self.a.dataLineToList()

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
		#self.a.dump()

		# states:	'ready'
		# 		'bang'
		# 		'garbage'
		state = 'ready'
		bang = False
		garbage = False

		nestlevel = 0
		acc = 0
		# quick and dirty version:
		# 
		g = 0

		for c in self.a.data:
			x = ''
			if garbage:
				if bang:
					x = "not!"
					bang = False
				else:
				    	if c == '!':
						x = "!"
						bang = True
					elif c == '>':
						x = ">"
						garbage = False
					else:
						g += 1
			else:
			    	if c == '<':
					x = "<"
					bang = False
					garbage = True
				if c == '{':
					x = "{"
					nestlevel += 1
					acc += nestlevel
				if c == '}':
					x = "}"
					nestlevel -= 1
				
			#self.a.write( "({}-{}) ".format( c,x ))
		print " is {}".format( acc )
		print "Garbage Count is {}".format( g )
			

if __name__ == "__main__":
	datas = [
		'input.txt' 
	]

	step2 = [
		'<>', # 0
		'<random characters>', #17 characters.
		'<<<<>', # 3 characters.
		'<{!>}>', # 2 characters.
		'<!!>', # 0 characters.
		'<!!!>>', # 0 characters.
		'<{o"i!a,<{i<a>', # 10 characters.

	]
	step1 = [
	    '{{{},{},{{}}}}', # score of 1 + 2 + 3 + 3 + 3 + 4 = 16.  
	    '{}',       # 1
	    '{{{}}}', # score of 1 + 2 + 3 = 6.
	    '{{},{}}', # score of 1 + 2 + 2 = 5.  
	    '{<a>,<a>,<a>,<a>}', # score of 1.  
	    '{{<ab>},{<ab>},{<ab>},{<ab>}}', # score of 1 + 2 + 2 + 2 + 2 = 9.  
	    '{{<!!>},{<!!>},{<!!>},{<!!>}}', # score of 1 + 2 + 2 + 2 + 2 = 9.
	    '{{<a!>},{<a!>},{<a!>},{<ab>}}', # score of 1 + 2 = 3.
	]

	for data in datas:
		d = Today( data )
		d.process( 1 )
