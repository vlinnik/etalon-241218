from setuptools import setup, find_packages
from AnyQt.QtCore import QLibraryInfo
import os

setup(
    name="etalon_241218",
    version="0.1.0",
    packages=find_packages(where='.'),
    install_requires=[
        # Список зависимостей вашего проекта, например:
        'PythonQwt',
        'AnyQt',
        'sqlalchemy',
        'git-versioner'
    ],
    entry_points={
        'console_scripts': [
            # Примеры:
            # 'имя-скрипта=модуль:функция',
            'etalon_241218=gui:main',
        ],
    },
    data_files=[
        ('', ['concrete6.dat','default.scada','SCADA.rcc']),
        ('ui',['ui/Home.ui','ui/Extensions.ui']),
        ('modules', ['/usr/lib/x86_64-linux-gnu/qt5/plugins/SCADA/modules/libconcrete6.so'])
    ],   
    author="Vasiliy Linnik",
    author_email="vlinnik@mail.ru",
    description="Визуализация ETALON-241218",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/vlinnik/etalon_241218",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
