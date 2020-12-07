import pickle

def add(form):
    pickle.dump(form, open("forms/"+form.form_id+".p", "wb+" ))
    
def get(form_id):
    form = pickle.load( open("forms/"+form_id+".p", "rb" ))
    return form
    
def update(form):
    pickle.dump(form, open("forms/"+form.form_id+".p", "wb+" ))



