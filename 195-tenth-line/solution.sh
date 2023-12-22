#!/bin/bash

# Given a text file file.txt, print just the 10th line of the file.

awk '
# BEGIN { print "The 10th line is:\n" }
{
    if (NR == 10) print;
}
' < file.txt
