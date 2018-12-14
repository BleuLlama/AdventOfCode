/*
 * Day X
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "../clib/aoclib.h"

#define kStep2Max	(200*1024*1024)

unsigned long idx0 = 0;
unsigned long idx1 = 1;

char * r = NULL;
unsigned long lastr = 0;

void addToEnd( char c )
{
	if( c >= 10 ) {
		addToEnd( 1 );
		c = c - 10;
	}
	r[ lastr ] = c;
	lastr++;
}

void setup( int val )
{
	r = (char *) malloc( sizeof( int ) * (val+20));;
	lastr = 0;
	idx0 = 0;
	idx1 = 1;
	r[0] = '\0';
	addToEnd( 3 );
	addToEnd( 7 );
}

void step()
{
	int v;

	// elf sum values
	v = r[ idx0 ] + r[ idx1 ];
	// add to the end
	addToEnd( v );

	// move the elves
	idx0 = ( idx0 + r[ idx0 ] + 1 ) % lastr;
	idx1 = ( idx1 + r[ idx1 ] + 1 ) % lastr;
}

void dump()
{
	for( unsigned long i=0 ; i<lastr ; i++ )
	{
/*
		printf( "%c%d%c",
			(i==idx0)?'[':' ',
			r[i],
			(i==idx1)?']':' ' );
*/
		if( i == idx0 && i == idx1 ) {
			printf( "(%d]", r[i] ); 
		}
		else if( i == idx0 ) { printf( "(%d)", r[i] ); }
		else if( i == idx1 ) { printf( "[%d]", r[i] ); }
		else { printf( " %d ", r[i] ); }
	}
	printf( "\n" );
}

void tightdump()
{
	for( unsigned long i=0 ; i<lastr ; i++ )
	{
		printf( "%d", r[i] ); 
		if( i%100 == 0 ) printf( "\n" );
	}
	printf( "\n" );
}

void go_step1( int count )
{
	for( int i=0 ; i<(count+10) ; i++ )
	{
		//dump();
		//printf( "%d ", i ); fflush( stdout );
		step();
	}
}

void go_step2( char * match )
{
	unsigned long mlen;
	mlen = strlen( match );

	printf( "Looking for |%s|(%ld)\n", match, mlen );

	for( int j=0 ; j < mlen ; j++ ) {
		match[j] = match[j] - '0';
	}
	// it's now a buffer of chars to match with

	for( unsigned long i=0 ; i < kStep2Max ; i++ )
	{
		step();

		if( lastr > mlen ) {
			// check end
			for( int Q = -2 ; Q < 1 ; Q++ ) 
			{
				int diff = 0;
				for( int k = 0 ; k < mlen; k++ ) 
				{
					if( match[k] != r[ lastr-mlen+k+Q ] )
					{
						diff = 1;
					}
		
				}

				if( !diff ) { 
					//tightdump();
					printf( "Matched at %ld\n", lastr-mlen+Q );
					return;
				}
			}
		}
	}
	printf( "Didn't find it after %d steps.\n", kStep2Max );
	
}

void showFrom( int pos )
{
	printf( "Value: " );
	for( int i=pos ; i<pos+10 ; i++ )
	{
		printf( "%d", r[i] );
	}
	printf( "\n" );
}

int main( int argc, char ** argv )
{
	if( argc != 2 ) {
		printf( "Usage: %s value\n", argv[0] );
		exit(-1);
	}
	int val = atoi( argv[1] );
	printf( "Running to %d\n", val );

	setup( val );
	go_step1( val );
	showFrom( val );

	free( r );

	setup( kStep2Max );
	go_step2( argv[1] );

	return 0;
}
