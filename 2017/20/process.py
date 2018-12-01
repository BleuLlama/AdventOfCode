#!/usr/bin/python

import sys
import os.path
sys.dont_write_bytecode = True
sys.path.append( '../libs' )
from libAOC import AOC

class Particle:
	def __init__( self, line, index ):
		components = line.split( ', ' )
		self.p = self.parseNums( components[0] )
		self.v = self.parseNums( components[1] )
		self.a = self.parseNums( components[2] )
		self.index = index
		self.closest = 0
		self.active = True

	def parseNums( self, s ):
		s = s[s.find("<")+1:s.find(">")]
		n = map( int, s.split( ',' ))
		return n

	def dump( self, ll ):
		for l in ll:
			print "{}".format( l )

	def updateTick( self ):
		if not self.active:
			return
		self.v[0] += self.a[0]
		self.v[1] += self.a[1]
		self.v[2] += self.a[2]

		self.p[0] += self.v[0]
		self.p[1] += self.v[1]
		self.p[2] += self.v[2]

	def getDistance( self ):
		if not self.active:
			return 999999
		return abs( self.p[0] ) + abs( self.p[1] ) + abs( self.p[2] )

class Today:
	def __init__( self, d ):
		print "{}".format( d )
		self.a = AOC( d )
		self.a.loadFileIntoLines()

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
		self.a.dump()
		self.particles = list();

		# create them
		i = 0
		for line in self.a.data:
			p = Particle( line, i )
			self.particles.append( p )
			i += 1

		# iterate
		for x in range( 0, 1000):
			closest = -1
			closestD = 999999
			# update 
			for particle in self.particles:
				if particle.active:
					particle.updateTick()
					distance = particle.getDistance()
					if distance < closestD:
						closest = particle.index
						closestD = distance
					print "{}> {}: {}  {}".format( x, particle.index, distance, particle.p )

			# collision check
			for particle in self.particles:
				if particle.active:
					# get this one
					# loop over the others for them
					for p2 in self.particles:
						if p2.active and p2.index != particle.index and particle.p[0] == p2.p[0] and particle.p[1] == p2.p[1] and particle.p[2] == p2.p[2]:

							print "COLLISION!  {} {}".format( p2.index, particle.index )
							# COLLISION!!!
							p2.active = False
							particle.active = False

			# find the closest
			self.particles[closest].closest += 1
			print "Closest: {} at {}".format( closest, self.particles[closest].getDistance())

		# find highest score
		highScore = 0
		highScoreI = -1
		nActive = 0
		for particle in self.particles:
			if particle.active:
				nActive += 1
			if particle.closest > highScore:
				highScore = particle.closest
				highScoreI = particle.index

		print "Highest Score: particle {} with {}".format( highScoreI, highScore )
		print "N Active (not collided): {}".format( nActive )

if __name__ == "__main__":
	datas = [
		'input.txt',
	]
	d2 = [
		'sample2.txt',
		'sample.txt',
	]

	for data in datas:
		d = Today( data )
		d.process( 1 )
		#d.process2( )
