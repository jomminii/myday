# -*- coding: utf-8 -*-

from flask import Flask
from flask_cors import CORS

from schedule.schedule_view import ScheduleView

def create_app():
    """

    Returns:
        생성된 플라스크 앱 객체
    Authors:


    """

    app = Flask(__name__)
    CORS(app, resources={r"/*/*": {"origins": "*"}})
    app.register_blueprint(ScheduleView.schedule_app)
    app.config['DEBUG'] = True
    return app
