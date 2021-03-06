from setuptools import setup

setup(
    name='hammock',
    py_modules=['hammock'],
    version='0.3.1',
    description='rest like a boss',
    author='Kadir Pekel',
    author_email='kadirpekel@gmail.com',
    url='https://github.com/kadirpekel/hammock',
    install_requires=[
        'requests>=2.3.0',
        'vcrpy==1.0.2'
    ],
    tests_require=['httpretty==0.5.4'],
)
