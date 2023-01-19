from flask import jsonify


def error_http(status):
    return jsonify({
        'error': status.phrase,
        'description': status.description
    }), status.value
