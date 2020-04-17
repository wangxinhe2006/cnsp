import setuptools
from cnsp import __version__

setuptools.setup(
    name='cnsp',  # Replace with your own username
    version=__version__,
    author='汪心禾',
    author_email='wangxinhe06@gmail.com',
    description='Search predictions in mainland China',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/wangxinhe2006/cnsp',
    packages=['cnsp'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
