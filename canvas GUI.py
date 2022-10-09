hour=int(input("Enter hours:\t"))
rate=int(input("Enter Rate:\t"))
if hour>40:
    print("Pay:\t", (hour*rate)*1.5)
else:
    print("Pay:\t",hour*rate)
