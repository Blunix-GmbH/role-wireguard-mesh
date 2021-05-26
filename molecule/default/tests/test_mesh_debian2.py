import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('bullseye2')


def test_debian1_reachable(host):
    command = host.run("ping -c 1 172.16.0.5")
    assert command.rc == 0


def test_debian2_reachable(host):
    command = host.run("ping -c 1 172.16.0.6")
    assert command.rc == 0


def test_debian3_reachable(host):
    command = host.run("ping -c 1 172.16.0.7")
    assert command.rc == 0
