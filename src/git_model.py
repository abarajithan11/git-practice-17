tree = ['src/*.py']

commit_1 = {
  'message': "Add initial files",
  'parents' : [], # list of commits
  'author' : 'aba: abarajithan07@gmail.com',
  'snapshot': tree
}

def add (a, b):
  return a+b

def multiply (a,b):
  return a*b

def divide (a,b):
  return a/b

if __name__ == '__main__':
  print("The commit is: ", "commit_1")
  print(add(2,3))
  print(multiply(2,3))
  print(divide(2,3))

