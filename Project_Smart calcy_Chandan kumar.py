import speech_recognition as sr
import webbrowser as wb

r1=sr.Recognizer()

responses=["Welcome to smart calculator","My name is Chandan kumar","Thank you","Sorry,This is after my ability"]
def Extract_num_from_text(text):
    l=[]
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return(l)
def lcm(a,b):
    L=a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L
        L+=1
def fact(a):
    ans=1
    while(a>1):
        ans=ans*(a)
        a=a-1
    return ans
def hcf(a,b):
    H=a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H
        H-=1
def big(a,b):
    return a if a>b else b
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return a/b
def mod(a,b):
    return a%b
def end():
    print(responses[2])
    input("Press enter key to Exit")
    exit()
def myname():
    print(responses[1])
def sorry():
    print(responses[3])
def help():
    print("List of valid command are :-")
    for k in operations:
        print(k)
    for k in commands:
        print(k)
operations={"PLUS":add,"ADD":add,"ADDITION":add,"SUM":add,"FACTORIAL":fact,"MINUS":sub,"SUBTRACTION":sub,"DIFFERENCE":sub,"PRODUCT":multiply,"MULTIPLICATION":multiply,"MULTIPLY":multiply,"DIVIDE":division,"DIVISION":division,"LCM":lcm,"HCF":hcf,"BIG":big,"MAX":big,"GREATER":big,"MOD":mod,"MODULAS":mod}
commands={"NAME":myname,"END":end,"EXIT":end,"CLOSE":end,"HELP":help}
print(responses[0])
print(responses[1])
    
while True:
    with sr.Microphone() as source:
        print('Speak your quary...')
        audio = r1.listen(source)
        try:
            text = r1.recognize_google(audio)
            print('you said : {}'.format(text))
        except:
            print('Sorry we could not recognize your voice')
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l=Extract_num_from_text(text)
                if len(l)==1:
                    r = operations[word.upper()](l[0])
                else:
                    r = operations[word.upper()](l[0], l[1])
                print(r)
            except:
                print("Something is wrong!!please Retry")
            finally:
                break
        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break
    else:
        sorry()

