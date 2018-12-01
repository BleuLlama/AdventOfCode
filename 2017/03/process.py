#!/usr/bin/python

# libs to import
import sys
import os.path
import math

# import AOC lib
sys.path.append( '../libs' )
from libAOC import AOC

# runtime settings
sys.dont_write_bytecode = True

class Today:
	def __init__( self, filename ):
		self.filename = filename
		self.lines = None


	def loadFileIntoLines( self ):
		with open( self.filename ) as f:
			self.lines = [ line.rstrip('\n') for line in f ]



	def process( self ):
		count = 1
		accumulator = 0
		for line in self.lines:

			print "{}: |{}|".format( count, line )
			stringnumbers = line.split()

			if( len( stringnumbers ) == 0 ):
				continue

			# convert them to numbers
			numbers = map( int, stringnumbers )

			minval = int( min( numbers ))
			maxval = int( max( numbers ))
			difval = maxval - minval

			print ""
			print "{} - {} = {}".format( maxval, minval, difval )
			accumulator = accumulator + difval

			count = count + 1

		print "------"
		print "Result: {}".format( accumulator )

def iseven( val ):
	if( (val & 1) == 0 ):
		return True
	return False

def shellFor( val ):
	#sq = math.ceil( math.sqrt( sample ))
	if( val <= 1 ):
		return 0
	for x in range( 1, 10000, 2 ):
		if( x*x >= val ):
			return x-2
	return 0

#	Shell	range	factor	qodd	linear	8th
#	0	1-1	1	1 	0	0
#	1	2-9	9	3 	8	1
#	2	10-25	25	5 	16	2
#	3	26-49	49	7 	24	3
#	4	50-81	81	9	32	4

# shell is distance from center.

def shellInfo( shell, val ):
	qodd = ((1+shell)*2)-1
	factor = qodd * qodd
	loval = (qodd-2) * (qodd-2)	# min on this level
	hival = factor			# max on this level
	circumference = (qodd * 4) - 4	# "walk around" distance
	result = 0
	
 	e  = loval + (1 * shell)
	ne = loval + (2 * shell)
	n  = loval + (3 * shell)
	nw = loval + (4 * shell)
	w  = loval + (5 * shell)
	sw = loval + (6 * shell)
	s  = loval + (7 * shell)
	se = loval + (8 * shell)

	# 	NW  Q3   N   Q2  NE 
	#	Q4               Q1
	#	 W                E
	#	Q5	         Q0
	#	SW  Q6   S   Q7  SE

	# if value <= NE, return shell+ (abs( E-Value ))
	# if value <= NW, return shell+ (abs( N-Value ))
	# if value <= SW, return shell+ (abs( W-Value ))
	# if value <= SE, return shell+ (abs( S-Value ))

	if   ( val <= ne ): result = shell + abs( e-val ) 
	elif ( val <= nw ): result = shell + abs( n-val )
	elif ( val <= sw ): result = shell + abs( w-val )
	else              : result = shell + abs( s-val )


	return [ result,
		 loval, hival,
		"--", e, ne, n, nw, w, sw, s, e
		 ]

if __name__ == "__main__":
	sample = 289326

	#	37  36  35  34  33  32  31
	#	38  17  16  15  14  13  30
	#	39  18   5   4   3  12  29
	#	40  19   6   1   2  11  28
	#	41  20   7   8   9  10  27
	#	42  21  22  23  24  25  26
	#	43  44  45  46  47  48  49

	# center diagonals:
	#	1^2, 3^2, 5^2 7^2 ... (odds)^2

	samples = [ 2, 3,  8, 9, 10, 12, 23, 1024, sample ]
	answers = [ 1, 2,  1, 2,  3,  3,  2,   31,     -1 ]

	idx = 0
	for x in samples: #range( 1, 50 ):
		shell = (shellFor( x )+1)/2

		print "{:<6}: ({:<2}) shell {:<3}: {}".format(
			x, answers[idx],
			shell,
			shellInfo( shell, x ))
		idx = idx+1
	
	sys.exit()

	maxx = 0
	for x in range( 0, 10000, 2 ):
		if( x*x > sample ):
			break
		print "{}: {} {}".format( x, x*x, sample )
		maxx = x

	print "Max was {}.".format( maxx )
		

	sys.exit
	for data in sample2:
		print '---------------'
		d = Day2( data )
		d.process()
