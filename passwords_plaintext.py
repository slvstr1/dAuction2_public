from django.contrib.auth.hashers import BasePasswordHasher

class PlainTextPassword(BasePasswordHasher):
    algorithm = "plain"

    def salt(self):
        return ''

    def encode(self, password, salt):
        assert salt == ''
        pass_encoded = "plain" + "$$" + str(password)
        return pass_encoded

    def verify(self, password, encoded):
        pass_encoded2 = "plain" + "$$" + str(password)
        return pass_encoded2 == encoded

    def safe_summary(self, encoded):
        return OrderedDict([
            (_('algorithm'), self.algorithm),
            (_('hash'), encoded),
        ])
