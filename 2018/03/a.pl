

$filename = "input.txt";

open my $handle, '<', $filename;
chomp(my @lines = <$handle>);
close $handle;

@xlines = split /\n/,<<EOB;
#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2
EOB

my @pixmap;

sub fillPix
{
	my $fx = shift;
	my $fy = shift;
	my $fw = shift;
	my $fh = shift;

	#printf( "fill %d,%d  %dx%d\n", $fx, $fy, $fw, $fh );

	$x = $fx;
	$y = $fy;

	for( $x=$fx ; $x < $fx + $fw ; $x++ ) 
	{
		for( $y=$fy ; $y < $fy + $fh ; $y++ )
		{
			$pixmap[ $x ][ $y ]++;
		}
	}
}

sub countPix
{
	my $fid = shift;
	my $fx = shift;
	my $fy = shift;
	my $fw = shift;
	my $fh = shift;

	#printf( "fill %d,%d  %dx%d\n", $fx, $fy, $fw, $fh );

	$x = $fx;
	$y = $fy;

	$notones = 0;
	for( $x=$fx ; $x < $fx + $fw ; $x++ ) 
	{
		for( $y=$fy ; $y < $fy + $fh ; $y++ )
		{
			if ( $pixmap[ $x ][ $y ] > 1 ) { 
				$notones++;
			}
		}
	}

	if( $notones == 0 ) {
		printf "Single at %s\n", $fid;
	}
}

$pixmap[10][10] = 0;

$part = 1;

if( $part == 1 ) {

	foreach $line ( @lines ) 
	{
		#printf( "LINE ~~ %s\n", $line );

		@cc = $line =~ /#(\d+) @ (\d+),(\d+): (\d+)x(\d+)/s;
		$x = $cc[1];
		$y = $cc[2];
		$w = $cc[3];
		$h = $cc[4];

		fillPix( $x, $y, $w, $h );

		#@ch = split //, $line;
	}

	#print( "\n" );

	$claims = 0;

	for($r = 0; $r < 1000 ; $r++ ) 
	{
		for( $c =0 ; $c < 1000 ; $c++ ) 
		{
			$px = $pixmap[$r][$c];
			if( 0 ) {
				if( $px == 0 ) { 
					printf( "." );
				} else {
					printf( "%d", $px );
				}
			}

			if( $px >= 2 ) {
				$claims++;
			}
		}

		#print( "\n" );
	}

	printf( "Part 1:  %d claims\n", $claims );


	# part 2, reloop, looking for '1's only
	foreach $line ( @lines ) 
	{
		#printf( "LINE ~~ %s\n", $line );

		@cc = $line =~ /#(\d+) @ (\d+),(\d+): (\d+)x(\d+)/s;
		$id = $cc[0];
		$x = $cc[1];
		$y = $cc[2];
		$w = $cc[3];
		$h = $cc[4];

		countPix( $id, $x, $y, $w, $h );

		#@ch = split //, $line;
	}



}