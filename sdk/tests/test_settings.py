#-*- coding: utf-8 -*-
''' Test the settings module
'''

from ..settings.settings import Settings

def test_settings_client_id():
    settings = Settings('.box/cwe_jwt.json')
    assert settings.client_id == 'dtpjtnxuo7v7hdwy5meuv1l22ti7wct7'
    
