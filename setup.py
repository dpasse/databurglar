import setuptools


with open('requirements.txt') as f:
    install_requires = f.read().splitlines()

setuptools.setup(
    name='',
    version='0.0.1',
    keywords='',
    description='SQLAlchemy Package for data tracking.',
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    install_requires=install_requires,
    url='https://github.com/dpasse/qa',
    long_description='',
    long_description_content_type='text/markdown',
    entry_points = {}
)
