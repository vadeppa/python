

'''
def validate_atm_pin_code(pin):
    is_valid=True
    is_four_or_six=(len(pin)==4) or (len(pin)==6)
    if is_four_or_six:
        is_digits=pin.isdigit()
        if not is_digits:
            is_valid=False
    else:
        is_valid=False
    if is_valid:
        print("Valid PIN Code")
    else:
        print("Invalid PIN Code")
pin = input("enter a pin")
# Call the validate_atm_pin_code function
validate_atm_pin_code(pin)

'''
#==========================================
'''def pincod(pin):
    if len(pin)==4 or len(pin)==6:
        print("it is valid")
    else:
        print("it is not valid")
pin=input("enter a pin:")
pincod(pin)'''

a=input()
k=0
for i in range(1,5):
    temp=" "
    temp=str(a)*i
    k=k+int(temp)
print(k)
