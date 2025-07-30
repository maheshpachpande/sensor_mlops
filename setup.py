from setuptools import setup, find_packages

def parse_requirements(filename):
    """Read dependencies from requirements.txt, excluding editable installs."""
    with open(filename, encoding="utf-8") as f:
        lines = f.read().splitlines()
        return [
            line.strip() for line in lines
            if line and not line.startswith(("-e", "#")) and "git+" not in line
        ]

setup(
    name="sensor",
    version="0.1.0",
    author="Your Name",
    description="Sensor ML project",
    packages=find_packages(),
    install_requires=parse_requirements("requirements.txt"),
    python_requires="==3.12.*",  # ✅ Enforce Python 3.12 only
)
