import pickle
infile=open("p.txt","rb")
d=pickle.load(infile)
infile.close()
count=0
user=input("enter username")
for i in d.keys():
    print(i)
    ans=int(input())
    if ans==d[i]:
        print('true')
        count+=1
print(count,"true")
outfile=open("tt.txt",'w')
outfile.write(f"""{user}
{count}
good job""")
outfile.close()