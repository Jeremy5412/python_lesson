# def hello():
#     print("hello, python")
#     hello()

def hello(cnt):
    if cnt == 0:
        return
    print("Hello python",cnt)
    cnt -= 1
    hello(cnt)

hello(993)