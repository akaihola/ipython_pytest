from distutils.core import setup


with open('README.rst') as f:
    long_description = f.read()


setup(
    name='ipython_pytest',
    version='0.0.1',
    author='Antti Kaihola',
    author_email='antti.kaihola@eniram.fi',
    py_modules=['ipython_pytest'],
    url='https://github.com/akaihola/ipython_pytest',
    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: BSD License',
                 'Programming Language :: Python :: 3.5',
                 'Operating System :: OS Independent'],
    license='README.rst',
    description='IPython extension to run pytest for the current cell.',
    long_description=long_description,
)
