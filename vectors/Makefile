.PHONY: all FORCE
NUM_THREADS=$(shell nproc --all)
NAME_PATTERN=([0-9])*lb([0-9])*sb([0-9]*)d.*

all: 1lb1sb600d_vectors_sample1e4 \
	1lb1sb100d_vectors_sample1e4 1lb1sb200d_vectors_sample1e4 1lb1sb400d_vectors_sample1e4 1lb1sb600d_vectors_sample1e4 1lb1sb800d_vectors_sample1e4 1lb32sb600d_vectors_sample1e4 1lb1sb1000d_vectors_sample1e4 \
	32lb1sb100d_vectors_sample1e4 32lb1sb200d_vectors_sample1e4 32lb1sb400d_vectors_sample1e4 32lb1sb600d_vectors_sample1e4 32lb1sb800d_vectors_sample1e4 32lb32sb600d_vectors_sample1e4 32lb1sb1000d_vectors_sample1e4 \
	1lb32sb100d_vectors_sample1e4 1lb32sb200d_vectors_sample1e4 1lb32sb400d_vectors_sample1e4 1lb32sb600d_vectors_sample1e4 1lb32sb800d_vectors_sample1e4 1lb32sb600d_vectors_sample1e4 1lb32sb1000d_vectors_sample1e4

FORCE:

../text8: ../text8.zip
	cd .. && unzip text8

../text8.zip:
	cd .. && wget -C http://mattmahoney.net/dc/text8.zip

%d_vectors_sample1e4: ../word2bits ../compute_accuracy ../text8
	../word2bits -sample 1e-4 -loss_bitlevel `if [ $$(echo $@ | sed -r 's/$(NAME_PATTERN)/\1/') = 1 ]; then echo 1; else echo 0; fi` -storage_bitlevel `if [ $$(echo $@ | sed -r 's/$(NAME_PATTERN)/\2/') = 1 ]; then echo 1; else echo 0; fi` -size `echo $@ | sed -r 's/$(NAME_PATTERN)/\3/'` -window 10 -negative 24 -threads $(NUM_THREADS) -iter 10 -min-count 5 -train ../text8 -output $@ -binary 1 | tee $@.training.log
	../compute_accuracy $@ <../data/google_analogies_test_set/questions-words.txt | tee $@.accuracy.log

../compute_accuracy: FORCE
	make -BC .. compute_accuracy

../word2bits: FORCE
	make -BC .. word2bits
