"""
A marathon is a long-distance race with an official distance of 42.195 kilometers (26 miles 385 yards), usually run as a road race or footrace.

A local marathon was organized at Bavdhan, Pune. The distance actually covered by the participants has been recorded in an array R[] which is an integer array holding the values in kilometers. If there are N number of participants who started running at a particular time, then the size of R[] is N. The participants should cover a distance of more than 0.0 km to get recorded in array R[]. Find the maximum distances covered by the 3 highest racers excluding finishers. If there are only one or two racers excluding finishers, give their distances covered. R[] will be an Input float array. Write a code to take Input array R[], and return 3 maximum distances excluding Finishers. Distance d = 42.195 km.

Example:

Input Values
Enter the distances covered by athletes in Marathon
(Kilometers) please
(press q to terminate)
42.195
42.195
42.195
33.25
40
41.2
38.9
37.5
q

Output Values:
Highest Distance excluding Finishers:
[41.2, 40.0, 38.9]
"""

def marathon():
    max_distance = 42.195
    R = [] 
    print("Enter the distance covered by racers in Marathon (Kilometers) please:\n(q to terminate):")
    
    while True:
        distance_covered = input()
        if distance_covered == "q":
            break
        elif distance_covered=="" or distance_covered ==" ":
            print("Invalid Input !")
            break
        elif float(distance_covered)>max_distance:
            print("Distance cannot be greater than 42.195")
            break
        elif float(distance_covered)>=max_distance or float(distance_covered)<0:
            pass
        else:
            R.append(float(distance_covered))        
    
    # print(R)
    R.sort(reverse=True)
    # print(R)
    print("Highest Distance excluding Finshers:")
    if len(R)>=3:
        print(R[:3])
    else:
        print(R)
        
marathon()