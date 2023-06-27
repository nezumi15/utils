from setuptools import setup, find_packages

setup(
  name="cookiecutter-utils",
  version="0.0.1",
  install_requires=[
    "action==1.4.4",
    "blessed==1.19.0",
    "boto3==1.24.9",
    "botocore==1.27.37",
    "cookiecutter==2.1.1",
    "gitdb==4.0.9",
    "GitPython==3.1.20",
    "inquirer==2.8.0",
    "jmespath==0.10.0",
    "python-dateutil==2.8.2",
    "python-editor==2.0.1",
    "readchar==2.0.1",
    "six==1.16.0",
    "smmap==5.0.0",
    "typing_extensions==4.1.1",
    "urllib3==1.26.15",
    "wcwidth==0.2.6",
  ],
  packages=find_packages(),
  entry_points={
    "console_scripts": [
      "cookiecutter_utils = cookie_utils.main:main",
    ]
  },
  include_package_data=True,
)
