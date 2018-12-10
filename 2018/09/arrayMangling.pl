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
$nMarbles = 71938; #*100;

$quiet = 0;

@marbleCircle = ( 0 );

$currentIndex = 0;

sub printCircle
{
	my $plr = shift;

	return;

	printf( "[%2d] ", $plr );

	for( my $i = 0 ; $i < scalar @marbleCircle ; $i++ )
	{
		if( $i == $currentIndex ) {
			my $x = sprintf( "(%d)", $marbleCircle[ $i ] );
			printf( "%4s", $x );
		} else {
			printf( " %2d ", $marbleCircle[ $i ] );
		}
	}
	printf( "\n" );
	#printf( "Current is %d\n", $currentIndex );
}

sub insertMarble
{
	my $mNo = shift;
	my @newArr;
	for( my $i =0 ; $i < scalar @marbleCircle ; $i ++ )
	{
		push @newArr, $marbleCircle[ $i ];
		if( $i == $currentIndex ) {
			push @newArr, $mNo;
		}
	}
	@marbleCircle = @newArr;
	$currentIndex++;
}

sub nextPosition
{
	$currentIndex += 1;
	$currentIndex = $currentIndex % (scalar @marbleCircle);
}

sub isMultipleOf23
{
	my $x = shift;
	if( $x % 23 == 0 ) {
		return 1;
	}
	return 0;
}

sub removeMarble
{
	# Move back by 7...
	$currentIndex += scalar @marbleCircle;
	$currentIndex -= 7;
	$currentIndex %= scalar @marbleCircle;

	#printf( "Removing marble $currentIndex => $marbleCircle[ $currentIndex ]\n");
	my $retValue = $marbleCircle[ $currentIndex ];

	splice @marbleCircle, $currentIndex, 1;
	return $retValue;
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

my @scores;

$currentPlayer = 1;
for( $i = 1 ; $i < $nMarbles; $i ++ )
{
	if( isMultipleOf23( $i )) {
		$scores{ $currentPlayer } += $i;
		$scores{ $currentPlayer } += removeMarble();
		if( $quiet != 1 ) { printScores( $i ) };
		if( $quiet == 1 ) { printScores( $i ) };
	} else {
		nextPosition();
        insertMarble( $i );
	}

	if( $quiet != 1 ) { printCircle( $currentPlayer ); }
	$currentPlayer++;
	if( $currentPlayer > $nPlayers ) {
		$currentPlayer = 1;
	}
}

printf "~~~~~~~~~~~~~~\n";

printScores( $nMarbles );

exit;
