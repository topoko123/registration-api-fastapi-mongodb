import os
import sys


class ModuleManager:
    def createFolder(self, path):
        try:
            os.mkdir(path)
        except OSError as err:
            print('Folder already exists')
            raise err

    def createFiles(self, path):
        try:
            f = open(f'{path}/__init__.py', 'w')
            f.close()
            f = open(f'{path}/controller.py', 'w')
            f.close()
            f = open(f'{path}/routes.py', 'w')
            f.close()
            f = open(f'{path}/services.py', 'w')
            f.close()
            f = open(f'{path}/models.py', 'w')
            f.close()
        except Exception as err:
            print('Failed to create the files')
            raise err

    def generateModule(self, name):

        path = f'{os.getcwd()}/app/{name}'
        try:
            self.createFolder(path)
            self.createFiles(path)
        except OSError:
            print("Creation of the module %s failed" % name)
        else:
            print("Successfully created the module %s " % name)


def module():
    module_manager = ModuleManager()
    module_manager.generateModule(sys.argv[2])


manager = {
    "module": module
}

manager[sys.argv[1]]()