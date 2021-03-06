# pyinfra
# File: example/roles/bsd_role.py
# Desc: example role that installs pip on (Open)BSD

from pyinfra.modules import server, pkg


# OpenBSD packages?
pkg.packages(
    ['py-pip', 'git'],
    sudo=True
)

# add_pkg does not automatically do this
server.shell(
    'ln -sf /usr/local/bin/pip2.7 /usr/local/bin/pip',
    sudo=True
)
