class hook_test:
    def __init__(self):
        self.aa=None

    def b(self,rice):
        self.aa=rice
        #print(self.aa())
        rice()
        print("年轻")

    def c(self):
        if self.aa is None:
            print("貌美")
        else:
            d()
            print(18)

def d():
    print("18")

if __name__ == '__main__':
    aaa=hook_test()
    aaa.b(d)
    aaa.c()
