

$filename = "input.txt";

open my $handle, '<', $filename;
chomp(my @lines = <$handle>);
close $handle;

@sample = split /\n/,<<EOB;
[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up
EOB

#@lines = @sample;


my @timemap;

sub slept
{
	my $xg = shift;
	my $xs = shift;
	my $xe = shift;

	printf( "Guard %d slept from %d - %d\n", $xg, $xs, $xe );

	#printf( "fill %d,%d  %dx%d\n", $fx, $fy, $fw, $fh );

	for( $x = $xs ; $x < $xe ; $x++ ) {
		$timemap[ $xg ][ $x ]++;
	}
}

$part = 1;

if( $part == 1 ) {

	$guard = 0;
	$sstart = 0;
	$send = 0;
	
	foreach $line ( @lines ) 
	{
		printf( "LINE ~~ %s\n", $line );
		@cc = $line =~ /\[\d+-\d+-\d+ \d+:(\d+)\] (.+)/s;
		$mins = int $cc[0];

		# figure out which type it is
		if( index( $line, 'Guard' ) != -1 ) {
			@x = split( /#/, $line );
			@y = split( / /, $x[1] );
			$guard = int $y[0];
			#printf( "  New Guard |%s|\n", $guard );

		} elsif ( index( $line, 'falls' ) != -1 ) { 
			$sstart = $mins;
			#printf( "  Falls asleep at %d\n", $mins );
		} elsif ( index( $line, 'wakes' ) != -1 ) { 
			#printf( "  Wakes up at %d\n", $mins );
			$send = $mins;
			slept( $guard, $sstart, $send );
		}

# [1518-11-05 00:03] Guard #99 begins shift
# [1518-11-05 00:45] falls asleep
# [1518-11-05 00:55] wakes up

	}

	my $part1Total = 0;
	my $part1Guard = -1;

	my $part2Minute = 0;
	my $part2Guard = 0;
	my $part2Value = 0;

	foreach $grd ( keys( @timemap ))
	{
		$x = '';
		$gt = 0;
		for( $mm = 0 ; $mm < 59 ; $mm++ ) {
			$val = $timemap[ $grd ][ $mm ];
			if( $val > 0 ) {
				$x .= sprintf( "%2d ", $val );
				$gt += $val;
			} else {
				$x .= '...';
			}

			# part 2
			if( $val > $part2Value ) {
				$part2Minute = $mm;
				$part2Guard = $grd;
				$part2Value = $val;
			}
		}
		$x2 = $x;
		$x2 =~ s/\.//g;
		if( length( $x2 ) > 0 ) {
			printf( "G %4d ~ %s Tot=%d\n", $grd, $x, $gt );
		}

		if( $gt > $part1Total ) {
			$part1Total = $gt;
			$part1Guard = $grd;
		}
	}

	printf( "\nP1 results\n" );
	printf( "Sleepiest guard: %d\n", $part1Guard );
	$min = -1;
	$max = 0; # HA!
	for( $mm = 0 ; $mm < 59 ; $mm++ ) {
		$v = $timemap[ $part1Guard ][ $mm ];
		if( $v > $max ) {
			$max = $v;
			$min = $mm;
		}
	}
	printf( "Sleepiest minute: %d\n", $min );
	printf( "Part 1 result: %d\n", $min * $part1Guard );

	printf( "Part 2 result: %d\n", $part2Minute * $part2Guard );

}
