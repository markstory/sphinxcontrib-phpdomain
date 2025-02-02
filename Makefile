clean:
	rm -r ./dist ./build
.PHONY: clean

package:
	python -m build
.PHONY: package

upload:
	twine upload dist/sphinxcontrib*
.PHONY: upload
