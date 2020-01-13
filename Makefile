sample-generate-keys:
	python3 run.py --mode g --length 100
sample-encrypt:
	python3 run.py --mode e --e 3 --d 1634663681848171147 --n 2451995525904917323 --inpt 'SALAM. fghj'
sample-decrypt:
	python3 run.py --mode d --e 3 --d 1634663681848171147 --n 2451995525904917323 --cipher 6871136751484928-1457117049753-223736982414912-1000
