presents = {}


def get_a_number(msg, first=True):
    if not first:
        msg += " (input must be a number) "
    inpt = input(msg)
    try:
        return int(inpt)
    except ValueError:
        return get_a_number(msg, first=False)


if __name__ == "__main__":
    # Ask the user to add recipients
    while True:
        inpt = input("Enter the name of a recipient or press Enter when done: ")
        if not inpt:
            break
        presents[inpt] = {"counter": 0}

    # For each recipient, ask how many presents they have
    for recipient in presents:
        presents[recipient]["amount"] = get_a_number(
            "How many presents does %s have? " % recipient
        )

    ts = {}
    total_presents = sum(recipient["amount"] for recipient in presents.values())
    for i, person in enumerate(presents):
        step = float(total_presents) / presents[person]["amount"]
        for j in range(1, presents[person]["amount"] + 1):
            ts[float("%s%s" % (step * j, i + 1))] = person
    for score, name in sorted(ts.items(), key=lambda x: x[0]):
        print(name)
    given = 0
    for score, name in sorted(ts.items(), key=lambda x: x[0]):
        given += 1
        input("Give %s a present! (%d remaining)" % (name, total_presents - given))

    print("All presents presented!")
