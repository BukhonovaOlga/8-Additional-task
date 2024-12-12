grades = [[5,3,3,5,4], [2,2,2,3], [4,5,5,2], [4,4,3], [5,5,5,4,5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#students_list = list(students)
#print(students_list)

#print(students_list[0])
#print(students_list[1])
#print(students_list[2])
#print(students_list[3])
#print(students_list[4])

students_list = ['Aaron', 'Bilbo', 'Johnny', 'Khendrik', 'Steve']
print(students_list)

print(students_list[0])
print(students_list[1])
print(students_list[2])
print(students_list[3])
print(students_list[4])

Aaron_gr = grades[0]
Aaron_av_gr = (Aaron_gr[0] + Aaron_gr[1] + Aaron_gr[2] + Aaron_gr[3] + Aaron_gr[4]) / len(Aaron_gr)

Bilbo_gr = grades[1]
Bilbo_av_gr = (Bilbo_gr[0] + Bilbo_gr[1] + Bilbo_gr[2] + Bilbo_gr[3]) / len(Bilbo_gr)

Johnny_gr = grades[2]
Johnny_av_gr = (Johnny_gr[0] + Johnny_gr[1] + Johnny_gr[2] + Johnny_gr[3]) / len(Johnny_gr)

Khendrik_gr = grades[3]
Khendrik_av_gr = (Khendrik_gr[0] + Khendrik_gr[1] + Khendrik_gr[2]) / len(Khendrik_gr)

Steve_gr = grades[4]
Steve_av_gr = (Steve_gr[0] + Steve_gr[1] + Steve_gr[2] + Steve_gr[3] + Steve_gr[4]) / len(Steve_gr)

average_grades = {students_list[0] : Aaron_av_gr, students_list[1] : Bilbo_av_gr, students_list[2] : Johnny_av_gr,
                  students_list[3] : Khendrik_av_gr, students_list[4] : Steve_av_gr}

print(average_grades)