from setuptools import setup, find_packages

setup (
    name = 'wheelTest', 
    version = '1.0.1',
    author = 'Dong HAN', 
    author_email = 'handbj@cn.ibm.com', 
    license = 'GPL',
    packages = find_packages(), 
    include_package_data = True, 
    zip_safe = True, 
    entry_point = {
        'consol_scripts': [
            'test_start=wheelTest.command:start', 
            'test_init=wheelTest.command:init',
        ]
    },
)