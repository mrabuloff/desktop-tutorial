Number_of_completed_task = float(12)
Text1 = "Всего задач:"
Text2 = "затрачено часов:"
Number_of_hours_spent = float(1.5)
Course_name='Python'
name = "Курс: " + Course_name
b=float(Number_of_hours_spent/Number_of_completed_task)
print(str(b))
Text3 = "среднее время выполнения "
Text4=" часа."
print(name, Text1, Number_of_completed_task,',', Text2,'', Number_of_hours_spent, Text3, str(b), Text4)
