#-*- coding: utf-8 -*-
''' This module contains the settings and
preferences
'''
import json
import os

from ..utils.defaults import __BOX_APP_SETTINGS__

class Settings:
    ''' Contains the box application settings
    '''
    def __init__(self, path=__BOX_APP_SETTINGS__):
        settings = self.read_settings_file(path)
        self.client_id = settings['boxAppSettings']['clientID']
        self.client_secret = settings['boxAppSettings']['clientSecret']
        self.public_key_id = settings['boxAppSettings']['appAuth']['publicKeyID']
        self.private_key = settings['boxAppSettings']['appAuth']['privateKey']
        self.passphrase = settings['boxAppSettings']['appAuth']['passphrase']
        self.enterprise_id = settings['enterpriseID']
        self.webhooks_primary_key = settings['webhooks']['primaryKey']
        self.webhooks_secondary_key = settings['webhooks']['secondaryKey']


    def read_settings_file(self, path):
        ''' Reads a box settings file
        and turns it into a python dictionary
        '''
        with open(path, 'r') as file:
            settings = json.load(file)
        return settings
