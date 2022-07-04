# def dec_fn(fn):
#
#     def inner_fn(n1,n2):
#         if n2>n1:
#             (n1,n2)=(n2,n1)
#         return fn(n1,n2)
#     return inner_fn
# @dec_fn
# def sub(n1,n2):
#     return n1-n2
# @dec_fn
# def div(n1,n2):
#     return n1/n2
#
# print(sub(10,20))

def admin_permission_required(fn):
    def inner_fn(*args, **kwargs):
        user = kwargs.get("user")
        if user.role != "admin":
            raise Exception("permission denied")
        else:
            return fn(*args, **kwargs)

    return inner_fn


class User:
    def set_user(self, username, role):
        self.username = username
        self.role = role

    def print_details(self):
        print(self.username, self.role)


class Addcourse:
    @admin_permission_required
    def set_course(self, *args, **kwargs):
        self.user = kwargs.get("user")
        self.course_name = kwargs.get("course_name")

    def print_details(self):
        print(self.course_name)


class Addbatch:
    @admin_permission_required
    def set_batch(self, *args, **kwargs):
        self.user = kwargs.get("user")
        self.batch_code = kwargs.get("batch_code")

        self.course = kwargs.get("course")

    def print_details(self):
        print(self.batch_code)


user = User()
user.set_user("rahul", "admin")

course = Addcourse()
course.set_course(user=user, course_name="django")

batch = Addbatch()
batch.set_batch(user=user, batch_code="aprdj2022", course=course)

course.print_details()
batch.print_details()
