score=input("Enter score:\t")

try:
    score=float(score)
    if score>=70:
                print("Grade:\tA")
    elif score>=60:
                print("Grade:\tB")
    elif score>=50:
                print("Grade:\tC")
    elif score>=45:
                print("Grade:\tD")
    elif score<45:
            print("Grade:\tF")
except:
        print("Wrong Score!,\tScore should be a float number")