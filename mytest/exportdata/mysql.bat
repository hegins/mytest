
@echo off
mysql -uroot -proot

use mytest;
truncate table asset_userhostlist;
