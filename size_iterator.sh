#!/bin/bash
i=152

while [ $i -lt 202 ]
do
  echo training $i-len vectors
  outfile=vectors/1b`echo $i`d_vectors_e10_nonbin
  ./word2bits -bitlevel 1 -size $i -window 10 -negative 24 -threads 8 -iter 10 -min-count 5 -train text8  -output $outfile -binary 0
  echo output in $outfile
  i=$[$i+2]
done
