from setuptools import setup, find_packages

setup(
    name="sherloock",
    version="0.1.0",
    author="SanchezSASE",
    description="Super Hybrid Efficient Reasoning Layered Orchestrator Of Knowledge (motor lógico sin entrenamiento)",
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
)
