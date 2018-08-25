Demonstrate simple variables

Here variable defined in playbook itself
# ansible-playbook 01-SimpleVariable.yml

Here variable defined in inventory file. check hostname local
# ansible-playbook 01A-SimpleVariable.yml

Here variable frim include file is demonstrated
# ansible-playbook 01B-SimpleVariable.yml

Demonstrate variable inside a inventory file
# ansible-playbook 02-VarsInsideInventory.yml

Value of variable coming from inventory file
# ansible-playbook 02A-VarsInsideInventory.yml

Values of variables being overridden and scope of variable demonstrated
# ansible-playbook 02B-VarsInsideInventory.yml


Demo for host_vars and group_vars
# ansible-playbook 03-Host-GroupVars.yml

Demonstrate Array variable
# ansible-playbook 04-ArrayVars.yml

Demo for seeiing registered variable outputs
# ansible-playbook 05-RegistedVars.yml

Overiding variables from command line
# ansible-playbook 03-Host-GroupVars.yml -e package=zsh

Example of deployment using variables 
# ansible-playbook 06-DeployVars.yml

