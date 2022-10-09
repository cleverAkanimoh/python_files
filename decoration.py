def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def print_text():
    print("Crush world!")

print_text = decor(print_text)

print_text();

def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

@decor
def print_text():
    print("Hello world!")

print_text();

text=input("Enter text here: ")
def upper_decor(func):
    def wrap(text):
        return func(text).upper()
    return wrap

@upper_decor
def dis_text(text):
    return (text)

print(dis_text(text))