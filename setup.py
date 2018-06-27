from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='LOFAR_pipeline_template',
      version='0.1',
      description='',
      long_description=readme(),
      packages=['LOFAR_pipeline_template'],
      zip_safe=True)