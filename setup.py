from setuptools import setup


setup(
    name='cldfbench_cldf_desc',
    py_modules=['cldfbench_cldf_desc'],
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'cldfbench.dataset': [
            'cldf_desc=cldfbench_cldf_desc:Dataset',
        ]
    },
    install_requires=[
        'cldfbench',
    ],
    extras_require={
        'test': [
            'pytest-cldf',
        ],
    },
)
