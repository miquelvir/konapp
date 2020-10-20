"""
    konapp.app
    ~~~~~~~~~

    This module implements the central Konapp application object.
"""


from .printing_helpers import print_surrounded
from .endpoints import _EndpointManagerObject
from .context import _ContextDictObject
from .blueprint import Blueprint

_MAIN_PATH = '/'


class App(_EndpointManagerObject, _ContextDictObject):
    """ runs the step assigned to main path until stop is called """

    def __init__(self, title: str = None):
        """ initialise the app; optionally with a title to display in the command line """
        super().__init__()

        self._main_loop = False  # controls the main loop, start paused
        self._title = title  # custom title to display at the beginning

    def run(self):
        """
        starts the app running the function in the main path endpoint

        repeats in an endless cycle (until stop called)
        """

        # some endpoint needs to be assigned to the main path,
        if _MAIN_PATH not in self._endpoints:
            raise ValueError("no function assigned to the main path endpoint ('%s')" % _MAIN_PATH)

        if self._title:  # if title is given, print it before starting the app as header
            print_surrounded(self._title)

        # run infinitely (until stop is called) from the main path
        self._main_loop = True
        while self._main_loop:
            self.run_step(_MAIN_PATH)

    def stop(self):
        """ stops the app main loop, next iteration of the loop won't be executed """
        self._main_loop = False

    def run_step(self, route: str):
        """ given a route, execute the function associated to it """
        try:
            step = self._endpoints[route]
        except KeyError:
            raise KeyError("given route '%s' is not assigned to any step" % route)
        else:
            step(ctx=self)  # call passing context

    def register_blueprint(self, blueprint: Blueprint, prefix: str = None):
        """ adds all endpoints from a blueprint to the current app """
        for route, callable_ in blueprint.endpoints.items():
            # if prefix is passed, use it
            if prefix:
                route = prefix + route

            # add endpoint to current app
            self._add_endpoint(route, callable_)
