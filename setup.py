import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

    PROJECT_NAME = "oneNeuron_pypi"
    USER_NAME = "kkkumar2"

setuptools.setup(
    name=f"{PROJECT_NAME}-{USER_NAME}",
    version="0.0.4",
    author=USER_NAME,
    author_email="kmohankumar123456@gmail.com",
    description="This is a Single layer Perceptron package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{USER_NAME}/{PROJECT_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{USER_NAME}/{PROJECT_NAME}",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
#    with open("requirements.txt", "r", encoding="utf-8") as fh:
#    install_requires = fh.read()
#    install_requires_content_type="text/plain"
    install_requires = ["numpy","tqdm","pandas","matplotlib","logging","joblib"]

)