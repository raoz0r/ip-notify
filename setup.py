from setuptools import setup, find_packages

setup(
    name="ip_notify",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyroute2",
        "requests",
        "python-dotenv",
    ],
    entry_points={
        "console_scripts": [
            "ip-listener=ip_notify.listener:main",
            "ip-writer=ip_notify.writer:main",
            "ip-notify=ip_notify.notifier:main",
        ],
    },
)