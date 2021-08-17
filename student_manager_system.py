import student


class StudentManagerSystem(object):  # 学生管理系统类

    def __init__(self):
        self.stu_dicts = {}  # 创建字典收集学生信息

    @staticmethod
    def show_menu():  # 学生显示菜单
        print("1、添加学生")
        print('2、删除学生')
        print('3、修改学生')
        print('4、查询单个学生信息')
        print('5、查询所有学生信息')
        print('6、退出系统')

    def insert_student(self):  # 添加学生封装
        stu_id = input('请输入学生号：')

        if stu_id in self.stu_dicts:  # 判断学生学号是否存在 key
            print("学生学号已经存在，不能添加")
            return
        name = input('请输入学生的名字：')
        age = input('请输入学生的年龄：')
        gender = input('请输入学生性别：')

        stu = student.Student(stu_id, name, age, gender)  # 放入字典

        self.stu_dicts[stu_id] = stu  # 将学生对象放入字典的 key = 数据值
        print('恭喜添加学生信息成功！')

    def show_all_info(self):  # 查看学生信息
        print('所有学生信息如下：')
        print('--' * 10)
        for stu in self.stu_dicts.values():
            print(stu)

    def remove_student(self):  # 删除学生信息

        stu_id = input('请输入你要删除的学号：')
        if stu_id in self.stu_dicts:  # 判断学生学号信息是否存在
            del self.stu_dicts[stu_id]
            print('学生信息已经删除')
        else:
            print('学生信息存在，无法删除')

    def modify_student(self):  # 修改学生信息
        stu_id = input('请输入你要修改的学号：')
        if stu_id in self.stu_dicts:  # 判断学生学号信息是否存在

            stu = self.stu_dicts[stu_id]  # 字典中的key 是学号 value 是对象
            stu.age = input('请输入新的年龄：')
            stu.name = input('请输入新的学生名字：')
            stu.gender = input('请输入新的性别：')
            print("......学生信息已经修改完成....")
        else:
            print('学生信息不存在，无法修改不')

    def search_student(self):  # 查找学生信息
        stu_id = input('请输入你要查找的学号：')
        if stu_id in self.stu_dicts:  # 判断学生学号信息是否存在
            stu = self.stu_dicts[stu_id]
            print('查找的信息如下：')
            print(stu)

        else:
            print('学生信息不存在，无法修改不')

    def save(self):  # 保存学生信息到文件
        f = open('student.txt', 'w', encoding='utf-8')
        for stu in self.stu_dicts.values():
            f.write(str(stu) + "\n")  # stu会调用类__tr__
            f.close()

    def load_file(self):  # 读取文件
        f = open("student.txt", 'r', encoding='utf-8')
        buf_list = f.readlines()
        for buf in buf_list:
            buf = buf.strip()  # 去除\n
            info_list = buf.split(',')  # 用逗号切割
            stu = student.Student(*info_list)  # 列表信息拆包 得到每个数据
            # 讲对象添加到字典
            stu_id = info_list[0]
            self.stu_dicts[stu_id] = stu
        f.close()

    def start(self):
        self.load_file()  # 先读取文件方便下次使用
        while True:
            self.show_menu()

            opt = input('请输入你的选择：')
            if opt == '1':
                self.insert_student()

            elif opt == '2':
                self.remove_stu()
            elif opt == '3':
                self.modify_student()
            elif opt == '4':
                self.search_student()
            elif opt == '5':
                self.show_all_info()
            elif opt == '6':
                print('。。。。。欢迎下次使用学生管理系统。。。。。')
                self.save()  # 退出系统保存学生信息到文件
                break
            else:
                print('输入有误，请重新输入......')
                continue

            input('........回车键继续操作.......')
