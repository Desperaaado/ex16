try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Bubble, Quick, and Merge Sort.',
    'author': 'Murphian',
    'url': 'XXXXXXXXXX',
    'download_url': 'XXXXXXXXXXXXX',
    'author_email': 'murphianx@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex16'],
    'scripts': [],
    'name': 'ex16'
}

setup(**config)