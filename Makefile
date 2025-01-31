clean:
	rm -r ./dist ./build
.PHONY: clean

package:
	python setup.py sdist bdist_wheel
.PHONY: package

upload:
	twine upload dist/sphinxcontrib*
.PHONY: upload
