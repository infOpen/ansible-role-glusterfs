# glusterfs

[![Build Status](https://travis-ci.org/infOpen/ansible-role-glusterfs.svg?branch=master)](https://travis-ci.org/infOpen/ansible-role-glusterfs)

Install glusterfs package.

## Requirements

This role requires Ansible 2.5 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Local and Travis tests run tests on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- CentOS 7
- Debian Jessie
- Debian Stretch
- Ubuntu Xenial
- Ubuntu Bionic

and use:
- Ansible 2.4.x
- Ansible 2.5.x
- Ansible 2.6.x
- Ansible 2.7.x

### Running tests

#### Using Docker driver

```
$ tox
```

You can also configure molecule options and molecule command using environment variables:
* `MOLECULE_OPTIONS` Default: "--debug"
* `MOLECULE_COMMAND` Default: "test"

```
$ MOLECULE_OPTIONS='' MOLECULE_COMMAND=converge tox
```

## Role Variables

### Default role variables

``` yaml
```

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: infOpen.glusterfs }
```

## License

MIT

## Author Information

Alexandre Chaussier (for Infopen company)
- http://infopen.pro
- a.chaussier [at] infopen.pro
