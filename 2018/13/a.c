/*
 * Day X
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../clib/aoclib.h"

char ** rows = NULL;

struct CART {
	int x;
	int y;
	char c;		// cart facing < v < >
	char track;
	int turnChoice;
};

struct CART carts[20];
int nCarts = 0;

void go( char * filename )
{
	rows = aoc_LoadInFile( filename );
//	aoc_PrintCCBuf( rows );

	// find the carts
	int y = 0;
	while( rows[y] != NULL ) {
		for( int x=0 ; rows[y][x] != '\0' ; x++ ) {
			char ch = rows[y][x];
			if( ch == '^' || ch == 'v' || ch == '<' || ch == '>' ) {
				carts[ nCarts ].turnChoice = 0;
				carts[ nCarts ].x = x;
				carts[ nCarts ].y = y;
				carts[ nCarts ].c = ch;
				printf( "Cart %c is at %d, %d\n", ch, x, y ); 
				// figure out the track under it.
				
				char n = (y>0)?rows[y-1][x] : ' ';
				char s = (rows[y+1])?rows[y+1][x] : ' ';

				char e = (x>0)?rows[y][x-1] : ' ';
				char w = rows[y][x+1];
				if( ch == '^' || ch == 'v' ) {
					carts[ nCarts ].track = '|';
				} else {
					carts[ nCarts ].track = '-';
				}
				
				nCarts++;
			}
		}
		y++;
	}

	printf( "%d carts found:\n", nCarts );

	for( int i=0 ; i<nCarts ; i++ ) {
		printf( " %-2d: %c  %3d, %-3d (over %c) \n", 
			i, carts[i].c, carts[i].x, carts[i].y, carts[i].track );
	}

	int crashes = 0;
	int fx = 0;
	int fy = 0;

	int tick = 0;

	while( crashes == 0 ) {
		tick++;
		// move them
		for( int i=0 ; i<nCarts ; i++ ) {
			int x = carts[i].x;
			int y = carts[i].y;

			// replace the track
			rows[y][x] = carts[i].track;

			// move the cart
			switch( carts[i].c ) {
			case( '^' ):	y--;	break;
			case( 'v' ):	y++;	break;
			case( '<' ):	x--;	break;
			case( '>' ):	x++;	break;
			default: 
				printf( "*ERROR*  Don't know what cart %d is!\n", i );
				break;
			}

			// store the new position
			carts[i].x = x;
			carts[i].y = y;

			// check for collision
			char trackUnder = rows[y][x];
			int c = carts[i].c;

			switch( trackUnder ){
			case( '^' ):
			case( 'v' ):
			case( '<' ):
			case( '>' ):
				if( crashes == 0 ) {
					fx = x;
					fy = y;
				}
				printf( "COLLISION AT %d,%d!\n", x, y );
				crashes++;
				break;

			// check for turn options
			case( '+' ):
				if( carts[i].turnChoice == 0 ) {
					// left turn
						 if( c == '^' ) c = '<';
					else if( c == 'v' ) c = '>';
					else if( c == '<' ) c = 'v';
					else if( c == '>' ) c = '^';
				} else if( carts[i].turnChoice == 1 ) {
					// straight
						// no change
				} else if( carts[i].turnChoice == 2 ) {
					// right turn
						 if( c == '^' ) c = '>';
					else if( c == 'v' ) c = '<';
					else if( c == '<' ) c = '^';
					else if( c == '>' ) c = 'v';
				}

				// adjust for the next one
				carts[i].turnChoice++;
				if( carts[i].turnChoice > 2 ) {
					carts[i].turnChoice = 0;
				}
				break;

			// check for rotation
			case( '/' ):
					 if( c == '^' ) c = '>';
				else if( c == 'v' ) c = '<';
				else if( c == '<' ) c = 'v';
				else if( c == '>' ) c = '^';
				break;
			case( '\\' ):
					 if( c == '^' ) c = '<';
				else if( c == 'v' ) c = '>';
				else if( c == '<' ) c = '^';
				else if( c == '>' ) c = 'v';
				break;
			default:
				break;
			}
			carts[i].c = c;

			// store the track
			carts[i].track = trackUnder;
			rows[y][x] = carts[i].c;

			printf( "%-2d: %c  %3d, %-3d (over %c) \n", 
				i, carts[i].c, carts[i].x, carts[i].y, carts[i].track );

			//printf( "[2J" );	// cls
			//printf( "[;H" ); // home
			printf( "Tick %d, Step %d\n", tick, i );
			for( int yy=0; yy < 12 && rows[yy]; yy++ ) printf( "  %s\n", rows[yy] );
		}
	}
	printf( "First collision at %d,%d!\n", fx, fy );
}


int main( int argc, char ** argv )
{
	if( argc != 2 ) {
		printf( "Usage: %s <filename>\n", argv[0] );
		exit(-1);
	}

	go( argv[1] );

	return 0;
}
