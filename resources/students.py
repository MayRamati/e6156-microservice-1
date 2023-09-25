import json
from pydantic import BaseModel
from typing import List

class StudentModel(BaseModel):
    uni: str
    first_name: str
    last_name: str
    school: str

class StudentsResource:
    #
    # This code is just to get us started.
    # It is also pretty sloppy code.
    #

    students_file = \
        "resources/old-students.json"
    def __init__(self,file_name):
        self.students_file = file_name
        self.students = None

        with open(self.students_file, "r") as j_file:
            self.students = json.load(j_file)

    def get_students(self, last_name=None, school=None) -> List[StudentModel]:
        result = []
        for s in self.students:
            if last_name == s['last_name']:
                result.append(s)
        return result
