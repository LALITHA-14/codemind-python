# cook your dish here
t = int(input())
for i in range(t):
    n,x,p = map(int,input().split())
    correct_questions  = x * 3
    incorrect = n - x
    incorrect_questions = (-1)*incorrect
    total_marks = correct_questions + incorrect_questions
    if(total_marks>=p):
        print("PASS")
    else:
        print("FAIL")
