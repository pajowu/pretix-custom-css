import os
from distutils.command.build import build

from django.core import management
from setuptools import setup, find_packages


try:
    with open(os.path.join(os.path.dirname(__file__), 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except:
    long_description = ''


class CustomBuild(build):
    def run(self):
        management.call_command('compilemessages', verbosity=1)
        build.run(self)


cmdclass = {
    'build': CustomBuild
}


setup(
    name='pretix-custom-css',
    version='1.1.1',
    description='Include Custom CSS code in all pretix pages',
    long_description=long_description,
    url='https://github.com/pajowu/pretix-custom-css.git',
    author='Karl Engelhardt',
    author_email='pajowu@pajowu.de',
    license='Apache Software License',

    install_requires=[],
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    cmdclass=cmdclass,
    entry_points="""
[pretix.plugin]
pretix_custom_css=pretix_custom_css:PretixPluginMeta
""",
)
