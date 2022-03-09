class Balance:

    amount = None

balance_1 = Balance()
balance_1.amount = 5000


class Person(Balance):
    first_name = None
    last_name = None
    number = None

print(Person().amount)
jack = Person()
jack.first_name = "jack"
jack.last_name = "Barbaro"
jack.number = "+996508172839"
jack.amount = 5000
jack.amount = jack.amount + 40