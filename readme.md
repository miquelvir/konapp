konapp

(console -> Konsole) + app

A microframework for clear and ordered console applications. Inspired by Flask.

I found out that some times i needed to create console applications (not even CLI apps, but be able to run and access 
different functionalities when running a Python script directly). I thought that having a microframework like Flask
to manage the different endpoints, use blueprints and take care of the app's main loop would be great. Konapp package 
also implements storing context variables in the same app object, which makes it quite useful and clean for applications
with +1 module (without passing around a large amount of variables from level to level).

If you have worked with Flask, it will be trivial to get started, but check out the hello_world.py for an example! 