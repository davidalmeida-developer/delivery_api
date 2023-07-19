from settings import app


import controller.ping_controlller
import controller.user_controller
import controller.order_controller
import controller.customer_controller


if __name__ == '__main__':

    app.run('0.0.0.0', debug=False)
