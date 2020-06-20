def average_scores(*args, **kwargs):
    """
    :param args: for arbitrary input for score
    :param kwargs: for arbitrary keyword
    :return: string with current average
    """
    number_tests = len(args)
    score_total = 0
    for x in args:
        score_total += x
    average = score_total/number_tests
    #use *args for average calculation
    for key, value in kwargs.items():
        print("%s = %s" % (key, value), end= ' ')
    #return a string like:
    #result: name = M gpa = 3.2 course = Python with current average 30.0
    print(f'with current average {average:.2f}')

if __name__ == '__main__':
    print(average_scores(48,93,37,92, first_name='Rachel', last_name='Ruse', course='Python'))
    print(average_scores(90,45,67,83, first_name='Mike', last_name='James', course='Math'))
    print(average_scores(90, 98, 59, 78, first_name='Nick', last_name='Fox', course='English'))

#output
#result: name = M gpa = 3.2 course = Python with current average 30.0
