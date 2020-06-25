# metapxe

**Currently under construction**

## SYNOPSIS
Dynamic generation of ipxe scripts using key value pairs

## DESCRIPTION
Netbooting has existed for a while, yet it is one of the best hidden gems of modern infrastructure. Originally intended to boot large fleets of machines, there is nothing stopping you from getting the benefits of booting your own server, desktop, or laptop using this fantastic technology.

For example, if you are a tinkerer you'll probably enjoy testing different operating systems, or distributions. Booting from the network not only allows you to switch back and forth between multiple options easily, it also makes it possible to forget about dual booting, or installation media.

## FILES
- _bootconfig.ini.example_ is a inline documented configuration example
- _templates/ipxe_menu.tpl_ is a template for the common elements of a boot menu
- _templates/boot_entry.tpl_ is a template for the common denominator of boot entries
- _cgi-bin/boot.cgi_ is a python script that will read the config file, and templates, and as it receives a call with a mac address or UUID passed as a parameter, will return the custom boot menu for that particular machine

## USAGE 
At the moment, this project can make things easier, but you still need to do some work.
1. Whichever it is your dhcp server, you need to set the next-server option to point to an address hosting a tftp, and http servers. Setting this up is trivial, but I will present a guide with options soon.
2. You need to obtain a ipxe payload that will chainload a call to this project
3. You need to transfer the cgi-bin script to your http server, make sure it is available

**Help is on the way, this works, but it is WIP**

## NOTES
Rather than focusing on the language used to produce the ipxe scripts, this project is focused on providing a clean key value abstraction to ipxe scripts. It is my thesis that this will open the doors for many people to enjoy network booting.

It is planned to add multiple implementations of ipxe menu generators, that can use simple key values to produce outputs.

The priority of this project is making it easy to adopt ipxe on your machines. The roadmap will incorporate as many features as possible but initially aiming the simplest, and most common ones.

## EXAMPLE

## SEE ALSO
- CONTRIBUTING.md on this same repo
- [iPXE Project Homepage](https://ipxe.org/start)