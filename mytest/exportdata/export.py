#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mytest.settings")

import django
django.setup()

from asset.models import serverlist

def main():
 f = open('servers.txt')
 for line in f:
    parts= line.split('|')
    serverlist.objects.create(ip=parts[1], Cmac=parts[2], Cname=parts[3],user=parts[4], position=parts[5], server=parts[6], OS=parts[7])

 f.close()


if __name__ == "__main__":
    main()
    print('Done!')