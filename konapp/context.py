"""
    konapp.context
    ~~~~~~~~~

    This module implements the basic object to support app context (adding and retrieving variables to the object dict itself).
"""


class _ContextDictObject:
    """ basic object to be able to store and retrieve variables from the inner dict

    mirrors the inner dict functionality as public interfaces of the App class;
    it allows the user to store and get values from the context of the app
    """

    def __contains__(self, key):
        return self.__dict__.__contains__(key)

    def __getitem__(self, key):
        """ get an item from the app object dict """
        return self.__dict__.__getitem__(key)

    def __setitem__(self, key, value):
        """ assign an item to a key in the app object dict """
        return self.__dict__.__setitem__(key, value)

    def __delitem__(self, key):
        """ deletes an item given a key from the app """
        return self.__dict__.__delitem__(key)
