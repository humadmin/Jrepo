Copy XX-ansible.cfg to ansible.cfg in the same folder and 
run ansible command below to show the differences.


# cp 01-ansible.cfg ansible.cfg
#ansible remote -m command -a whoami
This shows  student user. as currently logged in user, we have executed this command.

We are now specifing a new user shashi, currently not present, will add after this command execution
# cp 02-ansible.cfg ansible.cfg 

Observer user is now shashi


We are not forcing to ask password
# cp 03-ansible.cfg ansible.cfg


# cp 04-ansible.cfg ansible.cfg

