'''
    import module or from module import function
    (both case python will run complete module in seperate env)
    
'''
x = 42

def spam():
    print('x is : ',x)

def run():
    print('calling spam')
    spam()

if __name__ == '__main__':
    print('running')
    run()