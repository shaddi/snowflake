from distutils.core import setup, Extension
from distutils.command.install_scripts import install_scripts
import os

class snowflake_install_scripts(install_scripts):
    def run(self):
        install_scripts.run(self)
        os.system('snowflake -m') # generate the initial snowflake ID

setup(name="snowflake",
      version="0.0.4",
      description="Simple persistent unique IDs.",
      long_description="This package has been renamed to snowflake_uuid, and will be removed soon. Please use https://pypi.org/project/snowflake-uuid instead of this one!",
      author="Shaddi Hasan",
      author_email="shaddih@gmail.com",
      url="https://github.com/shaddi/snowflake",
      license='bsd',
      py_modules=['snowflake'],
      scripts=['snowflake'],
      cmdclass={"install_scripts": snowflake_install_scripts},
      classifiers=[
        'Operating System :: POSIX',
        'Development Status :: 7 - Inactive',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities',],
      keywords='unique id uuid persistent identification',
)
