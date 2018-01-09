echo "len(sequence), len(entities) ";
awk 'NR%4 == 2 {lengths[length($0)]++} END {for (l in lengths) {print l,lengths[l]}}' $1;

# Continue Adding more small checks
