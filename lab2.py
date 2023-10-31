import math

def compute_circle_relationship(x0, y0, r0, x1, y1, r1):
    d = math.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

    if d > r0 + r1:
        return "The two circles do not intersect and are separate."
    elif d < abs(r0 - r1):
        return "The two circles do not intersect, and one is contained within the other."
    elif d == r0 + r1:
        return "The two circles intersect at a single point."
    elif d == 0 and r0 == r1:
        return "The two circles are coincident."
    else:
        return "The two circles intersect at two points."


def get_valid_input(message, max_attempts=3):
    for _ in range(max_attempts):
        try:
            value = int(input(message))
            return value
        except ValueError:
            print("Please enter a valid integer.")

    print("Maximum attempts reached. Exiting.")
    exit()


def main():
    while True:
        print("\nEnter data for circle 1:")
        x0 = get_valid_input("Enter x coordinate for circle 1: ")
        y0 = get_valid_input("Enter y coordinate for circle 1: ")
        r0 = get_valid_input("Enter radius for circle 1: ")

        print("\nEnter data for circle 2:")
        x1 = get_valid_input("Enter x coordinate for circle 2: ")
        y1 = get_valid_input("Enter y coordinate for circle 2: ")
        r1 = get_valid_input("Enter radius for circle 2: ")

        relationship = compute_circle_relationship(x0, y0, r0, x1, y1, r1)
        print(relationship)

        choice = input("Do you want to continue? (yes/no): ")
        if choice.lower() != 'yes':
            break


if __name__ == '__main__':
    main()
