Example
=========

This is an example of the role.

Requirements
------------

No requirements

Role Variables
--------------

message: Text for display

Dependencies
------------

No depencencies.

Example Playbook
----------------

```
    - hosts: servers
      roles:
         - { role: dobachi.ansible-role-example, message: "Hello World" }
```

License
-------

BSD

Author Information
------------------

dobachi
