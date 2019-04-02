from setuptools import setup
from setuptools import find_packages

setup(name='FlaskApp',
      version='0.1',
      description='Thea',
      url='http://github.com/DuongDo-InterSystems/thea',
      author='Duong Do',
      author_email='duongdo@example.com',
      license='MIT',
      packages=find_packages(exclude=['contrib', 'docs', 'tests']),
      install_requires=[
          'Flask',
          'Flask-Mail',
          'gunicorn',
          'pymysql',
          'pytest-cov'
          'WTForms',
          'Flask-WTF',
      ],
      zip_safe=False)