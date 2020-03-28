
import setuptools


with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='sainofirst',
    version='0.0.1',
    author="Sainofirst",
    maintainer='Shubz Kothekar',
    maintainer_email='hello@shubzkothekar.com',
    author_email = 'contact@sainofirst.com',
    description="testing",
    long_description=open("readme.md").read(),
    long_description_content_type="text/markdown",
    # url="https://github.com/javatechy/dokr",
    package_dir={'': 'src'},
    packages=['sainofirst', 'sainofirst.services.sms', 'sainofirst.services.voice'],
    keywords='sdk bulk-sms bulk-voice sms-gateway',
    install_requires=[
        'requests=2.23.0'
    ],
    license='Apache',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: SDK',
        "Programming Language :: Python :: 3.7",
        'License :: OSI Approved :: Apache Software License',
    ],
    python_requires='>=3.5',
    package_data={  
        'sainofirst': ['config.json', 'errors.json', 'services'],
    },
    project_urls={  
        
        'website': 'https://www.sainofirst.com',
    },
    zip_safe=False

 )