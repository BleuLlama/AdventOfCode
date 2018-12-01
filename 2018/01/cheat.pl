#!/usr/bin/perl
use warnings;
use strict;
use autodie;
use feature qw/say/;

my $freq = 0;
my @shifts;

open my $shifts, "<", "input1.txt";
while (<$shifts>) {
  chomp;
  $freq += ( 0 + $_ );
  push @shifts, $_;
}

say "Part 1: $freq";

my %freqs = ( 0 => 1 );
$freq  = 0;
while (1) {
  for (@shifts) {
    $freq += $_;
    if (++$freqs{$freq} == 2) {
      say "Part 2: $freq";
      exit 0;
    }
  }
}

