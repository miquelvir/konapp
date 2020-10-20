from konapp import App

from hello_world_bugs import bugs

# initialise the console app
app = App(title="hello world")

# register some blueprints
app.register_blueprint(bugs, prefix='/bugs')


# now add some endpoints to the app

@app.endpoint('/')  # this is the main endpoint
def main_menu(ctx: App = None):
    print("This is the main menu. Choose what to do.")
    print("1. Notify a bug")
    print("2. Mark a bug as solved")
    print("3. Cry")
    print("4. Stop")
    choice = int(input("> "))  # use a Menu object instead for solid Menus; still not uploaded in public

    if choice == 1:
        ctx.run_step('/bugs/new')
    elif choice == 2:
        ctx.run_step('/bugs/solve')
    elif choice == 3:
        ctx.run_step('/cry')
    else:
        ctx.stop()


@app.endpoint('/cry')
def view_default_shipment(ctx: App = None):
    ctx["how-to-cry"] = "crying a lot"  # we can store objects to the app contextx
    print("crying...")
    print(ctx["how-to-cry"])  # and retrieve them, even between different endpoints


if __name__ == "__main__":
    app.run()  # start the console app
