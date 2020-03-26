python-mac
=========

[![MIT Licensed][badge-license]][link-license]

Uses homebrew to install Python 3 and virtualenv on MacOS 10.13 and above.

Requirements
------------

Python 3 through homebrew and virtualenv via pip.

Hombrew can be installed using the following command in a terminal:
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

Alternatively, you can install homebrew using this role:
```
ansible-galaxy install geerlingguy.homebrew
```

Role Variables
--------------

A list of homebrew packages to be installed:
```
homebrew_packages
```
* python

A list of python modules installed with pip
```
pip_modules
```
* virtualenv
* ansible-lint
* yamllint


Dependencies
------------

None.

Example Playbook
----------------

    - hosts: localhost
      roles:
         - role: ansible-role-python-mac


[badge-license]: https://img.shields.io/github/license/martianplatypus/ansible-role-virtual-mac
[link-license]: https://github.com/martianplatypus/ansible-role-virtual-mac/blob/master/LICENSE
