from setuptools import setup, find_packages
from setuptools_scm import get_version

setup(
    name="etalon_241218",
    # version=get_version(),
    packages=find_packages(where='.'),
    install_requires=[
        # Список зависимостей вашего проекта, например:
        'PythonQwt',
        'AnyQt',
        'sqlalchemy',
    ],
    entry_points={
        'gui_scripts': [
            # Примеры:
            # 'имя-скрипта=модуль:функция',
            'etalon-241218=gui.__main__:main',
        ],
    },
    data_files=[
        ('', ['concrete6.dat','default.scada','SCADA.rcc']),
        ('ui',['ui/Home.ui','ui/Extensions.ui']),
        # ('modules', ['/usr/lib/x86_64-linux-gnu/qt5/plugins/SCADA/modules/libconcrete6.so'])
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
    use_scm_version=True,
)
