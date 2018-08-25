emo sequence.

1. yum list python
2. yum list ansible
3. yum install -y ansible

4. a. ansible all --list-hosts
   b. ansible -v all --list-hosts
 
5. a. mkdir inst-ansible
   b. cd inst-ansible
   c. vi inventory
     [dev]
      servera.lab.example.com
     [prod]
      serverb.lab.example.com

6. a. ansible all --list-hosts
   b. ansible all -i inventory --list-hosts
   c. ansible dev -i inventory --list-hosts
   d. ansible prod -i inventory --list-hosts

