import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="trello_client-basics-api-username", version="0.0.1", author="Roshak7", author_email="Roshak7@gmail.com",
    description="Апи для сайта ТРЕЛЛО", long_description=long_description, long_description_content_type="text/markdown",
    url="[https://github.com/roshak7/trello_console_client](https://github.com/roshak7/trello_console_client)",
    packages=setuptools.find_packages(),
    classifiers=[ "Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License", "Operating System :: OS Independent", ],
    python_requires='>=3.6',)