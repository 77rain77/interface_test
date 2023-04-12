# print(sum([x for x in range(101)]))
# print(sum(list(range(1,101))))
def name(self):
    def func():
        res = "JK"
        print(res)
    return func

@name
def run():     # run = name(run)
    print(9)

if __name__ == '__main__':
    run()