from setuptools import find_packages,setup
from typing import List
def get_requirments(file_path:str)->List[str]:
    requirments=[]
    with open(file_path) as file_obh:
        requirments=file_obh.readlines()
        requirments=[req.replace("\n","") for req in requirments ]
        return requirments

setup(
    name="credit card fraud detection",
    version="0.0.1",
    author="mohit",
    author_email="mohankholiya28@gmail.com",
    install_requires=get_requirments('Requirment.txt'),
    packages=find_packages()
)