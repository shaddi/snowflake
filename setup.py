from distutils.core import setup, Extension
from distutils.command.install_scripts import install_scripts
import os

class snowflake_install_scripts(install_scripts):
    def run(self):
        install_scripts.run(self)
        os.system('snowflake -m') # generate the initial snowflake ID

setup(name="snowflake",
      version="0.0.2",
      description="Simple persistent unique IDs.",
      author="Shaddi Hasan",
      author_email="shaddi@cs.berkeley.edu",
      url="https://github.com/shaddi/snowflake",
      license='bsd',
      py_modules=['snowflake'],
      scripts=['snowflake'],
      cmdclass={"install_scripts": snowflake_install_scripts},
      classifiers=[
        'Operating System :: POSIX',
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',],
      keywords='unique id uuid persistent identification',
)
