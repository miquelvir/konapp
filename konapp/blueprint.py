"""
    konapp.blueprint
    ~~~~~~~~~

    This module implements the Konapp Blueprint object (an aggregated and reusable set of paths).
"""


from .endpoints import _EndpointManagerObject


class Blueprint(_EndpointManagerObject):
    """ stores endpoints for conglomerated use in an app """

    def __init__(self):
        """ initialise the blueprint """

        super().__init__()
