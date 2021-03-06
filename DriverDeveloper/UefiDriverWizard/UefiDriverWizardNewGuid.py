## @file
# Subclass of NewGuid, which is generated by wxFormBuilder.
#
# Copyright (c) 2012, Intel Corporation. All rights reserved.<BR>
#
# This program and the accompanying materials are licensed and made available
# under the terms and conditions of the BSD License which accompanies this
# distribution. The full text of the license may be found at
# http://opensource.org/licenses/bsd-license.php
#
# THE PROGRAM IS DISTRIBUTED UNDER THE BSD LICENSE ON AN "AS IS" BASIS,
# WITHOUT WARRANTIES OR REPRESENTATIONS OF ANY KIND, EITHER EXPRESS OR IMPLIED.
#
##

"""Subclass of NewGuid, which is generated by wxFormBuilder."""

##
# Import Modules
#
import Config
import wx
import os
import sys
import uuid
import string
import TemplateString
import UefiDriverWizard
import UefiDriverWizardNewPackage
import UefiDriverWizardNewUefiDriver
import UefiDriverWizardNewProtocol
import UefiDriverWizardNewGuid
import UefiDriverWizardNewLibraryClass
import UefiDriverWizardUefiDriverWizard
import UefiDriverWizardUefiDriverModelOptionalFeatures
import UefiDriverWizardUefiDriverModelConsumedProtocols
import UefiDriverWizardUefiDriverModelProducedProtocols

# Implementing NewGuid
class UefiDriverWizardNewGuid( UefiDriverWizard.NewGuid ):
  def __init__( self, parent ):
    UefiDriverWizard.NewGuid.__init__( self, parent )
    if Config.PackageFile <> '':
      self.PackageFile.SetPath(Config.PackageFile)
    else:
      if Config.PackagePath <> '':
        self.PackageFile.SetPath(Config.PackagePath + os.path.sep)
      else:
        self.PackageFile.SetPath(Config.WorkspacePath + os.path.sep)
    if Config.GuidValue == '':
      Config.GuidValue = uuid.uuid1().get_urn().split(':')[2]
    self.GuidValue.SetValue(Config.GuidValue)
    self.GuidIncludeName.SetValue(Config.GuidIncludeName)

  # Handlers for NewGuid events.
  def PackageFileOnFileChanged( self, event ):
    Config.PackageFile = self.PackageFile.GetPath()

  def GuidValueOnText( self, event ):
    Config.GuidValue = event.GetString()

  def GenerateGuidOnButtonClick( self, event ):
    Config.GuidValue = uuid.uuid1().get_urn().split(':')[2]
    self.GuidValue.SetValue(Config.GuidValue)

  def GuidIncludeNameOnText( self, event ):
    Config.GuidIncludeName = Config.App.TextFieldNameValid (self.GuidIncludeName, event)

  def FinishOnButtonClick( self, event ):
    Result, Message = Config.App.CreateGuid()
    if not Result:
      dlg = wx.MessageDialog(
            self,
            Message,
            'ERROR',
            wx.OK | wx.ICON_ERROR
            )
      dlg.ShowModal()
      dlg.Destroy()
      return
    dlg = wx.MessageDialog(
          self,
          Message,
          'New GUID',
          wx.OK | wx.ICON_INFORMATION
          )
    dlg.ShowModal()
    dlg.Destroy()
    Config.GuidValue       = ''
    Config.GuidIncludeName = ''
    self.Destroy()

  def CancelOnButtonClick( self, event ):
    Config.GuidValue       = ''
    Config.GuidIncludeName = ''
    self.Destroy()
