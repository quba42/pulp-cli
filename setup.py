from setuptools import find_namespace_packages, setup

plugin_packages = find_namespace_packages(include=["pulpcore.cli.*"])
packages = plugin_packages + ["pytest_pulp_cli"]
plugin_packages.remove("pulpcore.cli.common")
plugin_entry_points = [(package.rsplit(".", 1)[-1], package) for package in plugin_packages]

long_description = ""
with open("README.md") as readme:
    for line in readme:
        if line == "## Contributing\n":
            break
        long_description += line


setup(
    name="pulp-cli",
    description="Command line interface to talk to pulpcore's REST API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pulp/pulp-cli",
    version="0.10.0.dev",
    packages=packages,
    package_data={package: ["py.typed"] for package in plugin_packages},
    python_requires=">=3.6",
    install_requires=[
        "click<8.0.0",
        "packaging",
        "PyYAML~=5.4.1",
        "requests~=2.25.1",
        "toml==0.10.2",
    ],
    extras_require={
        "pygments": ["pygments"],
        "shell": ["click-shell~=2.0"],
    },
    entry_points={
        "console_scripts": ["pulp=pulpcore.cli.common:main"],
        "pulp_cli.plugins": [f"{name}={module}" for name, module in plugin_entry_points],
    },
    license="GPLv2+",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: System :: Software Distribution",
        "Typing :: Typed",
    ],
)
