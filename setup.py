from setuptools import find_packages,setup
from typing import List

HYPEN_e_dot = '-e .'

def get_requirements(file_path:str)-> List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("/n","")for req in requirements]
        
        if HYPEN_e_dot in requirements:
            requirements.remove(HYPEN_e_dot)
            
    return requirements

setup(
    name = 'Ml-project',
    version='0.0.1',
    author='Sunil',
    author_email='sunilkumarsk2423@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)