[![Circle CI](https://circleci.com/gh/rackspace-orchestration-templates/mysql-multi/tree/master.png?style=shield)](https://circleci.com/gh/rackspace-orchestration-templates/mysql-multi)
Description
===========

This is a template for deploying multiple Linux servers with [MySQL
5.5](http://www.mysql.com/) and local database backups configured on the Master
ode with [Holland](https://github.com/holland-backup/holland#readme).

Requirements
============
* A Heat provider that supports the Rackspace `OS::Heat::ChefSolo` plugin.
* An OpenStack username, password, and tenant id.
* [python-heatclient](https://github.com/openstack/python-heatclient)
`>= v0.2.8`:

```bash
pip install python-heatclient
```

We recommend installing the client within a [Python virtual
environment](http://www.virtualenv.org/).

Example Usage
=============
Here is an example of how to deploy this template using the
[python-heatclient](https://github.com/openstack/python-heatclient):

```
heat --os-username <OS-USERNAME> --os-password <OS-PASSWORD> --os-tenant-id \
  <TENANT-ID> --os-auth-url https://identity.api.rackspacecloud.com/v2.0/ \
  stack-create MySQL-Repl -f mysql-multi.yaml -P flavor="4 GB Performance" \
  -P slave_count=2
```

* For UK customers, use `https://lon.identity.api.rackspacecloud.com/v2.0/` as
the `--os-auth-url`.

Optionally, set environmental variables to avoid needing to provide these
values every time a call is made:

```
export OS_USERNAME=<USERNAME>
export OS_PASSWORD=<PASSWORD>
export OS_TENANT_ID=<TENANT-ID>
export OS_AUTH_URL=<AUTH-URL>
```

Parameters
==========
Parameters can be replaced with your own values when standing up a stack. Use
the `-P` flag to specify a custom parameter.

* `master_hostname`: Sets the hostname of the MySQL master server. (Default:
  mysql-master)
* `slave_hostnames`: Sets the hostname for all MySQL slave nodes. (Default:
  mysql-slave-%index%, note %index% is replaced with the resource index ID for
  each Slave node (0, 1, 2, ... n))
* `image`: Operating system to install on all servers. (Default: Ubuntu 14.04
  LTS (Trusty Tahr))
* `flavor`: Cloud server size to use for all servers in the deployment.
  (Default: 2 GB Performance)
* `slave_count`: Number of slave nodes to provision. (Default: 1)
* `kitchen`: URL for the kitchen to clone with git. The Chef Solo run will copy
  all files in this repo into the kitchen for the chef run. (Default:
  https://github.com/rackspace-orchestration-templates/mysql-multi)
* `chef_version`: Chef client version to install for the chef run. (Default:
  11.12.8)
* `child_template`: URL to the template to use for setting up slave nodes
  (Default:
  https://raw.githubusercontent.com/rackspace-orchestration-templates/mysql-multi/master/recipes/mysql-slave.rb)

Outputs
=======
Once a stack comes online, use `heat output-list` to see all available outputs.
Use `heat output-show <OUTPUT NAME>` to get the value fo a specific output.

* `private_key`: SSH private that can be used to login as root to the server.
* `server_ip`: Public IP address of the MySQL Master server
* `mysql_root_password`: The MySQL root password.

For multi-line values, the response will come in an escaped form. To get rid of
the escapes, use `echo -e '<STRING>' > file.txt`. For vim users, a substitution
can be done within a file using `%s/\\n/\r/g`.

Stack Details
=============
#### Getting Started
If you're new to MySQL, the [Getting Started with
MySQL](http://dev.mysql.com/tech-resources/articles/mysql_intro.html)
documentation will step you through the basics of configuration, user, and
permission management.

As a part of your server configuration, your server will be configured to run
nightly backups leveraging
[Holland](https://github.com/holland-backup/holland#readme).  Backups will be
stored in the directory /var/lib/mysqlbackups directory on the master node.

#### Logging in via SSH
The private key provided in the passwords section can be used to login as
root via SSH. We have an article on how to use these keys with [Mac OS X and
Linux](http://www.rackspace.com/knowledge_center/article/logging-in-with-a-ssh-private-key-on-linuxmac)
as well as [Windows using
PuTTY](http://www.rackspace.com/knowledge_center/article/logging-in-with-a-ssh-private-key-on-windows).

#### Additional Notes
All write operations should be performed on the Master node. Read operations
can be performed against any servers in this deployment. By default, all new
and existing databases will be replicated across the members of this
deployment.

Contributing
============
There are substantial changes still happening within the [OpenStack
Heat](https://wiki.openstack.org/wiki/Heat) project. Template contribution
guidelines will be drafted in the near future.

License
=======
```
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
