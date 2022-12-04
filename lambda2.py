# convert upper into lower and viceversa
# decorators is used to make changes in a fn using another fn

# list2=["a","B","C","D","e","f"]


# if list2[i].isupper:


def div(a,b):
    print(a/b)

def good_div(fn):
    def inner_div(a,b):
        if a<b:
            a,b=b,a
        return fn(a,b)
    return inner_div

div=good_div(div)   
div(2,4)
div(3,4)     
   



