# TODO: Tutorial I'm following: https://morioh.com/p/1d2afc550822
# Required imports
import os



config_name = os.getenv('APP_SETTINGS')
app = create_app(config_name)

if __name__ == '__main__':
    app.run()
