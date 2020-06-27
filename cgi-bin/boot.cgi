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
    if 'id' in form:
        getIPXEMenu(form['id'].value)
    else:
        print("boot.cgi")
        print("/////////////////////")
        print("Usage: boot.cgi?id=<hwAddress>")
        print("       boot.cgi?id=<machineUUID>")

def getIPXEMenu(machineId):
    config = ConfigParser(allow_no_value=True, default_section='common')

    config.read('bootconfig.ini')
    with open(config.get('common','menuTemplate'),'r') as menuTemplate:
        ipxeMenuTemplate = menuTemplate.read()
    with open(config.get('common','bootTemplate'),'r') as bootTemplate:
        bootEntryTemplate = bootTemplate.read()

    #get boot options for this machine
    bootEntries = (config.get('machines', machineId) if config.has_option('machines', machineId) 
                   else config.get('machines', 'default')).split(',')

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
        "menuAlert": "" if config.has_option('machines', machineId) else config.get('common', 'menuAlert'),
        "bootOptions": "\n".join(["item {}\t{}".format(x, config.get(x, 'description')) for x in bootEntries]),
        "defaultBootOption": bootEntries[0],
        "timeout": config.get('common', 'timeout'),
        "bootTargets": "\n".join(targets)
    }

    ipxeMenu = Template(ipxeMenuTemplate).substitute(menuParameters)
    print(ipxeMenu)

if __name__ == '__main__':
    main()