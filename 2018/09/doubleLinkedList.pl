#!/usr/bin/perl

$|=1;
use Data::Dumper;

#	plr		mrb		highscore
#	9		25		32
#	10		1618	8317
#	13		7999	146373
#
#	puzzle input
#	462 players; last marble is worth 71938 points

$nPlayers = 13;
$nMarbles = 7999;

# part 1 input
$nPlayers = 462;
$nMarbles = 71938*100;

$quiet = 0;

@marbles = (
	[0, 0, 0] # marble, prev idx, next idx
);

$current = 0;

sub addMarbleAfterCurrent
{
	my $mrb = shift;

	my $nxtID = $marbles[ $current ][ 2 ];

	# create the new marble
	my @newMrb = [ $mrb, $current, $nxtID ];

	# add it to the array
	push @marbles, @newMrb;

	my $newID = scalar @marbles -1;

	# set current to have this as its next
	$marbles[ $current ][2] = $newID;

	# set next to have this as its previous
	$marbles[ $nxtID ][1] = $newID;

	# adjust current to be this new one
	$current = $newID;
}


sub removeCurrent
{
	my $val = $marbles[ $current ][ 0 ];
	my $prv = $marbles[ $current ][ 1 ];
	my $nxt = $marbles[ $current ][ 2 ];

	# attach previous to next
	$marbles[ $prv ][ 2 ] = $nxt;

	# attach next to previous
	$marbles[ $nxt ][ 1 ] = $prv;

	# adjust current to the old current's next
	$current = $nxt;

	return $val;
}


sub printCircle
{
	my $plr = shift;

	my $ptr = 0;
	my $start = 0;

	printf( "[%2d] ", $plr );

	$done = 0;
	while( $done == 0 ) {
		if( $ptr == $current ) {
			my $x = sprintf( "(%d)", $marbles[ $ptr ][0] );
			printf( "%4s", $x );
		} else {
			printf( " %2d ", $marbles[ $ptr ][0] );
		}

		# next
		$ptr = $marbles[ $ptr ][2];
		if( $ptr == $start ) {
			$done = 1;
		}
	}
	printf( "\n" );
	#printf( "Current is %d\n", $currentIndex );
}

sub marbleSeek
{
	my $delta = shift;
	if( $delta == 0 ) { return; }
	if( $delta > 0 ) {
		while( $delta > 0 ) {
			$current = $marbles[ $current ][ 2 ];
			$delta--;
		}
		return;
	}

	if( $delta < 0 ) {
		while( $delta < 0 ) {
			$current = $marbles[ $current ][ 1 ];
			$delta++;
		}
		return;
	}
}




sub isMultipleOf23
{
	my $x = shift;
	if( $x % 23 == 0 ) {
		return 1;
	}
	return 0;
}

sub printScores
{
	my $marbleNo = shift;

	#printCircle( $currentPlayer );
#	printf( "-- $marbleNo marbles -----------------\n" );


	$topscore = 0;
	for( my $plr = 1 ; $plr <= $nPlayers ; $plr++ ) {
#		printf "Player $plr score = $scores{ $plr }\n";
		if( $scores{ $plr } > $topscore ) {
			$topscore = $scores{ $plr };
		}
	}

	printf "Marble $marbleNo; Top score: $topscore\r";
}

#printCircle( "-" );

#printCircle(0);
#marbleSeek( 1 );
#addMarbleAfterCurrent( 10 ); printCircle(1); 
#marbleSeek( 1 );
#addMarbleAfterCurrent( 11 ); printCircle(2);
#marbleSeek( 1 );
#addMarbleAfterCurrent( 12 ); printCircle(3);

my @scores;

$currentPlayer = 1;
for( $i = 1 ; $i < $nMarbles; $i ++ )
{
	if( isMultipleOf23( $i )) {
		marbleSeek( -7 );
		$scores{ $currentPlayer } += $i;
		$scores{ $currentPlayer } += removeCurrent();
		printScores( $i );
	} else {
		marbleSeek( 1 );
        addMarbleAfterCurrent( $i );
	}

	#if( $quiet != 1 ) { printCircle( $currentPlayer ); }

	$currentPlayer++;
	if( $currentPlayer > $nPlayers ) {
		$currentPlayer = 1;
	}
}

printf "~~~~~~~~~~~~~~\n";

printScores( $nMarbles );

exit;
