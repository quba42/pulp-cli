from pulpcore.cli.common import main

# from pulpcore.cli.container.repository import repository
# from pulpcore.cli.container.repository_version import version
from pulpcore.cli.container.remote import remote

# from pulpcore.cli.container.publication import publication
# from pulpcore.cli.container.distribution import distribution


@main.group()
def container() -> None:
    pass


# container.add_command(repository)
# container.add_command(version)
container.add_command(remote)
# container.add_command(publication)
# container.add_command(distribution)