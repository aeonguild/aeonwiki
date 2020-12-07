from Form import *
from Response import Response
import FormManager

def toHex(string):
    string = ''.join(hex(ord(x))[2:] for x in string)
    string = string.zfill(64)
    print(string)
    return string

question_1 = Question("Which is better: 1 or 0?",[Option("0"),Option("1")],1,1)
question_2 = Question("Which is best: 1, 3, or 2?",[Option("1"),Option("2"),Option("3")],1,1)
question_3 = Question("Who is your favorite superhero?",{},1,1,True)

form1 = Form("1",[question_1, question_2],1000,1100,0,Expiration.DURATION)
form4 = Form("4",[question_3],1000,1100,0,Expiration.DURATION)
form5 = Form("5",[question_3, question_2],1000,1100,0,Expiration.DURATION)

FormManager.add(form1)
FormManager.add(form4)
FormManager.add(form5)

form = FormManager.get(form1.form_id)
print(str(form))
form.updateStatus(Status.VOTING)
print(str(form))
response1 = Response("xxxxx_id","1",toHex('{"1":[[1],[2]]}'),100,2001)
response2 = Response("yyyyy_id","1",toHex('{"1":[[1],[1]]}'),200,2000)
form.addResponse(response1)
form.addResponse(response2)
print(str(form))
FormManager.update(form)


form = FormManager.get(form4.form_id)
print(str(form))
form.updateStatus(Status.VOTING)
print(str(form))
response1 = Response("xxx333xx_id","4",toHex('{"4":[["superman"]]}'),100,2001)
response2 = Response("yyy333yy_id","4",toHex('{"4":[["batman"]]}'),200,2000)
response3 = Response("y44433yy_id","4",toHex('{"4":[["superman"]]}'),600,2000)
form.addResponse(response1)
form.addResponse(response2)
form.addResponse(response3)
print(str(form))
FormManager.update(form)



form = FormManager.get(form5.form_id)
print(str(form))
form.updateStatus(Status.VOTING)
print(str(form))
response1 = Response("xxx333xx_id","5",toHex('{"5":[["superman"],[1]]}'),100,2001)
response2 = Response("yyy333yy_id","5",toHex('{"5":[["catwoman"],[2]]}'),200,2000)
response3 = Response("y44433yy_id","5",toHex('{"5":[["superman"],[3]]}'),600,2000)
form.addResponse(response1)
form.addResponse(response2)
form.addResponse(response3)
print(str(form))
FormManager.update(form)
