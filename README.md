python-mac
=========

[![Galaxy Role][badge-role]][link-galaxy]
[![Build Status][badge-travis]][link-travis]
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
* yamllint


Dependencies
------------

None.

Example Playbook
----------------

    - hosts: localhost
      roles:
         - role: ansible-role-python-mac


[badge-role]: https://img.shields.io/ansible/role/47242.svg?style=flat-square
[badge-license]: https://img.shields.io/github/license/martianplatypus/ansible-role-python-mac
[badge-travis]: https://img.shields.io/travis/com/martianplatypus/ansible-role-python-mac
[link-galaxy]: https://galaxy.ansible.com/martianplatypus/python_mac/
[link-license]: https://github.com/martianplatypus/ansible-role-python-mac/blob/master/LICENSE
[link-travis]: https://travis-ci.com/github/martianplatypus/ansible-role-python-mac/
