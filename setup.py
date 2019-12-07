from setuptools import find_packages, setup

requirements = [
    "Click>=7.0",
]


setup(
    author="Lionel Herman Bersee",
    author_email="lionel1232@gmail.com",
    python_requires=">=3",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.8",
    ],
    description="A Python module that simulates a toy robot moving around on a table.",
    entry_points={"console_scripts": ["toy_robot=toy_robot_challenge.cli:main"]},
    install_requires=requirements,
    license="MIT license",
    keywords="toy_robot_challenge",
    name="toy_robot_challenge",
    packages=find_packages(include=["toy_robot_challenge"]),
    test_suite="tests",
    url="https://github.com/Lionel1232/toy_robot_challenge",
    version="0.1.0",
    zip_safe=False,
)
