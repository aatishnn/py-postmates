from setuptools import setup

setup(
    name='pypostmates',
    version='0.1',
    description='Postmates API Wrapper',
    url='http://github.com/aatishnn/py-postmates',
    packages=['postmates'],
    license='MIT',
    install_requires=[
            'requests[security]',
    ],
    zip_safe=False
)
