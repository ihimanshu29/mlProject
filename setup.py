# setup.py
from typing import List
from setuptools import find_packages,setup

HYPEH_E_DOT='-e .'
def get_Requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requiremnsts
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if HYPEH_E_DOT in requirements:
            requirements.remove(HYPEH_E_DOT)
    
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Himanshu',
    author_email='himanshuawasthi.2999@gmail.com',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
) 