"""
    konapp.endpoints
    ~~~~~~~~~

    This module implements the basic object to support adding and storing endpoints.
"""
from typing import Callable


class _EndpointManagerObject:
    """ basic object to store endpoints using the endpoint decorator """

    def __init__(self):
        """ initialise the app; optionally with a title to display in the command line """

        self._endpoints = {}  # store the bindings between routes and functions to run

    def endpoint(self, route: str):
        """
        decorator; assigns the given route endpoint to the step the function contains

        all functions must accept as kwarg named ctx the app context
        """

        def decorator(f):
            self._add_endpoint(route, f)   # assign route to step contained in function
            return f

        return decorator

    def _add_endpoint(self, route: str, callable_: Callable):
        if route in self._endpoints:
            raise KeyError("route '%s' is already assigned to '%s'" % (route, self._endpoints[route]))

        self._endpoints[route] = callable_  # assign route to the callable

    @property
    def endpoints(self):
        """ exposes the endpoints getter """
        return self._endpoints
