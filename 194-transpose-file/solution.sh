#!/bin/bash

# Read from the file file.txt and print its transposed content to stdout.
# Expected output: 
# name alice ryan
# age 21 30

awk '
{
    # store entries in multi-dimensional array
    # https://www.grymoire.com/Unix/Awk.html#uh-23
    for (i=1; i<=NF; i++) {
        a[i,NR]=$i
    }
} 
END {    
    for (i=1; i<=NF; i++) {
        for (j=1; j<=NR; j++) {
            if (j<NR) {
                sep=" "
            } else {
                sep="\n"
            }
            printf("%s%s", a[i,j],sep);
        }
    }
    
}' file.txt
