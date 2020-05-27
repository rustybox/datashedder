from setuptools import setup, find_packages

setup(
    name='datashedder',
    version='0.1.0',
    license='MIT',
    description='Technical test application for a data management company',
    packages=['datashedder'],
    package_dir={'': 'src'},
    python_requires='>=3.6',
    install_requires=[
        'python-Levenshtein',
    ],
    entry_points={
        "console_scripts": [
            "datashedder = datashedder.main:run",
        ]
    }
)