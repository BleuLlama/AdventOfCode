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
