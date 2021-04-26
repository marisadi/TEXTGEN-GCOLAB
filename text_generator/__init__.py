#The __init__.py serves double duty: 
# it will contain the application factory, 
# and it tells Python that the flaskr directory 
# should be treated as a package.
# ---------------------------------------------
# Before this make sure requirements have been installed in PRODUCTION
# ($ pip3 install flask python-dotenv)
# ---------------------------------------------
from flask import Flask
# import our generator
from .routes import generator
# define create app function to create out app
# def create_app(config_file='settings.py'):
# name of file running
app = Flask(__name__, static_url_path="/tmp", static_folder="tmp")
#        app.config.from_pyfile(config_file)

        # Register Blueprint - In routes we'll configure a blueprint which will make setup easier
app.register_blueprint(generator)
        # return the app we have configured
#        return app
#app.run()
#if __name__ == "__main__":
#    app.run(host='0.0.0.0')
