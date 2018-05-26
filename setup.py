from setuptools import setup


setup(
    name='exchange',
    version='0.1',
    py_modules=['exchange'],
    install_requires=[
        'click',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'exchange = exchange:exchange'
        ],
    },
)