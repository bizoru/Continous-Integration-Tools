from fabric.api import local,settings
from fabric.colors import cyan

def hello():
  print(cyan('Testing Python Fabric',True))
  local('uname -a')
  with settings(warn_only=True):
    result = local('git status',capture=True)
    print(result)
    if result.failed:
      result  = local('git init')
      print(result)
      print('Initializing Empty Git Repo')
