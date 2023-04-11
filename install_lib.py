"""Install all the libraries in the requirements.txt file."""

import subprocess

with open('requirements.txt', 'r') as f:
    packages = f.read().splitlines()

for package in packages:
    subprocess.call(['pip', 'install', package])