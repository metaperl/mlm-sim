
from setuptools import setup

setup(
    name='mlm_sim',
    use_scm_version= {
        'write_to'w: 'mlm_sim/metadata.py'
    },
    setup_requires=['setuptools_scm'],
    packages=['mlm_sim'],
    install_requires=[
        'requests',
    ],
)
