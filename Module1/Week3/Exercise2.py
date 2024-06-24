from abc import ABC, abstractmethod

class Person (ABC):
    data = []
    def __init__(self, name, Yob):
        self._name = name
        self._Yob = Yob
        self.data.append(self)
    @abstractmethod
    def describe(self):
        pass

    def get_yob(self):
        return self._Yob

class Student(Person):
    def __init__(self, name, Yob, Grade):
        super().__init__(name = name, Yob = Yob)
        self.__grade = Grade
    
    def describe(self):
        print(f"Student - Name: {self._name} - Yob: {self._Yob} - Grade: {self.__grade}")

class Doctor(Person):
    def __init__(self, name, Yob, specialist):
        super().__init__(name = name, Yob = Yob)
        self.__specialist = specialist
    
    def describe(self):
        print(f"Doctor - Name: {self._name} - Yob: {self._Yob} - Specialist: {self.__specialist}")

class Teacher(Person):
    def __init__(self, name, Yob, Subject):
        super().__init__(name = name, Yob = Yob)
        self.__Subject = Subject
    
    def describe(self):
        print(f"Teacher - Name: {self._name} - Yob: {self._Yob} - Subject: {self.__Subject}")

class Ward:
    def __init__(self, name):
        self.__name = name
        self.__list_people = list()
    
    def add_person(self, person : Person):
        self.__list_people.append(person)

    def describe(self):
        print(f"Name: {self.__name}")
        for p in self.__list_people:
            p.describe()
    def count_doctor(self):
        total_doctor = 0
        for p in self.__list_people:
            if isinstance(p, Doctor):
                total_doctor += 1
        return total_doctor
    
    def sort_age(self):
        return self.__list_people.sort(key = lambda x: x.get_yob(), reverse= True)

    def compute_average(self):
        total = 0
        len_teacher = 0
        for p in self.__list_people:
            if isinstance (p , Teacher):
                total += p.get_yob()
                len_teacher += 1
        if len_teacher == 0:
            print("khoong cos giao vien")
        else:
            return total/len_teacher

ward1 = Ward("ward_1")
ward1.add_person(student1)
ward1.add_person(doctor2)
ward1.add_person(doctor3)
ward1.add_person(teacher1)
ward1.describe()
ward1.count_doctor()
ward1.sort_age()
ward1.compute_average()



student1 = Student("trong", 1999, 10)
student2 = Student("vy", 1999, 10)
student3 = Student("thi", 2004, 5)

teacher1 = Teacher("phuong", 1990, "maht")
teacher2 = Teacher("hieu", 1989, "pyshical")
teacher3 = Teacher("ngoc", 1988, "english")

Doctor1 = Doctor("tran", 1982, "surver")
doctor2 = Doctor("nguyen", 1983, "chilrend")
doctor3 = Doctor("ly", 1994, "lung")

