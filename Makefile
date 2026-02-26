run:
	python src/etl/main.py

test:
	pytest

clean:
	rm -rf output