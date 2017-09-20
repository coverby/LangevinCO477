from distutils.core import setup

with open('README.md') as f:
      long_description = ''.join(f.readlines())

setup(name='Langevin477CO',
      version='.01',
      description='CHE 477 Langevin Simulator',
      long_description=long_description,
      author='Clyde Overby',
      packages=['Langevin477CO']
     )