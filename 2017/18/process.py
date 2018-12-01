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
		self.a.loadFileIntoLines()
		self.regs = {}
		self.sendQ = []

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

	def regStore( self, reg, val ):
		self.regs[ reg.upper() ] = val;

	def representsInt( self, s ):
		try: 
			int(s)
			return True
		except ValueError:
			return False
		return False

	def dereferenceRead( self, param ):
		if( self.representsInt( param )):
			return int( param )
		return int( self.regs.get( param.upper(), 0 ))

	def dumpRegs( self ):
		self.a.dumpDict( "Registers", self.regs )

	def dumpQ( self ):
		self.a.dump( "Send Queue", self.sendQ )

	def process( self, programID ):
		self.regStore( 'p', programID )
		self.a.dump();

		pc = 0
		sound = 0

		while True:
			argv = self.a.data[pc].split()
			pc = pc+1
			#print ">> {}  {}".format( len( argv), line )
			opcode = argv[0]
			#print "  {}".format( opcode )
			drx = 0
			x = 0
			dry = 0
			y = 0

			if( len(argv) > 1 ):
				x = argv[1]
				drx = self.dereferenceRead( x )
			if( len(argv) > 2 ):
				y = argv[2]
				dry = self.dereferenceRead( y )

			if( opcode == 'snd' ):
				print " SND: send( {} )".format( drx )
				self.sendQ.append( drx )

			elif( opcode == 'set' ):
				print " SET: {} = {}".format( x, dry )
				self.regStore( x, dry )

			elif( opcode == 'add' ):
				print " ADD: {} = {} + {}".format( x, drx, dry )
				self.regStore( x, drx + dry );

			elif( opcode == 'mul' ):
				print " MUL: {} = {} * {}".format( x, drx, dry )
				self.regStore( x, drx * dry );

			elif( opcode == 'mod' ):
				print " MOD: {} = {} % {}".format( x, drx, dry )
				self.regStore( x, drx % dry );

			elif( opcode == 'rcv' ):
				if( drx != 0 ):
					print " RCV: RX >>> {} ({})".format( drx, self.sendQ[-1] )
					self.regStore( x, self.sendQ[-1] )
					self.dumpRegs()
					self.dumpQ()
					return
				else :
					print " RCV: >>> {} (skipped)".format( drx )

			elif( opcode == 'jgz' ):
				print " JGZ: if {}>0, JMP {}".format( drx, dry )
				if( drx > 0 ):
					pc = pc -1 + dry

			else:
				print " Unknown opcode: {}".format( opcode )


if __name__ == "__main__":
	datas = [
		'input.txt',
	]
	datas2 = [
		'sample.txt',
		'input.txt',
	]

	for data in datas:
		d = Today( data )
		d.process( 0 )
