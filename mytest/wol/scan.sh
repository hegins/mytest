#!/bin/bash
str=`nmap -T4 -p 0 $1 | grep "Nmap done" `
up=`echo $str | awk '{print $6}'`
echo `expr ${up#*(} `
