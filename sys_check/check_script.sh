#!/bin/bash

#Various checkups on system

echo "=== CPU ==="
echo
lscpu
echo
echo

echo "=== Disk ==="
echo
lsblk
echo
echo

echo "=== PCI info ==="
echo
lspci
echo
echo

echo "=== RAM ==="
echo
free -m
echo
echo

echo "=== System Info ==="
echo
if [[ $EUID -ne 0 ]]; then
	echo "This section requires sudo privileges. Rerun with sudo!"
else
	sudo dmidecode -t system
fi

echo
echo
echo "=== END ==="


