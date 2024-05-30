from flask import jsonify


def register_error_handlers(app):
    @app.errorhandler(400)
    def bad_request_error(error):
        response = jsonify({"error": "Bad Request", "message": "The request could not be understood or was missing "
                                                               "required parameters."})
        response.status_code = 400
        return response

    @app.errorhandler(500)
    def internal_server_error(error):
        response = jsonify({"error": "Internal Server Error", "message": "An unexpected error has occurred."})
        response.status_code = 500
        return response
