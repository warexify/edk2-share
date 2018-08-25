## @file
# Subclass of UefiDriverModelConsumedProtocols, which is generated by wxFormBuilder.
#
# Copyright (c) 2012 - 2018, Intel Corporation. All rights reserved.<BR>
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

"""Subclass of UefiDriverModelConsumedProtocols, which is generated by wxFormBuilder."""

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

# Implementing UefiDriverModelConsumedProtocols
class UefiDriverWizardUefiDriverModelConsumedProtocols( UefiDriverWizard.UefiDriverModelConsumedProtocols ):
  def __init__( self, parent ):
    UefiDriverWizard.UefiDriverModelConsumedProtocols.__init__( self, parent )
    self.UefiDriverConsumedProtocols.SetCheckedStrings(Config.UefiDriverConsumedProtocols)

  # Handlers for UefiDriverModelConsumedProtocols events.
  def UefiDriverConsumedProtocolsOnCheckListBoxToggled( self, event ):
    if self.UefiDriverConsumedProtocols.GetCheckedStrings() == ():
      self.UefiDriverConsumedProtocols.SetCheckedStrings(Config.UefiDriverConsumedProtocols)
      return
    Config.UefiDriverConsumedProtocols = tuple(set(self.UefiDriverConsumedProtocols.GetCheckedStrings()) - set(Config.UefiDriverConsumedProtocols))
    self.UefiDriverConsumedProtocols.SetCheckedStrings(Config.UefiDriverConsumedProtocols)

  def PrevOnButtonClick( self, event ):
    self.Destroy()
    frame = UefiDriverWizardUefiDriverModelOptionalFeatures.UefiDriverWizardUefiDriverModelOptionalFeatures (None)
    frame.Show()

  def NextOnButtonClick( self, event ):
    self.Destroy()
    frame = UefiDriverWizardUefiDriverModelProducedProtocols.UefiDriverWizardUefiDriverModelProducedProtocols (None)
    frame.Show()

  def FinishOnButtonClick( self, event ):
    if Config.UefiDriverName == '':
      Config.UefiDriverName = os.path.split(Config.UefiDriverPath)[-1]
    Result, Message = Config.App.CreateUefiDriver()
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
          'New UEFI Driver',
          wx.OK | wx.ICON_INFORMATION
          )
    dlg.ShowModal()
    dlg.Destroy()
    Config.UefiDriverName    = ''
    Config.UefiDriverVersion = ''
    Config.UefiDriverGuid    = ''
    self.Destroy()

  def CancelOnButtonClick( self, event ):
    Config.UefiDriverName    = ''
    Config.UefiDriverVersion = ''
    Config.UefiDriverGuid    = ''
    self.Destroy()
