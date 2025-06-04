max_students = 50
#método SEND, podemos enviar informações para dentro do gerador
def get_id_students():
    student_id = 1
    while max_students >= student_id:
        n = yield student_id
        if n is not None:
            student_id = n
            continue
        student_id += 1

students = get_id_students()
for id in students:
    #if id == 1:
        #id = students.send(25)
    if id <= 15: #Método throw
        print(id)
    else:
        #students.throw(ValueError, 'Invalid student ID')
        students.close()

