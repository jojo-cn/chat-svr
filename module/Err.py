"""
错误代码
"""


class Err(object):
    """ """

    def __init__(self):
        super(Err, self).__init__()

    # User module handle error
    USER_LOGON_FAILED = 'Username or password is wrong'
    # User already logon
    USER_ALREADY_LOGON = 'The user is already logon'
