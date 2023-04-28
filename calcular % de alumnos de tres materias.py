materia1=int(input("ingrese cantidad de alumnos materia#1:"))
materia2=int(input("ingrese cantidad de alumnos materia#2:"))
materia3=int(input("ingrese cantidad de alumnos materia#3:"))
total_alumnos=materia1+materia2+materia3
porcentaje_materia1=materia1/total_alumnos*100
porcentaje_materia2=materia2/total_alumnos*100
porcentaje_materia3=materia3/total_alumnos*100
print(f"el porcentaje de la materia 1 es:{porcentaje_materia1}%")
print(f"el porcentaje de la materia 2 es:{porcentaje_materia2}%")
print(f"el porcentaje de la materia 3 es:{porcentaje_materia3}%")