#!/bin/sh


dmgbuild -s settings.py -D app=Woffle.app "Woffle" Woffle-Installer.dmg

if [ -f Woffle-Installer.dmg ]; then
	mv Woffle-Installer.dmg installer/Woffle-Installer.dmg
fi
