""""Set up for locally run RAG pipelines
"""

import setuptools

# with open("README.md", "r", encoding="utf-8") as fh:
#     long_description = fh.read()

setuptools.setup(
    name=f"rag_pipeline",
    version="0.1.0",
    author="OZSoftCon",
    author_email="ozsoftcon@gmail.com",
    description="Sample RAG Pipeline",
    long_description="",
    long_description_content_type="text/markdown",
    #url="https://github.com/pypa/sampleproject",
    #project_urls={
    #    "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    #},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(include=[
        'rag_pipeline',
        'rag_pipeline.index_pipeline',
        'rag_pipeline.retrieval',
        'rag_pipeline.utility'
    ]),
    python_requires=">=3.9, <4.0"
)