inp = input('Enter Fahrenheit Temperature:\n')
try:
    float(inp)
    cel = (fahr - 32.0) * 5.0 / 9.0
    print(cel)
except:
    print('Please enter a float number')
