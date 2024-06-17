class Student:
    school="AkiraChix"
    def __init__(self,first_name,    last_name,age,country,code):
     self.first_name = first_name
     self.last_name=last_name
     self.age=age
     self.country=country
     self.code=code
    def greet_student(self):
        greeting =f" Hello {self.first_name} welcome to {self.school}. Your code is {self.code}"
        return greeting
    def full_name(self):
       return f"Hello your full names are {self.first_name} {self.last_name}"
    def check_if_minor(self):
       if self.age <18:
          return f"Hello you are a minor."
       else:
          return f"Hello,you are not a minor."
    def show_initials(self):
        full_name_parts = self.full_name().split()
        initials = ''.join([part[0].upper() + '.' for part in full_name_parts[:-1]])
        initials += ' ' + full_name_parts[-1].title()
        return initials
    def enroll_in_course(self, course):
        course.add_student(self)
        return f"{self.full_name()} has been enrolled in {course.name}"