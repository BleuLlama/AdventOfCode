/*
 * Day 12?
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define TEST

#ifdef TEST
#endif


struct LUTENTRY {
	char match[7];
	char becomes;
};

#ifndef TESTING

char * initial = "##.###.......#..#.##..#####...#...#######....##.##.##.##..#.#.##########...##.##..##.##...####..####";

struct LUTENTRY lut[] = {
    { "#.#.#", '#' },
    //{ ".##..", '.' },
    //{ "#.#..", '.' },
    { "..###", '#' },
    { ".#..#", '#' },
    //{ "..#..", '.' },
    { "####.", '#' },
    { "###..", '#' },
    //{ "#....", '.' },
    { ".#.#.", '#' },
    //{ "....#", '.' },
    { "#...#", '#' },
    { "..#.#", '#' },
    { "#..#.", '#' },
    { ".#...", '#' },
    //{ "##..#", '.' },
    //{ "##...", '.' },
    //{ "#..##", '.' },
    { ".#.##", '#' },
    //{ ".##.#", '.' },
    { "#.##.", '#' },
    //{ ".####", '.' },
   // { ".###.", '.' },
    //{ "..##.", '.' },
    //{ "##.#.", '.' },
    { "...##", '#' },
    //{ "...#.", '.' },
    //{ ".....", '.' },
    //{ "##.##", '.' },
    { "###.#", '#' },
    { "#####", '#' },
    //{ "#.###", '.' },
	{ "", '.' }
};
#else
char * initial = "#..#.#..##......###...###";

struct LUTENTRY lut[] = {
    { "...##", '#' },
    { "..#..", '#' },
    { ".#...", '#' },
    { ".#.#.", '#' },
    { ".#.##", '#' },
    { ".##..", '#' },
    { ".####", '#' },
    { "#.#.#", '#' },
    { "#.###", '#' },
    { "##.#.", '#' },
    { "##.##", '#' },
    { "###..", '#' },
    { "###.#", '#' },
    { "####.", '#' },
	{ "", '.' }
};
#endif


char findInLut( char * needle )
{
	int lutidx = 0;

	while( lut[ lutidx ].match[0] != '\0' )
	{
		if( !strncmp( needle, lut[ lutidx ].match, 5 )) {
			return lut[ lutidx ].becomes;
		}
		lutidx++;
	}
	return '.';
}

void test()
{
	printf( " Result ##.## %c\n", findInLut( "##.##" ));
	printf( " Result ##### %c\n", findInLut( "#####" ));
	printf( " Result ..... %c\n", findInLut( "....." ));
	printf( " Result xxxxx %c\n", findInLut( "xxxxx" ));
}

	//grid = (int **)malloc( sizeof( int* ) * 300 );


char * cGen;
char * nGen;
int genWidth;
int genPadding = 30;

void begin( void )
{
	genWidth = strlen( initial );

	cGen = (char *) malloc( genWidth+genPadding*2+1 );
	nGen = (char *) malloc( genWidth+genPadding*2+1 );

	memset( cGen, '.', genWidth+genPadding*2 );
	cGen[ genWidth+genPadding*2 ] = '\0';
	memset( nGen, '.', genWidth+genPadding*2 );
	nGen[ genWidth+genPadding*2 ] = '\0';
	
	for( int i=0 ; i < genWidth ; i++ ) {
		cGen[ i+genPadding ] = initial[ i ];
	}
}

void printGen( int g )
{
	int x=0;

	printf( "%-3d : ", g );
	
	// key
	for( int i =0 ; i < (genWidth + genPadding*2 ); i++ )
	{
		if( i < genPadding ) { 
			printf( " " );
		} else if( i == genPadding ) {
			printf( "0" );
		}
	}
	printf( "\n" );
	printf( "%-3d : ", g );

	// content
	for( int i =0 ; i < (genWidth + genPadding*2 ); i++ )
	{
		printf( "%c", cGen[i] );
	}


	printf( "\n" );
}

void generation( void )
{
	int l = strlen( cGen )-5;

	for( int pos = 0 ; pos < l ; pos++ ) {
		nGen[ pos+2 ] = findInLut( cGen + pos );
	}

	memcpy( cGen, nGen, genWidth + genPadding*2);
}

int countPots()
{
	int t=0;

	for( int pos = 0 ; pos < strlen( cGen ) ; pos++ )
	{
		if( cGen[ pos ] == '#' ) t += pos-genPadding;
		//printf( "%3d %c  %d\n", pos, cGen[ pos ], t );
	}
	return t;
}


int main( int argc, char ** argv )
{
	int gen = 0;

	begin();

	for( gen = 1 ; gen <= 20 ; gen++ )
	{
		generation();
		printGen( gen );
	}
	printf( "result = %d\n", countPots() );

	return 0;
}

int oldmain( int argc, char ** argv )
{
	if( argc != 2 ) {
		printf( "Usage: %s <SerialNo>\n", argv[0] );
		exit(-1);
	}
	return 0;
}
