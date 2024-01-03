from setuptools import setup, find_packages

setup(
    name="fueled",
    version="0.0.2",
    packages=find_packages(),
    include_package_data=True,
    package_data={'fueled': ['data/vehicles.json']},
    install_requires=[

    ],
    author='shoshone-s',
    description="A Python package for vehicle mileage calculations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/shoshone-s/fueled",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.11.0',
)