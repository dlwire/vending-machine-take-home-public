install:
	pip install -r dev-requirements.txt

test:
	$(MAKE) -C features test
