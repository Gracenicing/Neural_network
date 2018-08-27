import pickle

# a_dict = {'tg':1,'gui':2}
# file = open('pickle.explame','wb')
# pickle.dump(a_dict,file)
# file.close()

# file = open('pickle.explame','rb')
# a_dict1 = pickle.load(file)
# file.close()
# print(a_dict1)

with open('pickle.explame','rb') as tf:
	a_dict1 = pickle.load(tf)
print(a_dict1)