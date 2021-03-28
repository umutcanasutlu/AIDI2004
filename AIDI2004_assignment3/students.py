from settings import *
import json
import datetime

db = SQLAlchemy(app)

class Student(db.Model):
    __tablename__ = 'students'  
    id = db.Column(db.Integer, primary_key=True)  #primary key
    fname = db.Column(db.String(20), nullable=False)
    lname = db.Column(db.String(20), nullable=False)
    dob = db.Column(db.String(10), nullable=False)
    amountdue = db.Column(db.Integer, nullable=False)

    #turning student instance into json fo view
    def json(self):
        return {'id': self.id, 'fname': self.fname,
               'lname': self.lname, 'dob': self.dob, 'amountdue': self.amountdue}

    def add_student(_id, _fname, _lname, _dob, _amountdue):
            #adding students
            # creating an instance of student
            new_student = Student(id=_id, fname=_fname, lname=_lname, dob=_dob, amountdue=_amountdue)
            db.session.add(new_student) 
            db.session.commit()

    def get_all_students():
            #return all students in db
            return [Student.json(student) for student in Student.query.all()]

    def get_student(_id):
            #return student by id match
            return [Student.json(Student.query.filter_by(id=_id).first())]

    def update_student(_id, _fname, _lname, _dob, _amountdue):
            #find the student by id and update its values
            studentupdate = Student.query.filter_by(id=_id).first()
            studentupdate.fname = _fname
            studentupdate.lname = _lname
            studentupdate.dob = _dob
            studentupdate.amountdue = _amountdue
            db.session.commit()

    def delete_student(_id):
            #find student by id and delete
            Student.query.filter_by(id=_id).delete()
            db.session.commit() 
