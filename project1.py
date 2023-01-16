print("1.Enter 'R' for 'RUPEES' ")
print("2.Enter 'D' for 'DOLLARS' ")
print("3.Enter 'Y' for 'YEN' ")
m=str(input("Which currency would you want to convert:")).capitalize()


#converting RUPEES into DOLLARS and YEN
if m=="R":
    print("Into which currency would you want to convert 'RUPEES'")
    print("1.If you want to convert into 'DOLLARS' enter 'D' ")
    print("2.If you want to convert into 'YEN' enter 'Y' ")
    r=str(input("ENTER HERE:")).capitalize()
    
    if r=='D':
     hr=float(input("Enter how many 'RUPEES' would you want to convert into 'DOLLARS':")) 
     rd=hr*0.012
     print(hr,"RUPEES =",rd,"DOLLARS")

    elif r=='Y':
     hr=float(input("Enter how many 'RUPEES' would  you want to convert into 'YEN':")) 
     ry=hr*1.65
     print(hr,"RUPEES =",ry,"YEN")



  #converting DOLLARS into RUPEES and YEN 
     
elif m=='D':
    print("Into which currency would  you want to convert 'DOLLARS':")
    print("1.If you want to convert into RUPEES enter 'R' ")
    print("2.If you want to convert into yen enter 'Y' ")
    d=str(input("ENTER HERE:")).capitalize()
    
  
    if d=='R':
     hd=float(input("Enter how many 'DOLLARS' would  you want to convert into 'RUPEES':")) 
     dr=hd*82.24
     print(hd,"DOLLARS =",dr,"RUPEES")


    elif d=='Y':
     hd=float(input("Enter how many 'DOLLARS' would  you want to convert into 'YEN':")) 
     dy=hd*136.76
     print(hd,"DOLLARS =",dy,"YEN")

#converting YEN into RUPEES and DOLLARS 

    
elif m=='Y':
    print("Into which currency would you want to convert 'YEN':")
    print("1.If you want to convert into RUPEES enter 'R' ")
    print("2.If you want to convert into DOLLARS enter 'D' ")
    y=str(input("ENTER HERE:")).capitalize()


    
    if y=='R': 
     hy=float(input("Enter how many 'YEN' would  you want to convert into 'RUPEES':")) 
     yr=hy*0.60
     print(hy,"YEN =",yr,"RUPEES")


    elif y=='D': 
     hy=float(input("Enter how many 'YEN' would  you want to convert into 'DOLLARS':")) 
     yd=hy*0.0073
     print(hy,"YEN =",yd,"DOLLARS")


else: 
    print(m,"IS NOT VALID INPUT,PLEASE TRY AGAIN.")
     




        

    
