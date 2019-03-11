"""
Role tests
"""

import os
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('name', [
    ('glusterfs-client'),
    ('glusterfs-server'),
])
def test_packages(host):
    """
    Check installed package
    """

    assert host.package(nam).is_installed
