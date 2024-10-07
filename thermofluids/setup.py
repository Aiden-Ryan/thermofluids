
from setuptools import setup, find_packages
setup(
    name = 'thermofluids',
    version = '0.1.23',
    description='thermofluid library',
    author = 'Aiden Ryan',
    author_email = 'aiden.mc.ryan@gmail.com',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy', 
        'CoolProp',
        'math', 
        'CtREFPROP',
        
    ],
    extras_require = {
        "dev": ["twine>=4.0.2"],
    },
    python_requires=">=3.10"
)