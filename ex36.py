def dead(why):
    print(why, "So sad!")
    exit(0)

def tardis():
    print("Hello, I am the Doctor and this is my TARDIS!")

    choice = input(">")

    if "it's bigger on the inside" in choice:
        print("Yep!")
        adventure()
    elif "what is" in choice:
        print("Time And Relative Dimension In Space")
        adventure()
    elif "leave" or "walk" in choice:
        dead("Goodbye.")
    else:
        dead("You're no fun.")


def adventure():
    print("When and where to?")

    choice = input(">")

    if choice:
        print("That's fine. The TARDIS decides anyway.")


def start():
    print("You see a blue box.")
    print("Do you keep walking?")
    print("Or knock and go in?")

    choice = input(">")

    if "walk" in choice:
        dead("You miss out on the greatest adventure of your life.")
    elif "knock" in choice:
        tardis()
    else:
        dead("What are you thinking?")

start()
