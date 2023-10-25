Richter_magni=float(input("Enter The Richter magnitude value in Float"))

if (Richter_magni>1.0 and Richter_magni<2.0):
    print("Microearthquakes not felt or rarely felt")
elif(Richter_magni> 2.0 and Richter_magni< 4.0 ):
    print("Very rarely causes damage")
elif(Richter_magni> 4.0 and Richter_magni< 5.0 ):
    print("amage done to weak buildings")
elif(Richter_magni> 5.0 and Richter_magni< 6.0):
    print("Cause damage to the poorly constructed building")
elif(Richter_magni> 6.0 and Richter_magni< 7.0  ):
    print("Causes damage to well-built structures")
elif(Richter_magni> 7.0 and Richter_magni< 8.0):
    print(" Causes damage to most buildings")
elif(Richter_magni> 8.0 and Richter_magni< 9.0):
    print("Causes major destruction")
else:
    print(" Causes unbelievable damage")