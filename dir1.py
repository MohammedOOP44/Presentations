import array 

info = array.__dict__

for key , value in info.items():
    print(f"{key}  :  {value}")