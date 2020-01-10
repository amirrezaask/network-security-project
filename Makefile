sample-generate-keys:
	python3 run.py --mode g
sample-encrypt:
	python3 run.py --mode e --e 7 --d 91635976162903 --n 160362984049267 --inpt SALAM
sample-decrypt:
	python3 run.py --mode d --e 7 --d 91635976162903 --n 160362984049267 --cipher 124576655406223
