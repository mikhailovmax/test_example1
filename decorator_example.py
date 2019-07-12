import time


def timer(f):

    def tmp(*args, **kwargs):
        t = time.time()
        result = f(*args, **kwargs)
        print("Время работы функции: %f" % (time.time()-t))
        return result

    return tmp


@timer
def some_func():
    print("some text")

    
print(some_func()) 
