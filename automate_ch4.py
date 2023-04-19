# Write your code here :-)
def commatize(lissed):
    if len(lissed) > 1:
        n = 0
        while n < (len(lissed) - 2):
            print(lissed[n], end=', ')
            n = n + 1
        print(lissed[len(lissed) - 2], end='')
        print(" and", end=' ')
        print(lissed[len(lissed) - 1])
    elif len(lissed) == 1:
        print(lissed[0])
    else:
        print('oops, it\'s empty!')

lissed = ["But How Do It Know", "The Art of Writing Clean Code", "The Linux Command Line",\
          "Automate the Boring Stuff With Python", "Data Structures and Algorithms", "Job ready Java"]

commatize(lissed)


