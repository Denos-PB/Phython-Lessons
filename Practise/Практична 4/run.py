from FullTimeStudent import FullTimeStudent

st1 = FullTimeStudent("John", 20, 100, 5, 80, 90)
st2 = FullTimeStudent("Clara", 21, 90, 3, 50, 60)
st3 = FullTimeStudent("Java", 20, 80, 2, 30, 80)
st4 = FullTimeStudent("Python", 21, 70, 1, 20, 70)

print("Student 1 ")
print("Name: ", st1.name)
print("Age: ", st1.age)
print("Average Practice Score: ", st1.avg_practise_score())
print("Score: ", st1.total_score())

print("\n-----------------------------------\n")

print("Student 2 ")
print("Name: ", st2.name)
print("Age: ", st2.age)
print("Average Practise Score: ", st2.avg_practise_score())
print("Score: ", st2.total_score())

print("\n-----------------------------------\n")

print("Student 3")
print("Name: ", st3.name)
print("Age: ", st3.age)
print("Average Practise Score: ", st3.avg_practise_score())
print("Score: ", st3.total_score())

print("\n-----------------------------------\n")

print("Student 4")
print("Name: ", st4.name)
print("Age: ", st4.age)
print("Average Practise Score: ", st4.avg_practise_score())
print("Score: ", st4.total_score())

print("End of the program")

