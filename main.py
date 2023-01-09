from fastapi import FastAPI
import db
import models
app = FastAPI()


@app.get("/")
def home():
    return {"data":"Welcome"}

@app.get("/all")
def get_all():
    data = db.all()
    return {"data":data}

@app.post("/create")
def post_data(data:models.Todo):
    print(data)
    id = db.create(data)
    return {"id" : str(id)}

@app.get("/data/{data}")
def get_data(data:str):
    response = db.get_one(data)
    return {"response":"Done","data":response}

@app.put("/update")
def update_data(data:models.Todo):
    response = db.update()