Demo of dynamic inventory scripts, static files.

Attempt to get the list of all hosts by 
# ansible 'all' --list-hosts

but it fails saying,
ERROR! inventory/hosts:2: Section [servers:children] includes undefined group: webservers

Reason: A file, earlier in lexical order, is referencing a group which is defined in a later dynamic inventory script.


Demo the general running of scripts 
# ./inventory/inventorya.py --list

Move hosts to the last file in the order and try again.
# mv inventory/hosts inventory/zhosts

and try to get the list of hosts like, 
# ansible 'all' --list-hosts

