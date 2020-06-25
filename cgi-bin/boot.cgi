#!/opt/local/bin/python
import cgi
import cgitb
import logging

from string import Template
from configparser import ConfigParser

def main():
    form = cgi.FieldStorage()
    print("Content-Type: text/plain;charset=utf-8")
    print()
    if 'mac' in form:
        getIPXEMenu(form['mac'].value)
    else:
        print("No hardware address provided")

def getIPXEMenu(hwAddress):
    config = ConfigParser(allow_no_value=True, default_section='common')

    config.read('bootconfig.ini')
    with open(config.get('common','menuTemplate'),'r') as menuTemplate:
        ipxeMenuTemplate = menuTemplate.read()
    with open(config.get('common','bootTemplate'),'r') as bootTemplate:
        bootEntryTemplate = bootTemplate.read()

    #get boot options for this machine
    bootEntries = config.get('machines', hwAddress).split(',')

    targets = []
    for entry in bootEntries:

        entryParameters = {
            "name": entry,
            "kernel": config.get(entry, 'kernel'),
            "initrd": config.get(entry, 'initrd')
        }
        targets.append(Template(bootEntryTemplate).substitute(entryParameters))

    menuParameters = {
        "menuTitle": config.get('common', 'menuTitle'),
        "bootOptions": "\n".join(["item {}\t{}".format(x, config.get(x, 'description')) for x in bootEntries]),
        "defaultBootOption": bootEntries[0],
        "timeout": config.get('common', 'timeout'),
        "bootTargets": "\n".join(targets)
    }

    ipxeMenu = Template(ipxeMenuTemplate).substitute(menuParameters)
    print(ipxeMenu)

if __name__ == '__main__':
    main()