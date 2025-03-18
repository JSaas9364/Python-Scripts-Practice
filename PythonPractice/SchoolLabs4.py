def f1(f):
    def f2():
        print("before f2 call")
        f()
        print("after f2 call")
    return f2

@f1
def f3():
    print("f3")
    
f3()