try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

packages = [
    'yuntan_service',
]

requires = ['yuntan_service']

setup(
    name='yuntan_service',
    version='0.0.1',
    description='Python client for yuntan service.',
    author='Li Meng Jun',
    author_email='lmjubuntu@gmail.com',
    url='https://github.com/Lupino/python-yuntan',
    packages=packages,
    package_dir={'yuntan_service': 'yuntan_service'},
    include_package_data=True,
    install_requires=requires,
)
