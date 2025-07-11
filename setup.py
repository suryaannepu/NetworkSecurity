"""
setup.py is used to define the configuration of your projects such as meta data ,dependencies and more
"""
from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open("requirements.txt","r") as file:
            #readlines
            lines=file.readlines()
            for line in lines:
                requirement=line.strip()
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement) 
    except FileNotFoundError:
        print("requirements.txt not found")
    return requirement_lst
setup(
name='networksecurity',
version='0.0.1',
author='surya',
author_email='suryaannepu922@gmail.com',
packages=find_packages(),
install_requires=get_requirements()

)