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

my @links;

my $c = 0;

foreach $line ( @lines ) 
{
	$first = substr( $line, 5, 1 );
	$then = substr( $line, 36, 1);
	printf( "%d: %s ~~> %s\n", $c, $first, $then );

	$links[ $c ][0] = $first;
	$links[ $c ][1] = $then;
	$c++;
}

#printf( "-----\n" );
#print Dumper \@links;

# now, to find available moves, 
printf( "~~~~~\n" );

$result = '';

$doLoop = 1;
while( $doLoop == 1 ) {

	# build a todo list of all items that are in the 
	#	FROM column but not on the THEN column 
	my %todo;
	for( $j = 0 ; $j < scalar( @links ) ; $j ++ ) 
	{
		$first = $links[$j][ 0 ];
		$then = $links[$j][ 1 ];

		if( $first ne '' ) { 
			printf( "--- Checking %s\n", $first );
			
			$inThenList = 0;
			for( $i = 0 ; $i < scalar( @links ) ; $i ++ ) 
			{
				my $thisFirst = $links[ $i ][0];
				my $thisThen = $links[ $i ][1];

				if( $thisThen eq $first ) {
					$inThenList = 1;
				}
			}
			if( $inThenList eq 0 ) {
				$todo{ $first }++;
			}
		}
	}

	print( "Available next steps:\n" );
	@ava = sort keys %todo;
	if( scalar @ava == 0 )  {
		printf( "No more steps to do!\n" );	
		$doLoop = 0;
	} else {
		print Dumper( @ava );

		@ava = sort @ava;
		print Dumper( @ava );

		$step = shift( @ava );
		print( "Doing $step\n" );

		$result .= $step;
		# remove it from the lists and add new options

		# perform step?
		for( $j = 0 ; $j < scalar( @links ) ; $j++ ) 
		{
			$first = $links[ $j ][0];
			$then = $links[$j][ 1 ];
			if( $first eq $step ) {
				undef( $links[ $j ] );
				if( $then ne '' ) {
					$links[ $c ][0] = $then;
					$links[ $c ][1] = '';
					$c++;
				}
			}
		}
	}
}

print "Result is $result\n";
