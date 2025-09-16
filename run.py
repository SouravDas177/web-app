from app import crate_app,db

from app.models import Task

app=crate_app()

with app.app_context():
    db.create_all()
    print("database created")

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)