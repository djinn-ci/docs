__version__ = "0.0.1"

import mkdocs.config
import os
import re

import mkdocs_jinja2.table

from mkdocs.plugins import BasePlugin

from jinja2 import Environment, FileSystemLoader

def clean(html):
	if "<script" in html:
		return html.replace("{{", "{ {").replace("}}", "} }")
	return html

def slug(s):
	value = re.sub(r"[^\w\s-]", "", s).strip().lower()
	return re.sub(r"[{}\s]+".format("-"), "-", value)

	return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

class Jinja2Environment(BasePlugin):

	def __init__(self):
		self._macros = ""
		self._vars = {}

	def _exec(self, file):
		f = open(file)
		exec(f.read())

		l = locals()

		for v in list(l):
			if v.startswith("__"):
				continue

			for it in list(l.items()):
				if it[0] == v:
					self._vars[v] = it[1]
					break

	def on_config(self, config, **kwargs):
		self._vars = {}

		for file in self.config.get("exec"):
			self._exec(file)

		# Delete any variables set from outside of the script.
		del self._vars["f"]
		del self._vars["file"]
		del self._vars["self"]

		macros = self.config.get("macros")

		if macros != "":
			self._macros = open(macros).read() + "\n"

	def on_nav(self, nav, config, files):
		self.nav = nav

	def on_page_content(self, html, page, config, files):
		env = Environment(loader=FileSystemLoader(os.getcwd()), extensions=[table.TableTag])
		env.filters["slug"] = slug

		return env.from_string(self._macros + clean(html)).render(
			config=config,
			nav=self.nav,
			files=files,
			**self._vars,
		)
