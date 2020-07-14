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


questionlist = [True and True, False and True, 1 == 1 and 2 == 1, "test" == "test", 1 == 1 or 2 != 1, True and 1 == 1,
                False and 0 != 0, True or 1 == 1, "test" == "testing", 1 != 0 and 2 == 1, "test" != "testing", "test" == 1,
                not(True and False), not (1 == 1 and 0 != 1), not (10 == 1 or 1000 == 1), not(1 != 10 or 3 == 4), not("testing" == "testing" and "Zed" == "Cool Guy"),
                1 == 1 and (not ("testing" == 1 or 1 == 0)), "chunky" == "bacon" and (not (3 == 4 or 3 == 3)), 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))]
questionlist2 = [True and True, False and True, 1 == 1 and 2 == 1, "test" == "test", 1 == 1 or 2 != 1, True and 1 == 1,
                False and 0 != 0, True or 1 == 1, "test" == "testing", 1 != 0 and 2 == 1, "test" != "testing", "test" == 1,
                not(True and False), not (1 == 1 and 0 != 1), not (10 == 1 or 1000 == 1), not(1 != 10 or 3 == 4), not("testing" == "testing" and "Zed" == "Cool Guy"),
                1 == 1 and (not ("testing" == 1 or 1 == 0)), "chunky" == "bacon" and (not (3 == 4 or 3 == 3)), 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))]
answerlist = [True, False, False, True, True, True, False, True, False, False, True, False, True, False, True, False, True, True, False, False]
a = 0
for a in range(0, len(questionlist)):
    printanswer(questionlist)
    checkanswer(questionlist2, answerlist)
    print()

# 1.
# 2.
# 3.
# 4.
# 5.
# 6.
# 7.
# 8.
# 9.
# 10.
# 11.
# 12.
# 13.
# 14.
# 15.
# 16.
# 17.
# 18.
# 19.
# 20.