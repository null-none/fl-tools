from setuptools import setup

version = __import__("src").get_version()

setup(
    name="fl",
    version="0.1",
    description="File manager developed tools. These scripts can encompass functionalities such as sorting and organizing files within directories, searching for specific file types or patterns, removing duplicate files.",
    author="Kalinin Mitko",
    author_email="kalinin.mitko@gmail.com",
    url="https://github.com/null-none/fl-tools",
    license="MIT",
    packages=["src"],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Environment :: Web Environment",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    install_requires=[],
)