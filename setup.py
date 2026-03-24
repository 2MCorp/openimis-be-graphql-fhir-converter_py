from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="graphql-fhir-converter",
    version="1.0.0",
    author="Dawda Borje Kujabi",
    author_email="dawdaborjekujabi@gmail.com",
    maintainer="2M Corp",
    maintainer_email="info@2m-corp.com",
    description="A Python library for converting between FHIR resources and GraphQL types",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/2m-corp/graphql-fhir-converter",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
    ],
    python_requires=">=3.8",
    install_requires=[
        "graphene==2.1.9",
        "fhir.resources>=6.0.0",
        "django>=3.2.0",
    ],
    extras_require={
        "dev": [
            "pytest>=6.0.0",
            "pytest-cov>=2.0.0",
            "black>=21.0.0",
            "flake8>=3.8.0",
            "mypy>=0.800",
        ],
        "docs": [
            "sphinx>=4.0.0",
            "sphinx-rtd-theme>=1.0.0",
        ],
    },
    keywords="fhir, graphql, healthcare, medical, converter",
    project_urls={
        "Bug Reports": "https://github.com/2m-corp/graphql-fhir-converter/issues",
        "Source": "https://github.com/2m-corp/graphql-fhir-converter",
        "Documentation": "https://graphql-fhir-converter.readthedocs.io/",
    },
    license="MIT",
    zip_safe=False,
)
