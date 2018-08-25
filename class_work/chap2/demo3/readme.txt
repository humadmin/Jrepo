Demo of managing ad-hoc commands.
First copy the ansible.cfg.original to ansible.cfg
# cp ansible.cfg.original ansible.cfg

Get the list of all hosts by 
# ansible 'all' --list-hosts

Execute an ad-hoc default "command"
# ansible all  -a /usr/bin/hostname

Execute an ad-hoc command on a difference inventory
# ansible all  -i myinvntry -a /usr/bin/hostname

Execute an ad-hoc shell 
# ansible servera* -i myinvntry -m shell  -a 'ls -l /etc/*.conf | wc -l'

Copy ansible.cfg.backup to ansible.cfg and try the command
# ansible servera* -i myinvntry -m command  -a 'cat /etc/shadow'

Execute a command with changing user and password
# ansible servera* -i myinvntry -m command  -a 'cat /etc/shadow' --become --become-user root --ask-become-pass


Execute the below command to add a user
#ansible servera.lab.example.com -i myinvntry -m user -a 'name=newbie uid=4000 state=present'

Copy ansible.cfg.backup to ansible.cfg and then run the below commands
# cp ansible.cfg.backup ansible.cfg
# ansible servera.lab.example.com -m user -a 'name=myuser uid=4000 state=present'
# ansible servera.lab.example.com -m command -a 'id myuser'
