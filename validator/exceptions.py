from validator.utils import _unicode_if


class _BaseStateError(BaseException):
    '''Base class for state-related exceptions.
    Accepts only one param which must be a list of strings.'''
    def __init__(self, message=[]):
        if not isinstance(message, list):
            raise TypeError('{} takes a list of errors not {}'.format(
                self.__class__,
                type(message)
            ))
        super(_BaseStateError, self).__init__(message)

    def __str__(self):
        # There's only 1 arg, and it must be a list of messages.
        return u'\n'.join([_unicode_if(msg) for msg in self.args[0]])


class TransitionError(_BaseStateError):
    pass


class StateValidationError(_BaseStateError):
    pass


class BasicValidationError(BaseException):
    def __init__(self, message=''):
        super(BasicValidationError, self).__init__(message)
