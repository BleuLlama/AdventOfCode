#!/usr/bin/perl

use Data::Dumper;

$filename = "input.txt";
#$filename = "sample.txt";

open my $handle, '<', $filename;
chomp(my @lines = <$handle>);
close $handle;

my @points = (
	[ 0, 0, 0, 0 ]
);

foreach $line ( @lines ) 
{
	printf( "LINE ~~ %s\n", $line );
	# position=< 7,  0> velocity=<-1,  0>
	# position=< 3, -2> velocity=<-1,  1>
	# position=< 6, 10> velocity=<-2, -1>
	# position=< 2, -4> velocity=< 2,  2>
	# position=<-6, 10> velocity=< 2, -2>

	@cc = $line =~ /position=<\s*([-\d]+),\s*([-\d]+)> velocity=<\s*([-\d]+),\s*([-\d]+)>/s;

	my @pt = [ $cc[0], $cc[1], $cc[2], $cc[3] ];

	push @points, @pt;
}
#print Dumper \@points;

$gMinWidth = 9999;
$gMinHeight = 9999;

sub advanceAll
{
	$tick = shift;

	$minX = 9999; $maxX = -9999;
	$minY = 9999; $maxY = -9999;

	for( my $i = 0 ; $i < scalar @points ; $i ++ )
	{
		$points[$i][0] += $points[$i][2];
		$points[$i][1] += $points[$i][3];

		my $thisX = $points[$i][0];
		my $thisY = $points[$i][1];

		if( $thisX > $maxX ) { $maxX = $thisX; }
		if( $thisX < $minX ) { $minX = $thisX; }
		if( $thisY > $maxY ) { $maxY = $thisY; }
		if( $thisY < $minY ) { $minY = $thisY; }
	}

	my $wid = $maxX-$minX;
	my $hgt = $maxY-$minY;

	my $chg = 0;
	if( $wid < $gMinWidth ) { $gMinWidth = $wid; $chg++; }
	if( $hgt < $gMinHeight ) { $gMinHeight = $hgt; $chg++; }
	if( $chg > 1 ) {
		print( "$tick: min/max:  $minX,$minY - $maxX,$maxY  width/hgt: $wid x $hgt\n" );
	}
	if( $chg > 1 && $wid < 200 ) {
		return 1;
	}
	return 0;
}

sub DumpScreen
{
	$sx = 110;
	$tw = 80;

	$sy = 145;
	$th = 16;

	for( my $y = $sy ; $y < $th+$sy ; $y++ )
	{
		for( my $x = $sx ; $x < $tw+$sx ; $x++ )
		{
			$px = 0;
			for( my $i = 0 ; $i < scalar @points ; $i ++ )
			{
				$pix = int $points[$i][0];
				$piy = int $points[$i][1];

	#			printf "$pix,$piy ";

				if( $pix == $x && $piy == $y ) {
					$px = 1;
				}
			}
			if( $px == 1 )  { print( "#" ) }
			else {          print( "." ); }

		}
		printf( "\n" );
	}

}


#for( my $tick = 0 ; $tick < 10210 ; $tick++ )
for( my $tick = 1 ; $tick < 13000 ; $tick++ )
{
	if( advanceAll( $tick ) ) {
		DumpScreen();
	}
}

