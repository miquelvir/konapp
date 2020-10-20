from konapp import Blueprint, App

# initialise the console app
bugs = Blueprint()


# now add some endpoints to the blueprints

@bugs.endpoint('/new')  # this is the main endpoint
def new(**_):
    print("adding new bug...")


@bugs.endpoint('/solve')
def solve(**_):
    print("solving...")

