from distutils.core import setup

setup(
    name = 'python-mcprofiles',
    packages = ['mcprofiles'],
    version = '1.0',
    description = 'Python interface for Minecraft profile web API.',
    author = 'Brad Reardon',
    author_email = 'brad.jay.reardon@gmail.com',
    url = 'https://github.com/bradreardon/python-mcprofiles',
    keywords = [''],
    classifiers = [],
    requires=['requests']
)