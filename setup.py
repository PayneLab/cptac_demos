from setuptools import setup
import os.path as path


# Get the path to our current directory
path_here = path.abspath(path.dirname(__file__))

# Get the package version from its universal storage location, cptac/version.py
version = {}
version_path = path.join(path_here, "cptac", "version.py")
with open(version_path) as fp:
	exec(fp.read(), version)

# Get the long description from the README file
readme_path = path.join(path_here, "README.md")
with open(readme_path) as readme_file:
    readme_text = readme_file.read()

setup(name='cptac',
	version=version['__version__'],
	description='Python packaging for CPTAC data',
	long_description=readme_text,
	long_description_content_type='text/markdown',
	url='http://github.com/PayneLab/cptac',
	author='Dr. Samuel Payne',
	author_email='sam_payne@byu.edu',
	license='Apache 2.0',
	packages=['cptac','cptac.utils'],
	install_requires=[
		'numpy>=1.16.3',
		'pandas==0.25.*',
		'requests>=2.21.0',
		'beautifulsoup4>=4.7.1',
		'scipy>=1.2.1',
		'urllib3>=1.24.2',
	],
    data_files=[
         ('bioplex_interactions',['cptac/utils/BioPlex_interactionList_v4a.tsv'])
    ],
	classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: OSI Approved :: Apache Software License',
	],
	keywords='bioinformatics cancer proteomics genomics open science open data',
	python_requires='>=3.6.*',
	zip_safe=False,
	include_package_data=True,
	project_urls={
	   'Documentation': 'https://github.com/PayneLab/cptac/tree/master/docs'
	},
	)
