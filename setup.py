from setuptools import setup, find_packages

install_requires = [
    'asyncio'
]

test_requires = [
    'pytest',
    'pytest-timeout',
    'pytest-cov'
]

setup(name='asynctk',
      version='0.0.1',
      description='Asynchronous wrapper for tkinter',
      url='https://github.com/insolor/asynctk',
      author='insolor',
      author_email='insolor@gmail.com',
      license='MIT',
      packages=find_packages(),
      install_requires=install_requires,
      test_requires=test_requires,
      zip_safe=True)
