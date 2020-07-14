def printanswer(questionlist):
    question = questionlist.pop(0)
    print(str(a + 1) + "." + str(question))
    return questionlist


def checkanswer(questionlist2, answerlist):
    question = questionlist2.pop(0)
    answer = answerlist.pop(0)
    if answer == question:
        print("correct")
    else:
        print("incorrect")
    return questionlist2, answerlist


questiontarget = ['bear', 'python3.6', 'peacock', 'kangaroo', 'whale', 'platypus']
questionlist = [questiontarget[1], questiontarget[3-1], questiontarget[1-1], questiontarget[3], questiontarget[5-1],
                questiontarget[2], questiontarget[6-1], questiontarget[4]]
questionlist2 = [questiontarget[1], questiontarget[3-1], questiontarget[1-1], questiontarget[3], questiontarget[5-1],
                questiontarget[2], questiontarget[6-1], questiontarget[4]]
answerlist = ['python3.6', 'peacock', 'bear', 'kangaroo', 'whale', 'peacock', 'platypus', 'whale']
for a in range(0, len(questionlist)):
    printanswer(questionlist)
    checkanswer(questionlist2, answerlist)
    print()