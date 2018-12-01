#!/usr/bin/python

import sys
import os.path
sys.dont_write_bytecode = True
sys.path.append( '../libs' )
from libAOC import AOC

class Node:
	name = None
	weight = 0
	children = []
	indent = ' ' * 3

	def __init__( self, name, weight ):
		self.name = name
		self.weight = weight
		self.sums = 0
		self.children = []

	def addChild( self, kidname, kidweight ):
		newnode = Node( kidname, kidweight )
		self.children.append( newnode )

	def dump( self, indent='' ):
		if indent == '':
			print( "---- Tree Dump ----" )
		    
		print( "{}+ {}  {} (weight {}) (sum {})".format( 
			indent,
			self.sums,
			self.name,
			self.weight,
			self.sums ))
		for kid in self.children:
			kid.dump( indent + self.indent )

	def computeSums( self ):
		self.sums = self.weight
		if len( self.children ) > 0:
			for kid in self.children:
				self.sums += kid.computeSums()
		return self.sums

	def find( self, name ):
		if self.name == name:
			return self
		if len( self.children ) > 0:
			for kid in self.children:
				i = kid.find( name )
				if not i == None:
					return i
		return None;

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

	nodes = {}
	children = {}
	parents = {}
	balanced = {}
	rootnode = None

	def computeWeight( self, node ):
		r = self.nodes[ node ]
		kids = self.children.get( node )
		if not kids is None:
			for kid in kids:
				r = r + self.computeWeight( kid )
		return r

	tree = None


	def addKidsTo( self, nodeName ):
		for parent, kids in self.children.items():
			if parent == nodeName:
			    	p = self.tree.find( parent )
				for kid in kids:
					p.addChild( kid, self.nodes[ kid ])
					self.addKidsTo( kid )

	def process2( self ):
		self.a.dump()

		for datum in self.a.data:
			#self.a.write( '.' )
			print "{}".format( datum )
                        halves = [ z.strip() for z in datum.split( '->' )]

			name = halves[0].split()[0]

			# store the weight
			weight = self.a.extract( halves[0] )
			self.nodes[ name ] = int( weight )
			#print "  |{}|{}|".format( name, weight )

			# store the children, parents in arrays
			if( len( halves) > 1 ):
				kids = [ z.strip() for z in halves[1].split( ',' )]
				self.children[ name ] = kids

				for kid in kids:
					self.parents[ kid ] = name

		# ----------------------------------------
		self.a.dumpDict( "Nodes", self.nodes )
		self.a.dumpDict( "Children", self.children )
		self.a.dumpDict( "Parents", self.parents )

		for nodename in self.nodes:
			k2 = self.parents.get( nodename )
			if k2 is None :
				self.rootnode = nodename

		print "PART 1: {} is the root node!".format( self.rootnode )

		# ----------------------
		# build the tree

		self.tree = Node( self.rootnode, self.nodes[ self.rootnode ])
		self.addKidsTo( self.rootnode )
		self.tree.computeSums( )

		self.tree.dump()

		return

	def process( self, step ):
		self.a.dump()

		for datum in self.a.data:
			#self.a.write( '.' )
			print "{}".format( datum )
                        halves = [ z.strip() for z in datum.split( '->' )]

			name = halves[0].split()[0]

			# store the weight
			weight = self.a.extract( halves[0] )
			self.nodes[ name ] = int( weight )
			#print "  |{}|{}|".format( name, weight )

			# store the children, parents
			if( len( halves) > 1 ):
				kids = [ z.strip() for z in halves[1].split( ',' )]
				self.children[ name ] = kids

				for kid in kids:
					self.parents[ kid ] = name

			# prefill balanced
			self.balanced[ name ] = None

		# ----------------------------------------
		self.a.dumpDict( "Nodes", self.nodes )
		self.a.dumpDict( "Children", self.children )
		self.a.dumpDict( "Parents", self.parents )

		# ----------------------------------------
		for nodename in self.nodes:
			k2 = self.parents.get( nodename )
			if k2 is None :
				self.rootnode = nodename

		print "Result 1: Root node: {}".format( self.rootnode )

		# ----------------------------------------

		# compute all the weights
		for nodename in self.nodes:
			w = self.computeWeight( nodename )
			print "weight: {}: {}".format( nodename, w )

		# figure out imbalances
		unbalanced = None
		for parent, kids in self.children.items():
			print "Family >>{} {}".format( parent, kids )

			i = -1
			for kid in kids:
				j = self.computeWeight( kid )
				if i is -1:
					i = j
				elif i != j:
					unbalanced = parent
				
		# ok. we got the unbalanced parent
		# no checking!
		print "{} is unbalanced.".format( unbalanced )
		cv = {}
		for kid in self.children[ unbalanced ]:
			w = self.computeWeight( kid )
			print "{} -> {}".format( kid, w)
			ov = cv.get( w )
			if ov is None:
				ov = 0
			cv[ w ] = ov + 1

		wrong  = -1
		common = -1
		for key,cnt in cv.items():
			if cnt is 1:
				wrong = key
			else:
				common = key

		print( "-----" )
		print( "wrong: {} common:{}".format( wrong, common ))

		wrongname = ''
		valwrong = -1
		valcommon = -1
		for kid in self.children[ unbalanced ]:
			w = self.computeWeight( kid )
			if wrong == w:
				wrongname = kid
				valwrong = w
			else:
				valcommon = w
			print " fam: {} {} {}".format( wrong, w, kid )

		diffval = valcommon-valwrong
		print( "{} is wrong by {}".format( wrongname, diffval ))

		weight = self.nodes[wrongname]
		print( "weight of {} is {}".format( wrongname, weight ))
		print( "result 2 is {}".format( weight + diffval ))

if __name__ == "__main__":
	datas = [
		'input.txt' ]
	junk = [
		'example.txt' ]

	for data in datas:
		print '---------------'
		d = Today( data )
		#d.process( 1 )
		d.process2()
