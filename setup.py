import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ventos_simulation",
    version="0.1",
    author="Erich Schulz",
    author_email="erichbschulz@gmail.com",
    license="MIT",
    description="Ventilator simulation for project VentOS"
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ErichBSchulz/lung",
    packages=setuptools.find_packages(),
    package_data={'lung': ['*.txt']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
		'cycler==0.10.0',
		'kiwisolver==1.3.2',
		'matplotlib==3.4.3',
		'numpy==1.21.2',
		'pandas==1.3.4',
		'Pillow==8.4.0',
		'pynverse==0.1.4.4',
		'pyparsing==2.4.7',
		'python-dateutil==2.8.2',
		'pytz==2021.3',
		'scipy==1.7.1',
		'six==1.16.0'
    ],
    extras_require={
        'test': ['unittest'],
    },
    keywords=[
        "ventos",
        "ventilator",
        "medicine",
        "bioinformatics",
        ],
)
