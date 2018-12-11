
/*
#!/usr/bin/perl

use Data::Dumper;

my $sn = 8;

sub getPowerLevel
{
	my $x = shift;
	my $y = shift;

	my $rackID = $x + 10;
	my $pwrlev = $rackID * $y;
	$pwrlev += $sn;
	$pwrlev *= $rackID;

	$pwrlev = substr( $pwrlev, -3, 1 ) - 5;

	return $pwrlev;
}

@tests = (
	[ 3, 5,  8 ],
	[ 122, 79,  57 ],
	[ 217, 196, 39 ],
	[ 101, 153, 71 ],
);

printf( "---- tests -----\n" );
for( my $i = 0 ; $i < 4 ; $i++ ) 
{
	my $x = $tests[$i][0];
	my $y = $tests[$i][1];
	$sn = $tests[$i][2];
	printf( "$x,$y [$sn] = %d\n", getPowerLevel( $x, $y ) );
}

my $w=300;
my $h=300;
my @grid;
my @scores;
$sn = 5034;

# build the power levels
for( my $y = 0 ; $y <= $h ; $y++ ) 
{
	for( my $x = 0 ; $x<= $w ; $x++ ) 
	{
		$grid[ $x ][ $y ] = getPowerLevel( $x, $y );
	}
}

# dump it out
for( my $y = 0 ; $y <= $h ; $y++ ) 
{
	printf( "\n ($y) "  );
	for( my $x = 0 ; $x<= $w ; $x++ ) 
	{
		printf "% 3d ", $grid[ $x ][ $y ];
	}
	printf( "\n" );
}

# figure out 3x3 scores
$lrgVal = 0;
$lrgX   = 0;
$lrgY   = 0;
$lrgSZ	= 0;
$sz = 3;

for( $sz = 1 ; $sz <= 300 ; $sz++ ) 
{
	printf( "Trying size=$sz\n" );
	for( my $y = 0 ; $y < $h-$sz-1 ; $y++ )
	{
		for( my $x=0 ; $x < $w-$sz-1 ; $x++ )
		{
			$s = 0;
			for ( my $my ; $my < $sz ; $my++ ) {
				for ( my $mx ; $mx < $sz ; $mx++ ) {
					$s += $grid[ $x+$mx ][ $y+$my ];
				}
			}
			#$scores[$x][$y] = $s;

			if( $s > $lrgVal ) {
				$lrgVal = $s;
				$lrgX   = $x;
				$lrgY   = $y;
				$lrgSZ	= $sz;
			}
		}
	}
}

printf( "Largest score is $lrgVal at $lrgX,$lrgY,$lrgSZ\n" );
*/
#include <stdio.h>
#include <stdlib.h>

int ** grid;

void newGrid()
{
	grid = (int **)malloc( sizeof( int* ) * 300 );

	for( int i =0 ; i < 301 ; i++ ) 
	{
		grid[ i ] = (int *)malloc( sizeof( int ) * 300 );
	}
}

void populateGrid( int serno )
{
	int v=0;
	int v2;
	int rackid = 0;

	for( int x = 0 ; x < 300 ; x++ )
	{
		rackid = x+10;

		for( int y = 0 ; y < 300 ; y++ )
		{
			v = ((rackid * y)+serno)*rackid;
			v = v/100 - (10*(v/1000));
			v -= 5;
			grid[x][y] = v;
		}
	}
}

int highestV = -999;
int highestX;
int highestY;

void findHighest( int sz )
{
	int thisV;
	int mx, my;

	for( int x=0 ; x<(300-sz) ; x++ )
	{
		for( int y=0 ; y<(300-sz) ; y++ )
		{
			thisV = 0;
			for( mx=x ; mx < x+sz ; mx++ ) 
			{
				for( my=y ; my < y+sz ; my++ ) 
				{
					thisV += grid[ mx ][ my ];
				}
			}

			if( thisV > highestV ) {
				highestV = thisV;
				highestX = x;
				highestY = y;
				printf( "New highest: %d at %d,%d,%d\n", 
							highestV, highestX, highestY, sz );
			}
		}
	}
	
	printf( "Highest found %d at %d,%d,%d\n", 
			highestV, highestX, highestY, sz );
}

int main( int argc, char ** argv )
{
	int serno = 0;
	int sz = 0;

	if( argc != 2 ) {
		printf( "Usage: %s <SerialNo>\n", argv[0] );
		exit(-1);
	}
	newGrid();
	serno = atoi( argv[1] );
	printf( "SerialNumber: %d\n", serno );

	populateGrid( serno );

	for( sz=1; sz<300 ; sz++ ) {
		findHighest( sz );
	}

}
