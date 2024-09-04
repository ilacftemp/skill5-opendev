from setuptools import setup

setup(name='dev_aberto_ilanaf',
      version='0.1',
      author='Ilana Finger',
      python_requires='>=3.6',
      packages=['dev_aberto'],
      install_requires=[
            'requests'
      ],
      scripts=['scripts/hello.py']
      )