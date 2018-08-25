mkdir vars
ansible-vault create vars/secret.yml

ansible-playbook 01-playbook.yml --ask-vault-pass
