import io
import markdown
import sys

from jinja2_simple_tags import StandaloneTag

class Scanner:

	def __init__(self, str):
		self.pos = 0
		self.str = str

	def get(self):
		if self.pos == len(self.str):
			return -1

		c = self.str[self.pos]
		self.pos += 1

		return c

	def unget(self):
		self.pos -= 1

		if self.pos < 0:
			self.pos = 0

	def lit(self):
		return self.str[self.pos:]

class Parser:

	def __init__(self, f):
		self._pos = 0
		self._line = ""
		self._lines = f.readlines()

	def next(self):
		self._line = self._line[0:0]

		if self._pos >= len(self._lines):
			return True

		self._line = self._lines[self._pos]
		self._pos += 1

		return False

	def prev(self):
		self._line = self._line[0:0]
		self._pos -= 1

		if self._pos < 0:
			self._pos = 0

		self._line = self._lines[self._pos]

	def cell(self):
		sc = Scanner(self._line)

		if sc.get() != "-":
			return "", False, False

		if sc.get() != " ":
			return "", False, False

		buf = sc.lit()
		at_eof = False

		while True:
			at_eof = self.next()

			if at_eof:
				break

			sc = Scanner(self._line)
			c = sc.get()

			if c == "-" or c == "\n":
				self.prev()
				break

			sc.unget()
			lit = sc.lit()

			if lit == "\\\n":
				lit = "\n"
			buf += lit

		return buf[:len(buf)-1], True, at_eof

	def fence(self):
		if self._line != "\n":
			return False, False

		at_eof = self.next()

		if at_eof:
			return False, True

		if self._line != "---\n":
			return False, False

		at_eof = self.next()

		if self._line != "\n":
			return False, at_eof

		self.next()
		return True, at_eof

	def parse(self):
		at_eof = self.next()

		while self._line == "\n":
			at_eof = self.next()

		if at_eof:
			return None

		header = []

		while True:
			cell, ok, at_eof = self.cell()

			if at_eof:
				if ok:
					header.append(cell)

				return header, []

			if not ok:
				ok, at_eof = self.fence()

				if not ok or at_eof:
					return header, []

				break

			header.append(cell)
			self.next()

		rows = []
		row = []

		while True:
			cell, ok, at_eof = self.cell()

			if at_eof:
				row.append(cell)
				rows.append(row)
				row = row[0:0]
				break

			if not ok:
				ok, at_eof = self.fence()

				if ok:
					rows.append(row)
					row = row[0:0]
					continue

				if at_eof:
					break

			row.append(cell)
			self.next()

		return header, rows

class TableTag(StandaloneTag):

	tags = {"table"}

	def _render_header(self, out, header):
		out.write("<thead><tr>")

		for h in header:
			out.write("<th>{0}</th>".format(h))

		out.write("</thead></tr>")

	def _render_rows(self, out, rows):
		out.write("<tbody>")

		for row in rows:
			out.write("<tr>")

			for cell in row:
				out.write("<td>{0}</td>".format(markdown.markdown(cell, extensions=["sane_lists"])))
			out.write("</tr>")

		out.write("</tbody>")

	def render(self, name):
		p = Parser(open(name))

		header, rows = p.parse()

		buf = io.StringIO()

		buf.write("<table>")
		self._render_header(buf, header)
		self._render_rows(buf, rows)
		buf.write("</table>")

		return buf.getvalue()
