import json

lines=[]
while True:
    line=input()
    if line:
        lines.append(line)
    else:
        break
text=lines

def preprocessing(text):
    for i in text:
        i=json.loads(i)
        m=i['from']
        n=i['to']
        hasil=[]
        for a in range(m,n+1):
            if(a % 3==0)and a%5==0:
                res=i['fizz']+i['buzz']
            elif a%5==0:
                res=i['buzz']
            elif a%3==0 :
                res=i['fizz']
            else:
                res=a
            hasil.append(res)
        dictionary={i['id']:hasil}
        print(dictionary)

preprocessing(text)