import pickle
try:
    with open('sample_pickle.dat','rb') as f:
        n = pickle.load(f)
        print(n)
        for i in range(n):
            x = pickle.load(f)
            print(x)
        f.close()
except EOFError:
    print()


