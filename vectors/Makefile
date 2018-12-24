NUM_THREADS=$(shell nproc --all)

../text8: ../text8.zip
	cd .. && unzip text8

../text8.zip:
	cd .. && wget -C http://mattmahoney.net/dc/text8.zip

1b%d_vectors_sample1e4: ../word2bits ../compute_accuracy ../text8
	../word2bits -sample 1e-4 -bitlevel 1 -size `echo $@ | sed -r 's/[0-9]*b([0-9]*)d.*/\1/'` -window 10 -negative 24 -threads $(NUM_THREADS) -iter 10 -min-count 5 -train ../text8 -output $@ -binary 1 | tee $@.training.log
	../compute_accuracy $@ <../data/google_analogies_test_set/questions-words.txt | tee $@.accuracy.log

1b%d_vectors_sample1e4_nonquantized_loss: ../word2bits ../compute_accuracy ../text8
	../word2bits -sample 1e-4 -quantized_loss 0 -bitlevel 1 -size `echo $@ | sed -r 's/[0-9]*b([0-9]*)d.*/\1/'` -window 10 -negative 24 -threads $(NUM_THREADS) -iter 10 -min-count 5 -train ../text8 -output $@ -binary 1 | tee $@.training.log
	../compute_accuracy $@ <../data/google_analogies_test_set/questions-words.txt | tee $@.accuracy.log

32b%d_vectors_sample1e4: ../word2bits ../compute_accuracy ../text8
	../word2bits -sample 1e-4 -bitlevel 0 -size `echo $@ | sed -r 's/[0-9]*b([0-9]*)d.*/\1/'` -window 10 -negative 24 -threads $(NUM_THREADS) -iter 10 -min-count 5 -train ../text8 -output $@ -binary 1 | tee $@.training.log
	../compute_accuracy $@ <../data/google_analogies_test_set/questions-words.txt | tee $@.accuracy.log

../compute_accuracy:
	make -BC .. compute_accuracy

../word2bits:
	make -BC .. word2bits
