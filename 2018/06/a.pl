#!/usr/bin/perl

$filename = "input.txt";

# load sample? from command line
$x = shift;
if( $x ne "" ) {
	$filename = $x;
}

printf "Using input file %s\n", $filename;

open my $handle, '<', $filename;
chomp(my @lines = <$handle>);
close $handle;

# load sample from string
#@sample = split /\n/,<<EOB;
#dabAcCaCBAcCcaDA
#EOB
#@lines = @sample;


# load in the coordinates into an array.
my @coords;

$item = 0;
foreach $line ( @lines ) 
{
	@co = split ', ', $line;
	$x = $co[0];
	$y = $co[1];
	
	printf( "%4d, %4d\n", $x, $y );
	$coords[ $item ][0] = $x;
	$coords[ $item ][1] = $y;
	$item++;
}

# determine extents
$nCoords = scalar @coords;
$minx = 9999;
$miny = 9999;
$maxx = 0;
$maxy = 0;

for( $i=0 ; $i < $nCoords ; $i++ )
{
	$x = $coords[$i][0];
	$y = $coords[$i][1];

	if( $x < $minx ) { $minx = $x; }
	if( $x > $maxx ) { $maxx = $x; }
	if( $y < $miny ) { $miny = $y; }
	if( $y > $maxy ) { $maxy = $y; }

	printf( "Coord %d of %d:  %d,%d\n", $i, $nCoords, 
			$coords[$i][0],
			$coords[$i][1] );
}
printf( "Extents:  %d,%d - %d,%d\n", $minx, $miny, $maxx, $maxy );


# so the process:
#	1. read in the file, into an array of x,y (above)
#	2. determine extents
#	3. foreach item within the extents, determine the least distanced object
#	4. remove all that match the outer edge (infinites)
#	5. count up the occurrences of each

sub dist
{
	my $x1 = shift;
	my $y1 = shift;
	my $x2 = shift;
	my $y2 = shift;

	return abs( $x1-$x2 ) + abs( $y1-$y2 );
}

my @results;

# compute distances
for( $cy = $miny ; $cy <= $maxy ; $cy++ )
{
	for( $cx = $minx ; $cx <= $maxx ; $cx++ )
	{
		$currentMin = 99999;
		$currentMinItem = ' xxx';

		for( $i=0 ; $i < $nCoords ; $i++ )
		{
			$x = $coords[$i][0];
			$y = $coords[$i][1];
			$dst = dist( $cx, $cy, $x, $y );

			if( $dst == $currentMin ) {
				$currentMinItem = ' ...';
			}
			if( $dst < $currentMin ) {
				$currentMinItem = sprintf( ' %03d', $i );
				$currentMin = $dst;
			}
		}
		$results[ $cx ][ $cy ][0] = $currentMin;
		$results[ $cx ][ $cy ][1] = $currentMinItem;

		#printf( "At %3d,%3d, min is %d (%s)\n",
		#		$cx, $cy, $currentMin, $currentMinItem );
	}
}


sub eraseFromArray
{
	my $itm = shift;
	if( $itm eq ' ...' ) { return; }
	if( $itm eq ' ___' ) { return; }
	printf( "Erasing element [%s]\n", $itm );

	for( my $cy = $miny ; $cy <= $maxy ; $cy++ ) {
		for( my $cx = $minx ; $cx <= $maxx ; $cx++ ) {
			my $ci = $results[ $cx ][ $cy ][1];
			if( $ci eq $itm ) {
				$results[ $cx ][ $cy ][1] = ' ___';
			}
		}
	}
}

# determine items on the edges
printf( "Removing items from edges..\n" );

# top/bottom 
for( my $cy = $miny ; $cy <= $maxy ; $cy++ ) {
	eraseFromArray( $results[ $minx ][ $cy ][1] );
	eraseFromArray( $results[ $maxx ][ $cy ][1] );
}
for( my $cx = $minx ; $cx <= $maxx ; $cx++ ) {
	eraseFromArray( $results[ $cx ][ $miny ][1] );
	eraseFromArray( $results[ $cx ][ $maxy ][1] );
}

# count totals.
my %totals;

for( $cy = $miny ; $cy <= $maxy ; $cy++ ) {
	for( $cx = $minx ; $cx <= $maxx ; $cx++ ) {
		print( $results[ $cx ][ $cy ][1] );
		$min = $results[ $cx ][ $cy ][0];
		$item = $results[ $cx ][ $cy ][1];

		$totals{ $item }++;
		#printf( "%s => %d\n", $item, $totals[ $item ] );
	}
	printf( "\n" );
}

# print totals
$max = 0;
$maxItm = '';
foreach $itm ( keys %totals )
{
	printf( "%8s => %d\n", $itm, $totals{ $itm } );
	if( 
		( $itm ne ' ...' ) &&
		( $itm ne ' ___' ) ) {

		if( $totals{ $itm } > $max ) {
			$max = $totals{ $itm };
			$maxItm = $itm;
		}
	}
}

printf "Max region is %s with %d\n", $maxItm, $max;

if( $part == 1 ) {
}

