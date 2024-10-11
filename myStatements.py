my_list = ["apple","cherry",'lemon']
my_dict = {'drink': 'coffee', 'milk': 'whole'}

for item in my_list:
    print(f'my list: {item}')
    
for _,value in my_dict.items():
    print(f'my favorite {_} is: {value}')