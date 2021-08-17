class Student(object):  # 创建学生类
    def __init__(self, stu_id, name, age, gender):
        self.stu_id = stu_id   # 学号 是字典的key
        self.name = name   # 名字
        self.age = age   # 年龄
        self.gender = gender  # 性别

    def __str__(self):
        return f"{self.stu_id}, {self.name}, {self.age}, {self.gender}"


if __name__ == '__main__':
    stu = Student(1, 'aa', 18, 'n')
    print(stu)
