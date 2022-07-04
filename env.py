import os

env = {
	"DJINN_API_SERVER": "https://api.djinn-ci.com",
	"DJINN_SERVER":     "https://djinn-ci.com",
}

if "DJINN_API_SERVER" in os.environ:
	env["DJINN_API_SERVER"] = os.environ["DJINN_API_SERVER"]
	env["DJINN_SERVER"] = os.environ["DJINN_SERVER"]
