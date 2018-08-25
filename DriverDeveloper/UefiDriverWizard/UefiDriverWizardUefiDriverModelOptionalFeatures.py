## @file
# Subclass of UefiDriverModelOptionalFeatures, which is generated by wxFormBuilder.
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

"""Subclass of UefiDriverModelOptionalFeatures, which is generated by wxFormBuilder."""

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

# Implementing UefiDriverModelOptionalFeatures
class UefiDriverWizardUefiDriverModelOptionalFeatures( UefiDriverWizard.UefiDriverModelOptionalFeatures ):
  def __init__( self, parent ):
    UefiDriverWizard.UefiDriverModelOptionalFeatures.__init__( self, parent )
    self.UefiDriverDriverModelFeatures.SetCheckedStrings(Config.UefiDriverDriverModelFeatures)
    self.Rfc4646LanguageCodes.SetValue (Config.Rfc4646LanguageCodes)
    self.Iso639LanguageCodes.SetValue  (Config.Iso639LanguageCodes)
    Rfc = False
    Iso = False
    if u"HII Packages for forms and HII based configuration " in Config.UefiDriverDriverModelFeatures:
      Rfc = True
    if u"Component Name 2 Protocol" in Config.UefiDriverDriverModelFeatures:
      Rfc = True
    if u"Component Name Protocol" in Config.UefiDriverDriverModelFeatures:
      Iso = True
    if u"Driver Diagnostics 2 Protocol" in Config.UefiDriverDriverModelFeatures:
      Rfc = True
    if u"Driver Diagnostics Protocol" in Config.UefiDriverDriverModelFeatures:
      Iso = True
    if u"Driver Configuration 2 Protocol" in Config.UefiDriverDriverModelFeatures:
      Rfc = True
    if u"Driver Configuration Protocol" in Config.UefiDriverDriverModelFeatures:
      Iso = True
    if Rfc:
      self.Rfc4646LanguageCodes.Enable()
    else:
      self.Rfc4646LanguageCodes.Disable()
    if Iso:
      self.Iso639LanguageCodes.Enable()
    else:
      self.Iso639LanguageCodes.Disable()

  # Handlers for UefiDriverModelOptionalFeatures events.
  def UefiDriverDriverModelFeaturesOnCheckListBoxToggled( self, event ):
    Config.UefiDriverDriverModelFeatures = self.UefiDriverDriverModelFeatures.GetCheckedStrings()
    Rfc = False
    Iso = False
    if u"HII Packages for forms and HII based configuration " in Config.UefiDriverDriverModelFeatures:
      Rfc = True
    if u"Component Name 2 Protocol" in Config.UefiDriverDriverModelFeatures:
      Rfc = True
    if u"Component Name Protocol" in Config.UefiDriverDriverModelFeatures:
      Iso = True
    if u"Driver Diagnostics 2 Protocol" in Config.UefiDriverDriverModelFeatures:
      Rfc = True
    if u"Driver Diagnostics Protocol" in Config.UefiDriverDriverModelFeatures:
      Iso = True
    if u"Driver Configuration 2 Protocol" in Config.UefiDriverDriverModelFeatures:
      Rfc = True
    if u"Driver Configuration Protocol" in Config.UefiDriverDriverModelFeatures:
      Iso = True
    if Rfc:
      self.Rfc4646LanguageCodes.Enable()
    else:
      self.Rfc4646LanguageCodes.Disable()
    if Iso:
      self.Iso639LanguageCodes.Enable()
    else:
      self.Iso639LanguageCodes.Disable()

  def Rfc4646LanguageCodesOnText( self, event ):
    Config.Rfc4646LanguageCodes = event.GetString()

  def Iso639LanguageCodesOnText( self, event ):
    Config.Iso639LanguageCodes = event.GetString()

  def PrevOnButtonClick( self, event ):
    self.Destroy()
    frame = UefiDriverWizardNewUefiDriver.UefiDriverWizardNewUefiDriver (None)
    frame.Show()

  def NextOnButtonClick( self, event ):
    self.Destroy()
    frame = UefiDriverWizardUefiDriverModelConsumedProtocols.UefiDriverWizardUefiDriverModelConsumedProtocols (None)
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
