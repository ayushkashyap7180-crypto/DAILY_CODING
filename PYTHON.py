"""name1=input()
unit1=int(input())
price1=float(input())
name2=input()
unit2=int(input())
price2=float(input())
name3=input()
unit3=int(input())
price3=float(input())
r1=unit1*price1
r2=unit2*price2
r3=unit3*price3
if r1>=500:
    s1="High"
elif r1>=200:
    s1="Medium"
else:
    s1="Low"
if r2>=500:
    s2="High"
elif r2>=200:
    s2="Medium"
else:  
    s2="Low"
if r3>=500:
    s3="High"
elif r3>=200:
    s3="Medium"
else:
    s3="Low"
revenues=(r1,r2,r3)
name=(name1,name2,name3)
status=(s1,s2,s3)
total=sum(revenues)
top_revenue=max(revenues)
position=revenues.index(top_revenue)
top_name=name[position]
high_count=status.count("High")
print("="*30)
print("SALES REPORT")
print("="*30)
print(f"${name1}: ${r1:.2f} ({s1})")
print(f"${name2}: ${r2:.2f} ({s2})")
print(f"${name3}: ${r3:.2f} ({s3})")
print(f"Total Revenue: ${total:.2f}")
print(f"Top Revenue: ${top_revenue:.2f} ({top_name})")
print(f"High-Performing Products: {high_count}")"""




room1=input()
count1=int(input())
room2=input()
count2=int(input())
check=input()
print("Room 1:",room1,"-",count1)
print("Room 2:",room2,"-",count2)
if check==room1:
    print("Checked:",room1,"-",count1)
    if count1>=10:
        stt="Enough"
    else:
        stt="Refill"
else:
    print("Checked:",room2,"-",count2)
    if count2>=10:
        stt="Enough"
    else:
        stt="Refill"
print("Status:",stt)
