import sys

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