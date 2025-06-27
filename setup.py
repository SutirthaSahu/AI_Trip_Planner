from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return a list of requirements
    """
    requirement_list:List[str] = []

    try:
        #Open and read teh requirements.txt file
        with open('requirements.txt', 'r') as file:
            
            #Read lines from the file
            lines = file.readlines()

            #Process each file
            for line in lines:
                #Strip whitespaces and newline character
                requirement = line.strip()
                #Ignore empty lines and -e .
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_list

print(get_requirements())


setup(
    name="",
    version="0.0.1",
    author="Sutirtha Sahu",
    author_email="sutirthasahu@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)