#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.extend([BASE_DIR,])

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mytest.settings" )

import django
django.setup()

from asset.models import userhostlist

def main():
 f = open('host.txt')
 for line in f:
    print(line)
    parts= line.split('|')
    hostname=parts[4].replace('\n','')
    userhostlist.objects.create(ip=parts[1], mac=parts[2], hostname=hostname,username=parts[3])

 f.close()


if __name__ == "__main__":
    main()
    print('Done!')