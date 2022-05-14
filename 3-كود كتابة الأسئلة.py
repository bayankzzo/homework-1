import pickle
d={"1+1=":2,"1+3=":4,"2+7=":9,"1*10=":10,"100+2=":102,"10*10=":100,"52+3=":55,"22+22=":44}
outfile=open("p.txt","wb")
pickle.dump(d,outfile)
outfile.close()