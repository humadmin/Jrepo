Create a user on servera using the user module

# ansible -m user -a "name=user1  state=present" servera.lab.example.com

Create the playbook for above step
01-pb.yml  -> with some indetation
02-pb.yml  -> with random indetation
03-pbProperIndent.yml  -> with proper indentation
Execute all the above playbooks
# ansible-playbook 01-pb.yml
# ansible-playbook 02-pb.yml
# ansible-playbook 03-pbProperIndent.yml

Create new playbook with multiple tasks

cat  04-multipletasks.yml

Demo of syntax check and trail-run execution 
# ansible-playbook --syntax-check 04-multipletasks.yml 
# # ansible-playbook -C 04-multipletasks.yml 

