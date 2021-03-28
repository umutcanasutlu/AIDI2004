from students import *

@app.route("/")
def welcomepage():
    return render_template("welcome.html")

@app.route('/allstudents', methods=['GET'])
def getAllstudents():
    '''Function to get all the movies in the database'''
    return jsonify({'Students': Student.get_all_students()})

@app.route('/getstudent',methods=['GET', 'POST'])
def get_student():
    return render_template("getstudent.html")

@app.route('/student', methods=['GET', 'POST'])
def getStudent():
    id = request.args.get('id')
    student = Student.get_student(id)
    flash(student[0])
    return render_template("getstudent.html")



@app.route('/newstudent', methods=['GET', 'POST'])
def new_student():
    return render_template("newstudent.html")

@app.route('/studentadded', methods=['GET', 'POST'])
def add_student():
    id = request.args.get('id')
    fname = request.args.get('fname')
    lname = request.args.get('lname')
    dob = request.args.get('dob')
    amountdue = request.args.get('amountdue')
    Student.add_student(id, fname, lname, dob, amountdue)
    flash('Student is added succesfully.')
    return render_template("newstudent.html")

@app.route('/updatestudent', methods=['GET', 'POST'])
def update_student():
    return render_template("updatestudent.html")

@app.route('/studentupdated', methods=['GET', 'POST', 'PUT'])
def studentUpdated():
    id = request.args.get('id')
    fname = request.args.get('fname')
    lname = request.args.get('lname')
    dob = request.args.get('dob')
    amountdue = request.args.get('amountdue')
    Student.update_student(id, fname, lname, dob, amountdue)
    flash('Student is updated succesfully.')
    return render_template("updatestudent.html")

# route to delete movie using the DELETE method
@app.route('/removestudent', methods=['GET', 'POST'])
def removeStudent():   
    return render_template("removestudent.html")

@app.route('/studentremoved', methods=['GET', 'POST', 'DELETE'])
def remove_student():   
    id = request.args.get('id')
    Student.delete_student(id)
    flash('Student is removed succesfully.')
    return render_template("removestudent.html")



if __name__ == "__main__":
    app.run(port=1234, debug=True)
