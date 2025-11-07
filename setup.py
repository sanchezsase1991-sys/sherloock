from setuptools import setup, find_packages

setup(
    name="sherloock",
    version="0.1.0",
    author="Sergio Alberto Sanchez Echeverria",
    author_email="sanchezsase1991@gmail.com",  
    description="Super Hybrid Efficient Reasoning Layered Orchestrator Of Knowledge (Sherloock)",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scikit-learn",
        "z3-solver",
        "pulp",
        "sympy",
        "psutil"
    ],
    python_requires=">=3.10",
    license="Custom Non-Commercial License",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "sherloock-cli=cli:main"
        ]
    },
)
