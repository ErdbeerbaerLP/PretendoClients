
import setuptools

long_description = \
	"This library implements various network protocols made by Nintendo."

setuptools.setup(
	name = "nintendoclients",
	version = "2.0.0",
	description = "Nintendo network library",
	long_description = long_description,
	author = "Yannik Marchand",
	author_email = "ymarchand@me.com",
	url = "https://github.com/kinnay/NintendoClients",
	license = "MIT",
	packages = [
		"nintendo", "nintendo.nex"
	],
	package_data = {
		"nintendo": ["files/config/*", "files/cert/*"]
	},
	install_requires = [
		"anynet ~= 1.1",
		"pycryptodome"
	]
)
