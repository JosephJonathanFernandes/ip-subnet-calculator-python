from setuptools import setup, find_packages

setup(
    name="ip_subnet_flask",
    version="0.1.0",
    description="A professional IP and subnet calculator web app (Flask)",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask>=2.0.0",
        "python-dotenv",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "ip-subnet-flask=ip_subnet_flask.__main__:app"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
