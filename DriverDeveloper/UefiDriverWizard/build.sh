#!/usr/bin/env bash
## @file
# Shell file to convert UEFI Driver Wizard to APP
#

#
# Use PyInstaller to Convert UEFI Driver Wizard Python application to an APP
# pyi-makespec --onefile --icon Logo.icns --windowed --name UefiDriverWizard.Generated --osx-bundle-identifier org.tianocore.UefiDriverWizard launch.py
pyinstaller UefiDriverWizard.spec
