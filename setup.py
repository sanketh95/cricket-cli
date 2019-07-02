from setuptools import setup

setup(
    name = "livecricket",
    version = "0.0.4",
    author = "Sanketh Mopuru",
    author_email = "sanketh.mopuru@gmail.com",
    description = ("Live scoreboard display similar to cricbuzz"),
    license = "BSD",
    keywords = "cricket",
    url = "",
    packages=[],
	install_requires=['pycricbuzz'],
	scripts=['live.py']
)
