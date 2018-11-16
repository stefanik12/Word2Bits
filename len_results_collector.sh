#!/bin/bash
i=200

while [ $i -lt 2000 ]
do
  echo [INFO] Current vec len $i:
  outfile=vectors/1b`echo $i`d_vectors_e10
  ./word2bits -bitlevel 1 -size $i -window 10 -negative 24 -threads 8 -iter 10 -min-count 5 -train text8  -output $outfile -binary 1 > /dev/null
  echo output in $outfile
  ./compute_accuracy $outfile < data/google_analogies_test_set/questions-words.txt
  i=$[$i+20] 
done
