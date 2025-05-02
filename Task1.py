try :
    f1 = open('sample.txt', 'r')
    op = f1.read()
    print(op)
    f1.close()
except FileNotFoundError:
    print("Sorry! 'Sample.txt' was not found.")
