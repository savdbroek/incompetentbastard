# incompetentbastard

*Not so fine (you'll find out) bash and python scripts for incompetent bastards, like myself.*



## Bash scripts currently on board


### ./init.sh (always use this function first)

This script will


...

### ./scan.sh (always use this function second)

This wil take a basic nmap scan of the network. For example mylocalnetwork

```./scan.sh eth0 mylocalnetwork 12.3.4/24```




### ./search.sh

Completed the scan with `scan.sh`? `search.sh` greps the output

Find all host's Up:
```./search.sh mylocalnetwork up```

Find all MS SMB shares:
```./search.sh mylocalnetwork microsoft-ds```

Find all Samba share
```./search.sh mylocalnetwork Samba```

Etc. Use your imagination. 

### ./revershells.sh

Generates some reverse shells and a txt file for some good ol' copy & paste.
Currently default's to port 443 you. Change this by giving the port als a second option.
You'll find the generated shells and the textfile shell_443.txt in the directory http/payloads.

Usage (with port set to default port):
```./reverseshell.sh eth0```
Or to change the port to 4444:
```./reverseshell.sh eth0 4444```

The reverse shells are taken from 

### ./shell.sh

Connect to a screen

### ./sshuttle.sh

Obvious

### ./commands.sh

inject a file from http/commands in to a screen session

```./commands.sh screenname filename```

### ./kerberos.sh
Get info from domain controlers

Usage:
```./kerberos.sh mylocalnetwork```

### ./ftp_anon.sh
Enumerates all open ftp shares with nmap.

Usage:
```./ftp_anon.sh mylocalnetwork```

### ./ftp_asp.sh

todo

### ./rfi_input.sh

This one utilizes `php://input%00`



# dependancies

For MacOS, this might help...


- ip `brew install iproute2mac`
- mono/ xbuild `brew install mono`
- ` pip3 install dnsrecon asciinema nmaptocsv`



