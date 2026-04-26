def my_funtion(fname,lname):
    print("hello",fname,lname)

person = {'fname':'mohammed',
          'lname':'salah'}
my_funtion(**person)