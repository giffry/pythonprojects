class Ide:
    def functionalities(self):
        funcs=["create_file","rename","delete"]
        return funcs

class Pycharm(Ide):
    def functionalities(self):
        funcs=super().functionalities()
        funcs.append("debug")
        funcs.append("execute")
        return funcs

class Vscode(Ide):
    def functionalities(self):
        funcs=super().functionalities()
        funcs.append("vcs")
        funcs.append("formatting")
        return funcs

py=Pycharm()
print(py.functionalities())

vs=Vscode()
print(vs.functionalities())




