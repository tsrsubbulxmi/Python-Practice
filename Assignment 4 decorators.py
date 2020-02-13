def joining(func):
    def inner():
        a=func()
        return ' '.join(a)    # returning the joined string
    return inner              #returning to calling function
def titlecase(func):
    def inner():
        t=func() 
        return t.title()      #returning the titlecase string 
    return inner              #returning to the calling function

@titlecase                    #second called with string input
@joining                      #first called with list input
def welcoming():
    return ['welcome','to','python']
print(welcoming())
