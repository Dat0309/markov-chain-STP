import numpy as np
import random as rd

from numpy.core.numeric import count_nonzero

# the statespace
states = ["Không mua thường xuyên","Thỉnh thoảng mua","Mua thường xuyên"]

#Possible sequences of events
transitionName = [["KK","KT","KM"],["TK","TT","TM"],["MK","MT","MM"]]

# probabilities matrix
transitionMatrix = [[0.3,0.3,0.4],[0.2,0.3,0.5],[0.1,0.3,0.6]]

if sum(transitionMatrix[0])+sum(transitionMatrix[1])+sum(transitionMatrix[2])!=3:
    print("Ma trận lỗi")
else:
    print("Ma trận đúng")

# A function implements the Markov model to forecast the state/mood.
def activity_forecast(days):
    i=0
    #stating state
    activityToday = "Không mua thường xuyên"
    activityList = [activityToday]

    prob = 1
    while i != days:
        if activityToday == "Không mua thường xuyên":
            change = np.random.choice(transitionName[0], replace=True, p=transitionMatrix[0])
            if change == "KK":
                prob = prob * 0.3
                activityList.append("Không mua thường xuyên")
                pass
            elif change == "KT":
                prob = prob * 0.3
                activityToday = "Thỉnh thoảng mua"
                activityList.append("Thỉnh thoảng mua")
            elif change == "KM":
                prob = prob * 0.4
                activityToday = "Mua thường xuyên"
                activityList.append("Mua thường xuyên")
        elif activityToday == "Thỉnh thoảng mua":
            change = np.random.choice(transitionName[1], replace=True, p=transitionMatrix[1])
            if change == "TK":
                prob = prob * 0.2
                activityList.append("Không mua thường xuyên")
                pass
            elif change == "TT":
                prob = prob * 0.3
                activityToday = "Thỉnh thoảng mua"
                activityList.append("Thỉnh thoảng mua")
            elif change == "TM":
                prob = prob * 0.5
                activityToday = "Mua thường xuyên"
                activityList.append("Mua thường xuyên")
        elif activityToday == "Mua thường xuyên":
            change = np.random.choice(transitionName[2], replace=True, p=transitionMatrix[2])
            if change == "MK":
                prob = prob * 0.1
                activityList.append("Không mua thường xuyên")
                pass
            elif change == "MT":
                prob = prob * 0.3
                activityToday = "Thỉnh thoảng mua"
                activityList.append("Thỉnh thoảng mua")
            elif change == "MM":
                prob = prob * 0.6
                activityToday = "Mua thường xuyên"
                activityList.append("Mua thường xuyên")

        i+=1
    print("Lịch sử lựa chọn: " + str(activityList))
    print("Lựa chọn cuối cùng: " + str(days) + " days: " + activityToday)
    print("Xác suấT của mỗi trạng thái: " + str(prob))
    return activityList

print("activities forecast")
# activity_forecast(3)
# Save activities
list_activity = []
count = 0

# Range start from the first count up until but excluding the last count
for iteretions in range(1,10):
    list_activity.append(activity_forecast(3))

#check all list
# print(list_activity)

# Iterate through the list to get a count of all activities ending in state :'Không mua thường xuyên'
for smaller_list in list_activity:
    if(smaller_list[-1] == "Không mua thường xuyên"):
        count += 1

#Calculate the probability of starting from state:'Không mua thường xuyên' and ending at state:'Mua thường xuyên' 
percentage = (count/10)*100
print("Xác suất bắt đầu ở trạng thái: 'Không mua thường xuyên' và kết thúc ở trạng thái: 'Mua thường xuyên'" + str(percentage)+"%")

                