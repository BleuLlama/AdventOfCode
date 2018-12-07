

$filename = "input.txt";

open my $handle, '<', $filename;
chomp(my @lines = <$handle>);
close $handle;

@sample = split /\n/,<<EOB;
dabAcCaCBAcCcaDA
EOB

#@lines = @sample;


$part = 2;

if( $part == 1 ) {

	foreach $line ( @lines ) 
	{
		$done = 0;
		while( $done == 0 ) {
			$x = length( $line );
			#printf( "LINE ~~ %s\n", $line );
			#printf "%s\n",$line;

			$line =~ s/Aa|Bb|Cc|Dd|Ee|Ff|Gg|Hh//g;
			$line =~ s/Ii|Jj|Kk|Ll|Mm|Nn|Oo|Pp//g;
			$line =~ s/Qq|Rr|Ss|Tt|Uu|Vv|Ww|Xx//g;
			$line =~ s/Yy|Zz//g;
			$line =~ s/aA|bB|cC|dD|eE|fF|gG|hH//g;
			$line =~ s/iI|jJ|kK|lL|mM|nN|oO|pP//g;
			$line =~ s/qQ|rR|sS|tT|uU|vV|wW|xX//g;
			$line =~ s/yY|zZ//g;

			#printf "%s\n",$line;
			$y = length( $line );
			if( $x == $y ) {
				$done = 1;
				printf( "Part 1: %d units long\n", $x );
			}
		}
	}
}

if( $part == 2 ) 
{
    foreach $origLine ( @lines )
	{
		@rms = (
			'Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Gg',
			'Hh', 'iI', 'Jj', 'Kk', 'Ll', 'Mm', 'Nn',
			'Oo', 'Pp', 'Qq', 'Rr', 'Ss', 'Tt', 'Uu',
			'Vv', 'Ww', 'Xx', 'Yy', 'Zz',
		);

		$p2Val = 9999999999;
		foreach $rm ( @rms ) {
			$line = $origLine;
			$line =~ s/[$rm]//g;

			$done = 0;
			while( $done == 0 ) {
				$x = length( $line );
				#printf( "LINE ~~ %s\n", $line );
				#printf "%s\n",$line;

				$line =~ s/Aa|Bb|Cc|Dd|Ee|Ff|Gg|Hh//g;
				$line =~ s/Ii|Jj|Kk|Ll|Mm|Nn|Oo|Pp//g;
				$line =~ s/Qq|Rr|Ss|Tt|Uu|Vv|Ww|Xx//g;
				$line =~ s/Yy|Zz//g;
				$line =~ s/aA|bB|cC|dD|eE|fF|gG|hH//g;
				$line =~ s/iI|jJ|kK|lL|mM|nN|oO|pP//g;
				$line =~ s/qQ|rR|sS|tT|uU|vV|wW|xX//g;
				$line =~ s/yY|zZ//g;

				#printf "%s\n",$line;
				$y = length( $line );
				if( $x == $y ) {
					$done = 1;
					if( $x < $p2Val ) {
						$p2Val = $x;
					}
					printf( "Part 2: rm %s -> %d units long\n", $rm, $x );
				}
			}
		}
		printf( "Part 2: shortest is %d\n", $p2Val );
	}
}
