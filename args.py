def my_funtion(username,**details):
    print('username',username)
    print('age',details['age'])
    print('power',details['power'])
    print('hobby',details['hobby'])

my_funtion("Ali",age=30,power="hard",hobby="coding")
        
