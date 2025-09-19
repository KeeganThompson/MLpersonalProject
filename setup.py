from setuptools import find_packages, setup
from typing import List


E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    '''This function will return the list of requirements'''
    requirements=[]
    with open('requirements.txt') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if E_DOT in requirements:
            requirements.remove(E_DOT)
    return requirements

setup(
    name="MLpersonalProject",
    version='0.0.1',
    author="Keegan Thompson",
    author_email='keeganwthom@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)