import re
phone = input("Phone Number: ")
# phone = '+996-707-77-77-77'
result = re.match(r"^\+([0-9]{1,3})-([0-9]{1,3})-([0-9]{2})-([0-9]{2})-([0-9]{2})", phone)

try:
    if phone[result.start():result.end()] == phone:
        print("Phone Nomber Valid")

    else:
        raise "IS not valide phone nuber!"
except:
    print("IS not valide phone nuber!")


print(result)
