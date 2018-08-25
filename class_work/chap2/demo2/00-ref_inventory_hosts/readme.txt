Try the following commands to demo referencing host groups.

All:
# ansible 'all' --list-hosts

rename ansible.cfg.backup to ansible.cfg

Wildcard:
# ansible '*2' --list-hosts

groupa:
# ansible 'groupa' --list-hosts

groupb:
# ansible 'groupb' --list-hosts

Union:
# ansible 'groupa:groupb' --list-hosts

Intersection:
# ansible 'groupa:&groupb' --list-hosts

Exclusion:
# ansible 'groupa:!ws*' --list-hosts
