from distutils.core import setup, Extension
from distutils.command.install_scripts import install_scripts
import os

class snowflake_install_scripts(install_scripts):
    def run(self):
        install_scripts.run(self)
        os.system('snowflake -m') # generate the initial snowflake ID

with open("README.md", 'r') as f:
    long_desc = f.read()

setup(name="snowflake_uuid",
      version="0.1.0",
      description="Simple persistent unique IDs.",
      long_description=long_desc,
      author="Shaddi Hasan",
      author_email="shaddih@gmail.com",
      url="https://github.com/shaddi/snowflake",
      license='bsd',
      py_modules=['snowflake_uuid'],
      scripts=['snowflake'],
      cmdclass={"install_scripts": snowflake_install_scripts},
      classifiers=[
        'Operating System :: POSIX',
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',],
      keywords='unique id uuid persistent identification',
)
