python-mac
=========

[![MIT Licensed][badge-license]][link-license]

Uses homebrew to install Python 3 and virtualenv on MacOS 10.13 and above.

Requirements
------------

Python and virtualenv are installed via homebrew.

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
* virtualenv


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
