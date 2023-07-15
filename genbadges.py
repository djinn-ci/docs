import jinja2
import os

def main():
	order = []

	for ent in os.scandir("badges"):
		if ent.is_file():
			if ent.name.endswith(".desc"):
				continue

			order.append(ent.path)

	order.sort()

	badges = []

	for name in order:
		badges.append({
			"html": open(name).read(),
			"desc": open(name + ".desc").read(),
		})

	env = jinja2.Environment(loader=jinja2.FileSystemLoader("."))

	tmpl = env.get_template("badge-table.jinja")
	tmpl.stream(badges=badges).dump("badge-table.html")

if __name__ == "__main__":
	main()
