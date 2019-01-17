#-*- coding: utf-8 -*-
''' Test the settings module
'''

from ..settings.settings import Settings

class TestSettings:
    def setup_method(self):
        """ Instantiate the settings class
        """
        self.settings = Settings('.box/fake_jwt.json')

    def test_client_id(self):
        assert self.settings.client_id == "qm07vgu6o41a86ct6k20wvj1dbhxtvwj"
    
    def test_client_secret(self):
        assert self.settings.client_secret == "FCIfOzIOPnRhsUXjQyNnwrxLAfqz8yYh"

    def test_public_key_id(self):
        assert self.settings.public_key_id == "fdt7840b"

    def test_private_key(self):
        assert self.settings.private_key == "-----BEGIN ENCRYPTED PRIVATE KEY-----\nMIIFDjBABgkqhkiG9w0BBQ0wMzAbBgkqhkiG9w0BBQwwDgQI9EBYmkRkTD8CAggA\nMBQGCCqGSIb3DQMHBAjeIF4owI/KSwSCBMjgFhV6p9aaWPV1IPwHARXe9W97cGdO\nzQsWnkkvHY2wGsvryxhdXddluNXUSWVLjUiF2GW8EEvyjYR5s+HjfqbTR5AgwofG\nuy1+BpREp66g3amftIypvrnFXXM4ig7+IGL+J9g70e5SA7yX7zUxEP/UefyATKyM\nZvIEbGsjJ5fcQbnSBd4rGcstuChTmrL3n9a5eQNyO3sobHHd0rZZ8xjWQ/jvHTeB\n0Yz0ZMqywDRDGKCSycyJNdyZbbl2YsZLu3zfhra2EFm9AkEZ6Erklws/4LZIbzZT\nMZfjYwukXRPHxtwt881nkXEbReFn3LwSqqUlzTeDXCsCK7ibvutM861a14+4VI4k\ninKXhigA+Q67y1wULEu2TJHxrZDuTiCHKNS7Q4RVU8AdpqtxXWhkJJCLVFT62fjf\n+7TlnrcTPV3F5rSDPoBVNjFXe7L7SxWAZvp0S4DD0K1TKlP9r5b4tAnG/Hhz0NHB\nAw3RyTUSLEl6Oi9kER+DwiYy4M+/2LVnnGqbGvHILf17n5bpVJvdBE/VIhAaQXlr\nhCQQhnSepkEJclWKTCEP7UTzMVV6rKG2JQBntB7H0HZ51h7Ty5LFg2cDtXDCgMle\nDtoVBn1wtAoYlk6hYFbCI5ZurGjWYXr13VGcM9psRKwWzi1Qd4Y0axv94aH9Mtwo\nvSO8E72pIr7/gyAHevLboGjU/xYkvOQv4/7yusyzePLPXocxuJP9bq/KKNNzp7Nw\npzeCWF1ezR30SNxeeM+wzXIr1qaFOIsQ3Qqp/Al9bF1crD/SYETpMvzXoVW808i0\nREBaZYTXwXqJTIyY1Q+so7QAvU33JM06ZClSRGN/Q8rXEwfkUGpe+mXf4684ZpDz\n9KKRkDqutyq0mU5LLLR0pFSNmDgV0uW0IY2663fPJFaCignbaSaLyDgsilPGoQgg\nv20POPAXY7LoiFoJ69IfTnXvFlGtjYlgphR/c8YuWjnmNVj6b7nsuACu986biucR\nCSuZdVgTg7K2H9ImPDll39M6VVgubkjIz5FP9DZqrKeKINVRwRUEKn/PTlmv0cAh\nHR66AB75crniVzv/1FxZ2LwjoHMilVbhiaXIyrft27/0/df3j7AAC8RjZ3JOfwJY\nLfvw4Nt9QQyAZ61vF2DEwONLknZ7+dsF4WPo32+Rb/YhV8tEqDS5wZCWZhKtAfyv\ncqGO3lmXSMeF7GOE5SaNNjM7xwZWoxTLGwdSlZrIjnsrPz3XHBNSbqbJW7l4KZMu\nQCqAlghJ+/XWQgDWnFZuNEM5rGpCMUuCK/RFUTySe2L+g+2ZhaEm2lKu+v2ep8rB\nyFiZgGZWvFojIqd3GrSCHJFM+LiCBahnH1unTJTnbZ1JdQV/QtzebszFPVA5uSY4\nQ/oRudpSPLPCegW7/jkdu+Mfm39nwZJN0m4aw1g6a3cEIbYdNFcsJuYYFhMYlY2U\n73SH98BJ1MlBejvZq/Ph5C45FK2cZNhpcJZkL/Jn/KMuk7hCHX18CEekXSpTv3KZ\ng9XRDneRx50/DdmSruGZR7Za2D90/KEtbFusn6iQnNhU8sy1BE0Rd+/2BNUNgD3N\n00Z7XZqy9SQvol9tW54L8E/JvRCum5ZG2J2wqUQBHRZB2cA0TVwQCei1+BBqBiex\nv0Q=\n-----END ENCRYPTED PRIVATE KEY-----\n"

    def test_passphrase(self):
        assert self.settings.passphrase == "0e0c57a7daf7d0e30672f329b3270447"

    def test_enterprise_id(self):
        assert self.settings.enterprise_id == "20675415"

    def test_webhooks_primary_key(self):
        assert self.settings.webhooks_primary_key == "viLEp36APtS20wIrOcrPQGSkW24oGvV8"

    def test_webhooks_secondary_key(self):
        assert self.settings.webhooks_secondary_key == "G0EQpQZHQpcjRN9qQy1oLTTMIt5ljrOI"
