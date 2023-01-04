from setuptools import find_packages, setup


with open("requirements.txt", "r") as f:
    requirements = f.read()
requirements = requirements.split("\n")[:-1]


setup(
    name="BLIP -pycocotools",
    version="1.0.0",
    url="https://tryrelevance.com/",
    author="Relevance AI",
    author_email="dev@tryrelevance.com",
    packages=find_packages(),
    setup_requires=["wheel"],
    install_requires=requirements,
    package_data={
        "": [
            "*.ini",
        ]
    },
)
