from setuptools import setup

setup(
    name='py-postmates',
    version='0.1',
    description='Postmates API Wrapper',
    url='http://github.com/aatishnn/py-postmates',
    packages=['postmates'],
    license='MIT',
    install_requires=[
        'requests',
        'requests[security]',
        'python-dateutil'
    ],
    setup_requires=['pytest-runner'],
    tests_requires=['pytest'],
    zip_safe=False
)
