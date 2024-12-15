from setuptools import setup, find_packages

setup(
    name="fwt_rankings",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Core API Requirements
        "aiohttp>=3.8.0",  # Für async HTTP requests
        "requests>=2.28.0",  # Für synchrone HTTP requests
        
        # PDF Generation
        "fpdf2>=2.7.0",  # Verbesserte Version von fpdf mit Unicode Support
        
        # Data Processing & Visualization
        "matplotlib>=3.5.0",  # Für Performance Charts
        "pillow>=9.0.0",     # Für Bildverarbeitung
        "python-dateutil>=2.8.0",  # Für Datumsverarbeitung
        
        # Development Tools
        "tqdm>=4.65.0",      # Für Fortschrittsbalken
        
        # Type Hints
        "typing-extensions>=4.0.0",  # Für erweiterte Type Hints
    ],
    
    # Optional dependencies
    extras_require={
        'dev': [
            'pytest>=7.0.0',
            'pytest-asyncio>=0.20.0',  # Für async Tests
            'black>=22.0.0',           # Code formatting
            'mypy>=1.0.0',             # Type checking
            'flake8>=6.0.0',           # Code linting
        ],
    },
    
    # Metadata
    author="Kai Unterrainer",
    author_email="kai.unterrainer@example.com",
    description="FWT Rankings PDF Generator using Liveheats GraphQL API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/kaiunt/fwt_rankings",
    
    # Klassifikatoren
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    
    # Python Version
    python_requires=">=3.7",
    
    # Package Data
    include_package_data=True,
    package_data={
        'fwt_rankings': ['py.typed'],  # Für MyPy Unterstützung
    },
)
