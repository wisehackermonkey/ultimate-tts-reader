# update app script
# allows for updating the app to the latest version
# by oran collins
# github.com/wisehackermonkey
# oranbusiness@gmail.com
# 20200526



import logging

logging.basicConfig(level=logging.DEBUG)

# location of server address, app version number
from client_config import ClientConfig

from pyupdater.client import Client, AppUpdate, LibUpdate


# goes to webserver grabs newest version of app and
# replaces the exe with the new one
def check_for_update():
    client = Client(ClientConfig(), refresh=True)
    app_update = client.update_check(ClientConfig.APP_NAME, ClientConfig.APP_VERSION)

    if app_update is not None:  # is there a new update
        if app_update.download():  # the update download is made here
            if isinstance(app_update, AppUpdate):  # you should freeze it
                app_update.extract_restart()
                return True
            else:
                app_update.extract()
                return True
    return False