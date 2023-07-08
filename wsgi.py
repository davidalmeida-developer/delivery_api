from settings import app


import src.controller.ping_controlller
import src.controller.user_controller
import src.controller.order_controller



if __name__ == '__main__':

    app.run('0.0.0.0', debug=False)