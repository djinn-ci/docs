#!/bin/sh

cd plugins && {
	python setup.py install --user

	cd - > /dev/null
}

yarn_() {
	bin="node_modules/.bin/lessc"

	[ ! -f "$bin" ] && yarn install

	"$bin" --clean-css less/main.less theme/css/main.css
}

yarn_
mkdocs build
