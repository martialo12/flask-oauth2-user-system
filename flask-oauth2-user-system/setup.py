from setuptools import setup

setup(
    name='oauth_user_system-CLI',
    version='1.0',
    packages=['cli', 'cli.commands'],
    include_package_data=True,
    install_requires=[
        'click',
    ],
    entry_points="""
        [console_scripts]
        oauth_user_system=cli.cli:cli
    """,
)
