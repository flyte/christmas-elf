from collections import deque

from ipdb import set_trace


presents = {}


def get_a_number(msg, first=True):
    if not first:
        msg += " (input must be a number) "
    inpt = raw_input(msg)
    try:
        return int(inpt)
    except ValueError:
        return get_a_number(msg, first=False)


worthiest_recipient = lambda presents: sorted(
    presents.items(), key=lambda x: x[1]["counter"], reverse=True
)[0][0]


if __name__ == "__main__":
    # Ask the user to add recipients
    while True:
        inpt = raw_input("Enter the name of a recipient or press Enter when done: ")
        if not inpt:
            break
        presents[inpt] = {"counter": 0}

    # For each recipient, ask how many presents they have
    for recipient in presents:
        presents[recipient]["amount"] = get_a_number("How many presents does %s have? " % recipient)

    highest_amt = max(recipient["amount"] for recipient in presents.values())
    total_presents = sum(recipient["amount"] for recipient in presents.values())
    for person in presents:
        presents[person]["probability"] = presents[person]["amount"] / float(total_presents)

    queue = deque()
    for _ in xrange(highest_amt * len(presents)):
        print "Before adding: %s " % presents
        # Add each recipients probability to their counter
        for recipient in presents:
            presents[recipient]["counter"] += presents[recipient]["probability"]
        print "After adding: %s " % presents
        # Get the highest counter, add their name to the queue and set the counter to 0
        recipient = worthiest_recipient(presents)
        print "Worthiest recipient: %s" % recipient
        queue.appendleft(recipient)
        presents[recipient]["counter"] = 0
