from setuptools import setup, find_packages

setup(
    name='overlink',
    version='0.4.0',
    description='Bridge between local PC and cloud GPU processing',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='KhanhRomVN',
    author_email='khanhromvn@gmail.com',
    url='https://github.com/KhanhRomVN/overlink',
    packages=find_packages(),
    # CHỈ giữ những package thực sự cần thiết cho cloud bridge, loại bỏ ultralytics và các package model cụ thể
    install_requires=[
        'flask',
        'pyngrok',
        'opencv-python-headless',
        'numpy',
        'requests'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    keywords='cloud gpu ngrok yolov8 ultralytics',
)