from setuptools import setup, find_packages

try:
    README = open('README').read()
except:
    README = None

setup(
    name='pagination',
    version=__import__('pagination').__version__,
    description='Simple django pagination based on Twitter Bootstrap and jQuery',
    long_description=README,
    license='APL',
    author='Brandon Taylor',
    author_email='alsoicode@gmail.com',
    url='http://brandonftaylor.com/',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    classifiers=['Development Status :: 5 - Production/Stable',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: Apache Software License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
)
