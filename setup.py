from setuptools import setup, find_packages

setup(
    name="AISecGuard",
    version="0.1.0",
    description="AI Security Testing and Auditing Toolkit",
    author="Your Name",
    author_email="you@example.com",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests>=2.31.0",
        "PyYAML>=6.0.1",
        "shap>=0.44.0",
        "scikit-learn>=1.3.2",
        "streamlit>=1.32.0",
        "textattack>=0.3.9",
        "matplotlib>=3.8.2"
    ],
    entry_points={
        "console_scripts": [
            "aisecguard=reports.compliance.generator:generate_report"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
)
