students={
    'Lalit':{'score':90,'age':19},
    'Mohit':{'score':80,'age':20}
    }
print(max(students,key=lambda i:students[i]['score']))
