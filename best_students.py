# By Kamran Bigdely Nov. 2020
# Replace temp variable with query

# TODO: Use 'extract method' refactoring technique to improve this code.
# TODO: If required, use 'replace temp variable with query' technique to make it easier to extract methods.

class Employer:
  def __init__(self, name):
    self.name = name

  def send(self, students):
    print("Students' contact info were sent to", self.name + '.')


class Student:
  def __init__(self, gpa, name):
    self.gpa = gpa
    self.name = name

  def get_gpa(self):
    return self.gpa

  def send_congrat_email(self):
    print("Congrats", self.name + ". You graduated successfully!")


class School:
  def __init__(self, students) -> None:
    self.students = students
    self.min_gpa = 2.5
    self.employers = [Employer('Microsoft'), Employer(
      'Free Software Foundation'), Employer('Google')]

  def print_students(self, students, header):
    for s in students:
      print(s.name)

  def passing_students(self):
    passed_students = []
    for s in self.students:
      if s.get_gpa() > self.min_gpa:
        passed_students.append(s)

    return passed_students

  def top_students(self, students):
    students.sort(key=lambda s: s.get_gpa())
    percentile = 0.9
    index = int(percentile * len(students))
    top_10_percent = students[index:]

    return top_10_percent

  def process_graduation(self):
    passed_students = self.passing_students()

    self.print_students(passed_students, "*** Students who graduated ***")

    for s in passed_students:
      s.send_congrat_email()

    top_10_percent = self.top_students(passed_students)
    for e in self.employers:
      e.send(top_10_percent)


students = [Student(2.1, 'donald'), Student(2.3, 'william'), Student(2.7, 'toro'),
            Student(3.9, 'lili'), Student(3.2, 'kami'), Student(3, 'sarah')]

school = School(students)
school.process_graduation()
