from enum import Enum
import json

class Status(Enum):
    CREATED = 1
    VALIDATED = 2
    VOTING = 3
    EXPIRED = 4
    FINALIZED = 5
    
class Expiration(Enum):
    AMOUNT = 1
    DURATION = 2
    AMOUNT_FOR_DURATION = 3
    AMOUNT_OR_DURATION = 4
    AMOUNT_AND_DURATION = 4
    
class Option:
    def __init__(self, body, amount=0, tally=0):
        self.body = body
        self.amount = amount
        self.tally = tally
        
class Question:
    def __init__(self, body, options, num_answers_min, num_answers_max, isFreeResponse=False):
        self.body = body
        self.options = options
        self.num_answers_min = num_answers_min
        self.num_answers_max = num_answers_max
        self.isFreeResponse = isFreeResponse
        
class Form:
    def __init__(self, form_id, questions, block_begin, block_end, amount_req, expiration):
        self.form_id = form_id
        self.questions = questions
        self.block_begin = block_begin
        self.block_end = block_end
        self.amount_req = amount_req
        self.status = Status.CREATED
        self.expiration = Expiration(expiration)
        self.responses = {}
        
    def updateStatus(self, status):
        self.status = status
        
    def addResponse(self, response):
        self.responses[response.tx_id]=response
        choices = json.loads(response.msg)[self.form_id]
        for i in range(len(self.questions)):
            for c in choices[i]:
                if not self.questions[i].isFreeResponse:
                    self.questions[i].options[c-1].amount+=response.amount
                    self.questions[i].options[c-1].tally+=1
                else:
                    if c in self.questions[i].options:
                        self.questions[i].options[c].amount+=response.amount
                        self.questions[i].options[c].tally+=1
                    else:
                        op = Option(c)
                        op.amount += response.amount
                        op.tally+=1
                        self.questions[i].options[c] = op
                        
                        
                
    def getResponse(self, tx_id):
        return self.responses[tx_id]
        
    def __str__(self):
     return self.form_id+" " +str(len(self.responses))+ " "+ str(self.status)
    
    def finalize(self):
        return None
        
