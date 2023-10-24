from setuptools import find_packages, setup
from typing import List
HYPE_E_do='-e.'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[r.replace("\n"," ") for r in requirements]
        
        if(HYPE_E_do) in requirements:
            requirements.remove(HYPE_E_do)
    return requirements

setup(
name="MLPRO",
version="0.1.0",
author="Dhruvil",
author_email="dhruvilmht0319@gmail.com",
packages=find_packages(),
install_requires=get_requirements("requirements.txt")
)

