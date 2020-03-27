import pytest

def test_system_type(host):
    '''Check OS type'''
    assert host.system_info.type == "darwin"
    assert host.system_info.distribution == "Mac OS X"

# TODO: fix this test
# @pytest.mark.parametrize("package", [
#     "ansible-lint",
#     "molecule",
#     "virtualenv",
#     "yamllint",
# ])
# def test_pip_packages(host, package):
#     packages = host.pip_package.get_packages()
#     assert package in packages

def test_python3_installed(host):
    cmd = host.run("python --version")
    expected_version = "3."
    version = cmd.stdout.split()[1]
    assert version.startswith(expected_version)

def test_python3_path(host):
    cmd = host.run("which python3 | tr -d '\n'")
    expected_path = "/usr/local/bin/python3"
    python_path = cmd.stdout
    assert python_path == expected_path
