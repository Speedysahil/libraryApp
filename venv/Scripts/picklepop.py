import pickle


file = "my_file.pkl"
load = open(file,"rb")
my_file=pickle.load(load)
print(type(my_file))

