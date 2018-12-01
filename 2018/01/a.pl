

$filename = "input1.txt";

open my $handle, '<', $filename;
chomp(my @lines = <$handle>);
close $handle;

#@lines = split( /,/,"+1,-1" );
#@lines = split( /,/,"+3,+3,+4,-2,-4" );
#@lines = split( /,/,"-6,+3,+8,+5,-6" );

$acc = 0;

my %counts;

$part2 = -1;
$foundPart2 = 0;

$run = 1;
while( $run ) {
	foreach $item( @lines ) 
	{
		printf " %d  %10s  -> ", $acc, $item;

		$op = substr( $item, 0, 1);
		$value = 0 + substr( $item, 1 );

		if( $op eq '-' ) {
			print( "--" );
			$acc = $acc - $value;
		}

		if( $op eq '+' ) {
			print( "++" );
			$acc = $acc + $value;
		}

		printf " %d\n", $acc;
		
		$key = sprintf( "val %d", $acc );

		$counts{ $key }++;

		#printf( "  %s -> %d\n", $key, $counts[ $key ] );
		#printf "  %s ~~ %s ===> %d\n", $op, $value, $acc;

		# part b
		if( $counts{ $key } > 1 ) {
			$run = 0;
			printf "FOUND REPEAT! (%d)\n", $acc;
			if( !$foundPart2 ) {
				$foundPart2 = 1;
				$part2 = $acc;
			}
		}
	}
}

printf "Final ACC = %d\n", $acc;

printf "-------------\n";

foreach $k( keys %counts )
{
	printf "cc  %10s => %d\n", $k, $counts{ $k };
}



printf "part 2: %s\n", $part2;
