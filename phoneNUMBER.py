import random

otp = random.randrange(100000, 1000000)
print(otp)

user = int(input('Enter the OTP: '))
if otp ==  user:
    print('Access granted!!!')
else:
    print('Access denied!!!')

@app.post("/user/phone_number/send_otp")
async def send_otp(phone_number: str):
    """
    send otp to phone number
    """
    if not phone_number:
        return {"message": "phone number is required"}
    if not phone_number.isdigit():
        return {"message": "phone number should be digits only"}
    if len(phone_number) != 10:
        return {"message": "phone number should be 10 digits"}
    otp = random.randint(1000, 9999)
    print(otp)
    return {"message": "otp sent successfully"}