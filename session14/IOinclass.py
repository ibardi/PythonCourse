try:
    fin = open('bad_file')
except:
    print("Sommething went wrong.")

import pickle
t = [1,2,3]
print(pickle.dumps(t))

