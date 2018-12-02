

$filename = "input.txt";

open my $handle, '<', $filename;
chomp(my @lines = <$handle>);
close $handle;

#@lines = split( /,/,"abcdef,bababc,abbcde,abcccd,aabcdd,abcdee,ababab");

@xlines= split /\n/,<<EOB;
abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz
EOB

$acc = 0;

my %counts;

$part2 = -1;
$foundPart2 = 0;

$tot2 = 0;
$tot3 = 0;

$run = 2;

if( $run == 1 ) {
	foreach $item ( @lines ) 
	{
		@ch = split //, $item;
		my %ch;
		foreach $x( @ch ) {
			$ch{ $x }++;
		}

		$twos = 0;
		$threes = 0;
		foreach $k( keys %ch ) {
			printf( "%2s -> %s\n", $k, $ch{ $k } );
			if( $ch{ $k } == 2 ) { $twos++; }
			if( $ch{ $k } == 3 ) { $threes++; }
		}

		if( $twos > 0 ) { $tot2++ }
		if( $threes > 0 ) { $tot3++ }
		printf( "twos: %d   threes: %d\n", $twos, $threes );

	}

	printf( " #2: %d  #3: %d   =>  %d\n", $tot2, $tot3, ($tot2 * $tot3 ));
	exit;
}

print( "part two" );


sub nDiffs 
{
	my $a = shift;
	my $b = shift;

	my $i = 0;

	printf "Compare: %s %s\n", $a, $b;

	if( length( $a ) != length( $b ) ){ return 9999; }

	$nDiff = 0;
	for( $i = 0 ; $i < length( $a ) ; $i++ ) {
		if( substr( $a, $i, 1 ) ne substr( $b, $i, 1 ) ) {
			$nDiff++;
		}
	}

	return $nDiff;
}

printf "-------------\n";
	
	$totallowestA = 'xxx';
	$totallowestB = 'yyy';
	$totallowestX = 9999;

	$lowestA = '';
	$lowestB = '';
	$lowestX = 9999;

	foreach $item ( @lines ) 
	{
		printf( "\nLine: %s\n", $item );
		$lowestA = '';
		$lowestB = '';
		$lowestX = 9999;

		foreach $i2 ( @lines )
		{
			$nd = nDiffs( $item, $i2 );
			if( $nd == 0 ) {
				# IT ME!
			} else { 
				if( $nd < $lowestX ) {
					$lowestA = $item;
					$lowestB = $i2;
					$lowestX = $nd;
				}
			}
		}
		printf( "Local Lowest (%d) = %s\n", $lowestX, $lowestB );

		if( $lowestX < $totallowestX ) {
			$totallowestX = $lowestX;
			$totallowestA = $lowestA;
			$totallowestB = $lowestB;
		}
		
	}
		
	printf( "Total Lowest (%d) = %s %s\n", 
		$totallowestX, $totallowestA, $totallowestB );
	printf( "    %s\n", $totallowestA );
	printf( "    %s\n", $totallowestB );

