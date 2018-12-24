import setuptools 

setuptools.setup(name='tagcounter_by_AB',
                 version='0.1',
                 description='Intro to Python hometask',
                 author='Aliaksandr Bandarchyk',
                 url='https://github.com/abandarchyk/tagcounter',
                 packages=['tagcounter'],
                 package_data={'tagcounter': ['conf/config.yaml', 'db/scan_results.db']},
                 install_requires=[
                        'beautifulsoup4',
                        'requests',
                        'pyaml'
                       ],
                 entry_points={'console_scripts': ['tcrun = tagcounter.runner:main']}
                 )
