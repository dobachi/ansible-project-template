# ansible-project-template

## About contents

### ansible.cfg

An example of ansible.cfg based on [Official ansible.cfg Example] .
The differences are like the following.

- Use inventory in the project directory (not /etc/ansible/hosts)
- Add roles directoy in the project directory 

[Official ansible.cfg Example]: https://github.com/ansible/ansible/blob/devel/examples/ansible.cfg

###  hosts

An example of inventory file.
This inventory includes the top leve group and sample child group.

### group_vars

Most of variables used in roles are changed via hosts_vars.

### roles

Roles used in playbooks in this repository.
You can add new roles using `ansible-galaxy` command.

### playbook directory

Playbooks for configuring and operating machines.

The sub-directries are separated intto `conf` and `op` .

`conf` includes playbooks for the configuration. e.g. installing middleware

`op` includes playbooks for the operation. e.g. starting middleware

## How to execute

```
$ ansible-playbook playbook/conf/example.yml -c local
$ ansible-playbook playbook/op/example.yml -c local
```

## How to use this project

Clone this this repository on GitHub.
Pull to local and modify it.

Or, you can download this repository from [Release page on GitHub] .

```
$ git clone https://github.com/dobachi/ansible-project-template.git ansible-your-project
```


[Release page on GitHub]: https://github.com/dobachi/ansible-project-template/releases

## License

GNU General Public License v3.0 or later

Please read COPYING.txt for the detail.

<!-- vim: set et ts=2 sw=2: -->
