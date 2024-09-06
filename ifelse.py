n1 = input("plz enter sugar number")
n2=float(n1)
if n2<80:
    print(f"{n2} sugar is low")
elif n2>100:
    print(f"{n2} suagr is high")
else:
    print("sugar is normal")
message="sugar is low" if n2<80 else "suagr is noraml"
print(message)