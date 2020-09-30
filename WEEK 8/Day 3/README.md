# Developers_Institute W8 and D3

What can we do with a Model.
2 Ways to save new data:
------------------------
s = Student(first_name="blah", last_name="flah")   #Create New
s.save()
s = Student.objects.create(first_name="blah", last_name="flah")
3 Ways to fetch data:
---------------------
students = Student.objects.all()
student = Student.objects.get(first_name = "Charlie")
students = Student.objects.filter(first_name = "Charlie")
Other filters:
--------------
first_name__contains="a"
first_name__startswith="A"
first_name__endswith="e"


And you can do this all in the shell:
python manage.py shell
from student.models import Student, Pet