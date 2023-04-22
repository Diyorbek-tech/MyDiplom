import json

file = open('Morfologik_buttons.json', encoding='utf8')
data = json.load(file)
data2 = data
print(data)


a = "data=data2"
S=[]


def steps(s):
    global a,S
    S.append(s)
    a += f'["{s}"]'
    return a
def remstep():
    global a,S
    b=a.split(f"[{S[-1]}]")
    print(a.split(f"[{S[-1]}]"))
    a=b[0]
    print(a)
    return a

while True:
    n = input(">>:")
    if n == "exit":
        exec(remstep())
        print(data)
    else:
        if n in data.keys():
            if isinstance(data[n], str):
                print(data[n])
                break
            else:
                data = data[n]
                print(data)
            print(steps(n))

        else:
            print("bu key yoq")

