from setuptools import setup, find_packages
setup(
  name = 'json_typer',         # How you named your package folder (MyLib)
  packages = find_packages(),   # Chose the same as "name"
  version = '1.0.3',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Seamlessly encode and decode python objects to json while maintaining their types.',   # Give a short description about your library
  author = 'Sam Privett',                   # Type in your name
  author_email = 'privett.sam@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/maspe36/json_typer',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/maspe36/json_typer/archive/v1.0.3.tar.gz',    # I explain this later on
  keywords = ['JSON', 'TYPING', 'TYPER', 'DYNAMIC'],   # Keywords that define your package best
  install_requires=[],
  classifiers=[
    'Development Status :: 5 - Production/Stable',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
