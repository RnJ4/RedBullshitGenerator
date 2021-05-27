import random

f=open('dict.txt')
shitDict=f.readlines()
f.close()

length=input("How long do you want?")
length=int(length)

output=""
i=0

while i < length:
	tmp=random.sample(shitDict,1)
	tmp=str(tmp).replace("['\n']","").replace("\n']","").replace("['","")
	tmp=tmp.replace("\\n\']","")
	output+=tmp+'\n'
	i+=len(str(tmp))

f=open("output.txt","w")
f.write(output)
f.close()
