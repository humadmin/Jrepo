Undestanding Ansible Facts

# ansible all -m setup
# ansible local -m setup -a 'filter=ansible_default_ipv4'
# ansible local -m setup -a 'filter=ansible_devices'

Create a Playbook to display simple facts

# ansible-playbook 07-SimpleFacts.yml 

Disable facts. Un-comment the gather_facts line and then demo
# ansible-playbook 08-DisableSimpleFacts.yml 

# reset serverb system , login as root into serverb

mkdir -p /etc/ansible/facts.d

# Create the below file

vim  /etc/ansible/facts.d/hardware.fact
[asset]
class = server
id = 1234
dc = uswest
installedby = Shashi

#Save the file

run the command

# ansible serverb.lab.example.com -m setup -a "filter=ansible_local"

# ansible-playbook 09-ViewCustomFacts.yml

Display the content of servera.fact, then execute the below script. -b needed as user is devops
# ansible-playbook 10-InstallCustomFacts.yml -b

# ansible servera.lab.example.com -m setup -a "filter=ansible_local"
# ansible-playbook 11-VerifyCustomFacts.yml 

To see local variables at command line

# ansible localhost -m debug -a 'var=hostvars["localhost"]'

To see group defenitions of inventory file
cat /etc/inventory  !!!!! :-)
# ansible localhost -m debug -a 'var=groups'

