../text8: ../text8.zip
	cd .. && unzip text8

../text8.zip:
	cd .. && wget -C http://mattmahoney.net/dc/text8.zip

1b600d_vectors_sample1e4: ../word2bits ../compute_accuracy ../text8
	../word2bits -sample 1e-4 -bitlevel 1 -size 600 -window 10 -negative 24 -threads 4 -iter 10 -min-count 5 -train ../text8 -output $@ -binary 1 | tee $@.training.log
	../compute_accuracy $@ <../data/google_analogies_test_set/questions-words.txt | tee $@.accuracy.log

1b600d_vectors_sample1e4_nonquantized_vectors: ../word2bits ../compute_accuracy ../text8
	../word2bits -sample 1e-4 -bitlevel 0 -size 600 -window 10 -negative 24 -threads 4 -iter 10 -min-count 5 -train ../text8 -output $@ -binary 1 | tee $@.training.log
	../compute_accuracy $@ <../data/google_analogies_test_set/questions-words.txt | tee $@.accuracy.log

1b600d_vectors_sample1e4_nonquantized_loss: ../word2bits ../compute_accuracy ../text8
	../word2bits -sample 1e-4 -quantized_loss 0 -bitlevel 1 -size 600 -window 10 -negative 24 -threads 4 -iter 10 -min-count 5 -train ../text8 -output $@ -binary 1 | tee $@.training.log
	../compute_accuracy $@ <../data/google_analogies_test_set/questions-words.txt | tee $@.accuracy.log

../compute_accuracy:
	make -BC .. compute_accuracy

../word2bits:
	make -BC .. word2bits
