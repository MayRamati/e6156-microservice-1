from fastapi import FastAPI, Response
from typing import List
import uvicorn
from resources.students import StudentsResource, StudentModel

app = FastAPI()
students_resource = StudentsResource("./resources/students.json")

@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {
            "message": f"hello {name}",
            "Sender": "May Ramati"
            }


@app.get("/hello_text/{name}")
async def say_hello_text(name: str):
    the_message = f"Hello {name}"
    rsp = Response(content=the_message, media_type="text/plain")
    return rsp


@app.get("/students", response_model=List[StudentModel])
async def get_students(last_name: str = None):
    result = students_resource.get_students(last_name)
    return result

@app.post("/students")
async def get_students(s: StudentModel):
    result = students_resource.create_students(s)
    return None

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8011)
