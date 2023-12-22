#!/bin/bash

sed -E 's/(\s+)/\n/g' words.txt | \
    sed  '/^$/d' | \
    sort | \
    uniq -c | \
    sort -r | \
    awk '{print $2, $1 }'