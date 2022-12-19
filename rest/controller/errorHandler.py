from flask import jsonify

from rest import jwt


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({"status": "KO", "error": "token_expired", "message": "The token has expired."}), 401


@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({"status": "KO", "error": "invalid_token", "message": "Signature verification failed."}), 401


@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({"status": "KO", "error": "authorization_required",
                    "message": "Request does not contain an access token."}), 401
