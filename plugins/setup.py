from setuptools import setup

setup(
	name="mkdocs-jinja2",
	version="0.0.1",
	author="Andrew Pillar",
	author_email="me@andrewpillar.com",
	packages=["mkdocs_jinja2"],
	license="LICENSE",
	description="Custom MkDocs plugin for rendering API schemas",
	install_requires=[],
	entry_points={
		"mkdocs.plugins": [
			"jinja2 = mkdocs_jinja2:Jinja2Environment",
		],
	},
)
