students={
    "harish":70,
    "Elen":91,
    "found":22,
    "bond":74,
    "starwin":58,
    "Flash":78
}
for grade in students:
    num=students[grade]
    if num > 90:
        students[grade]= "Outstanding"
    elif num >= 81:
        students[grade]="Exceeds Expections"
    elif num >=71:
        students[grade]= "Acceptable"
    else:
        students[grade]= "Fail"

print(students)