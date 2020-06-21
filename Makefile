.PHONY: examples

test:
	python3 setup.py test

examples:
	! PYTHONPATH=. python3 examples/integer.py --min-max -1
	! PYTHONPATH=. python3 examples/integer.py --min -1
	! PYTHONPATH=. python3 examples/integer.py --max 1000
	! PYTHONPATH=. python3 examples/integer.py --any a
	PYTHONPATH=. python3 examples/integer.py \
	    --min-max 47 --min 1000 --max -5 --any 1

test-sdist:
	rm -rf dist
	python3 setup.py sdist
	cd dist && \
	mkdir test && \
	cd test && \
	tar xf ../*.tar.gz && \
	cd argparse_addons-* && \
	python3 setup.py test

release-to-pypi:
	python3 setup.py sdist
	python3 setup.py bdist_wheel --universal
	twine upload dist/*
