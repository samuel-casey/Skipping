# import random
# running_count = 0

# for i in range(50):
#     a = random.random()
#     if a > .5:
#         running_count+=1
#     else:
#         running_count-=1
#     print(running_count)
# print('Hey\nwhatsssssdasdasda')
# print('What\'s uaaaasasp')


a = {1:'a',2:'b',3:'c'}
b = {2:'p',3:'l',4:'d'}

print({random:a[random] for random in a if random in b})
