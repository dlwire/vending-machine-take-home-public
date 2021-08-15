install:
	pip install -r dev-requirements.txt

test:
	PYTHONPATH='/Users/david/Projects/MEDNAX/vending-machine-take-home-public/src' $(MAKE) -C src/features test
