from setuptools import setup, find_packages


__version__ = "0.0.1"


setup(
    # package name in pypi
    name='pm.recipe.shinken',
    # extract version from module.
    version=__version__,
    description="A buildout recipe to install Shinken.",
    long_description="",
    classifiers=[],
    keywords='',
    author='Lars van de Kerkhof',
    author_email='lars@permanentmarkers.nl',
    url='https://github.com/permanentmarkers/pm.recipe.shinken',
    license='ZPL',
    # include all packages in the egg, except the test package.
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    # for avoiding conflict have one namespace for all apc related eggs.
    namespace_packages=['pm', 'pm.recipe'],
    # include non python files
    include_package_data=True,
    zip_safe=False,
    # specify dependencies
    install_requires=[
        'setuptools',
        'zc.buildout',
        'zc.recipe.egg',
    ],
    # generate scripts
    entry_points={
        'console_scripts':[
            'script_name = name.module:main',
        ]
    },
)
