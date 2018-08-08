import pickle

n = 7
i = 130000
a = 99.056
s = '中国人民123ksjdhfhu'
lst = [[1,2,4],2,[5,6,98]]
tu = (-4,54,6)
coll = {1,3,5}
dic = {'a':'apple','b':'banana','g':'grap'}
with open("sample_pickle.dat","wb") as f:
    try:
        pickle.dump(n,f)
        pickle.dump(i,f)
        pickle.dump(s,f)
        pickle.dump(lst,f)
        pickle.dump(tu,f)
        pickle.dump(coll,f)
        pickle.dump(dic,f)
    except:
        print("写入文件异常")
    finally:
        f.close()

