import os

__location__ = os.path.dirname(__file__)

import setuptools

setuptools.setup(
    name='spark-df-profiling',
    version='1.1.13',
    author='Julio Antonio Soto de Vicente',
    author_email='julio@esbet.es',
    packages=['spark_df_profiling'],
    url='https://github.com/julioasotodv/spark-df-profiling',
    license='MIT',
    description='Create HTML profiling reports from Apache Spark DataFrames',
    install_requires=[
        "pandas>=0.25",
        "matplotlib>=3.2",
        "jinja2>=2.11",
        "six>=1.15"
    ],
    extras_require={
            "notebook": [
                "jupyter-client>=6.0.0",
                "jupyter-core>=4.6.3",
                "ipywidgets>=7.5.1",
            ],
        },
    include_package_data = True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering',
        'Framework :: IPython',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'

    ],
    keywords='spark pyspark report big-data pandas data-science data-analysis python jupyter ipython',
    python_requires=">=3.6",
)
