import pathlib
from setuptools import setup

# reading the README file
HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

# the setup script
setup(
    name="kakaopy",
    version = "0.1.0",
    description = "kakao search API customizing",
    long_description = README,
    long_description_content_type = "text/markdown",
    url = "https://github.com/SeoJeongYeop/kakaopy",
    author = "Jeongyeop Seo",
    author_email="sjyswe99@gmail.com",
    license ="MIT",
    packages = ["kakaopy"],
    classifiers = [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],

)