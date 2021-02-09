import setuptools


setuptools.setup(
    name="windows-path-adder",
    version="1.0.4",
    license='MIT',
    author="oneofthezombies",
    author_email="hunhoekim@gmail.com",
    description="add environment path in windows.",
    long_description=open('README.md').read(),
    long_description_content_type = 'text/markdown',
    url="https://github.com/oneofthezombies/windows-path-adder",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
)
