.PHONY: dist clean

.DEFAULT_TARGET = dist

dist:
	python3 -m build --no-isolation --wheel && rm -rf flexy.egg-info

clean:
	rm -rf flexy.egg-info dist
