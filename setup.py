from setuptools import setup
"""
mypythonhelper
"""
setup(
    name="mypythonhelper",
    # wersion tuple should be parsed from __init__ code text.
    version="0.0.4",
    author="zhanghui",
    keywords="helper",
    #packages is a necessary arg which contains names of all packages in this project,
    #or getting .wheel files will just include items in packages.
    packages=["mypythonhelper", "mypythonhelper.pyspark_helper"],
    install_requires=[],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.5',
    ]
)