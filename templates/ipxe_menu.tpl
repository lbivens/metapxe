#!ipxe
:start
menu $menuTitle $menuAlert
item
item --gap -- \\\\\ Operating systems 
$bootOptions
item --gap -- \\\\\ Utilities 
item shell    Enter iPXE shell
item reboot   Reboot
item
item exit     Exit (boot local disk)
choose --default $defaultBootOption --timeout $timeout target && goto $${target}

:shell
echo Type exit to get the back to the menu
shell
set menu-timeout 0
goto start

$bootTargets

:reboot
reboot

:exit
exit