from setuptools import setup, find_packages

from code2flowdiagram.engine import VERSION

url_base = 'https://github.com/KeilanEvans/code2flowdiagram'
download_url = f'{url_base}/releases'

setup(
    name='code2flowdiagram',
    version=VERSION,
    description='Visualize your source code as DOT flowcharts',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    entry_points={
        'console_scripts': ['code2flowdiagram=code2flowdiagram.engine:main'],
    },
    license='MIT',
    author='Keilan Evans',
    url=url_base,
    download_url=download_url,
    packages=find_packages(),
    python_requires='>=3.6',
    include_package_data=True,
    package_data={
        'code2flowdiagram': ['graphviz/bin/*'],
    },
    classifiers=[
        'Natural Language :: English',
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
