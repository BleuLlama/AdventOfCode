#!/usr/bin/perl

use Data::Dumper;

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

$idx = 0;

@elements = split /\s+/, $lines[0];

print Dumper \@elements;

$childid = 0;

$idx = 0;

sub parseElement1
{
	my $idno = $childid++;
	printf( "Child %d starting at %d\n", $idno, $idx );

	# header
	my $nChildren = $elements[ $idx++ ];
	my $nMetas    = $elements[ $idx++ ];

	my $metasum = 0;
	for( my $i = 0 ; $i < $nChildren ; $i++ ) {
		$metasum += parseElement1( $idx );
	}
	for( my $i = 0 ; $i < $nMetas ; $i++ ) {
		my $meta = $elements[ $idx++ ];
		printf( "     %d meta: %d\n", $idno, $meta );
		$metasum += $meta;
	}
	return $metasum;
}

$idx = 0;
my $part1Sum = parseElement1();

printf( "part 1: %d\n", $part1Sum );

printf( "------------------\n\n" );



sub parseElement2
{
	my $sp = shift;
	my $idno = $childid++;
	printf( $sp . "%d starting at %d\n", $idno, $idx );
	$sp .= '  ';

	# header
	my $nChildren = $elements[ $idx++ ];
	my $nMetas    = $elements[ $idx++ ];
	printf( $sp . "%d has %d children, %d metas\n", $idno, $nChildren, $nMetas );

	my $metasum = 0;
	my %childSums;

	for( my $i = 0 ; $i < $nChildren ; $i++ ) {
		$tval = parseElement2( $sp . '   ' );
		printf( $sp . "Child %d value = %d\n", $i, $tval );
		$childSums{ $i } = $tval;
	}
	printf $sp . "Child sums:", $idno;
	print Dumper \%childSums;

	for( my $i = 0 ; $i < $nMetas ; $i++ ) {
		my $meta = $elements[ $idx++ ];
		if( $nChildren == 0 ) {
			printf( $sp . "%d meta immediate: %d\n", $idno, $meta );
			$metasum += $meta;
		} else {
			if( exists( $childSums{ $meta -1 } ) ) {
				printf( $sp . "%d meta ref: %d -> %d\n", 
						$idno, $meta, $childSums{ $meta -1 } );
				$metasum += $childSums{ $meta -1 };
			}
		}
	}
	printf $sp . "%d: Returning %d\n", $idno, $metasum;
	return $metasum;
}

$childid = 0;
$idx = 0;
my $part2Sum = parseElement2( '' );
printf( "part 2: %d\n", $part2Sum );

