# given_list = [5, 4, 4, 3, 1, -2, -3, -5]

# total3 = 0
# i = 0
# while given_list[i] > 0:
#     total3 += given_list[i]
#     i += 1
#     print (i)
# print (i)
exam_scores = [62, 50, 63, 54, 39, 49, 50, 43, 56, 62, 64, 58]
for score in exam_scores:
    score += 23
    if score >= 70:
        print("Excellent")
    elif score >= 60:
        print("Good")
    elif score >= 50:
        print("Pass")
    else:
        print("Fail")

    
        
