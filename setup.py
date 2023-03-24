from setuptools import find_packages,setup
from typing import List

edot = '-e .'
def get_requirements(file_path:str)->List[str]:
    # this function will return list of requirements
    requirements = []
    with open(file_path) as fileobj:
        requirements = fileobj.readlines()
        requirements = [req.replace("\n"," ") for req in requirements]
        if edot in requirements:
            requirements.remove(edot)
    return requirements
        
setup(
name = "mlproject",
version = '0.0.1',
author = 'Varun',
author_email='erravarun@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)