from setuptools import setup, find_packages

setup(
    name="DcarbonizeWebViewer",
    version="0.1.0",
    description="A dashboard for Dcarbonize web visualization",
    url="https://github.com/Jayesh-dcarbonize/Craftsman-relevant-data",
    keywords="streamlit, speckle, visualization, pandas, plotly",
    author_email="jayesh.adlinge@dcarbonize.de",
    license="MIT",
    platforms=["Windows", "Linux", "MacOS"],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "streamlit>=1.7.0",
        "specklepy>=2.6.2",
        "pandas>=1.3.0",
        "plotly>=5.6.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
