from app import app, db

@app.errorhandler(404)
def not_found_error(error):
    return {"message": "The endpoint you are trying to reach does not exist. Have you read the documentaion the API before calling it?"}, 200

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return "500", 500