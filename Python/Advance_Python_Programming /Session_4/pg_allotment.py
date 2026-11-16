
# PG ROOM ALLOTMENT SYSTEM

# Task 1: Room Dictionary

rooms = {
    "R101": 2,
    "R102": 3,
    "R103": 2,
    "R104": 3,
    "R105": 2,
    "R106": 3
}

students = {
    "R101": [],
    "R102": [],
    "R103": [],
    "R104": [],
    "R105": [],
    "R106": []
}


# Task 2: Custom Exceptions

class InvalidRoomError(Exception):
    pass


class RoomFullError(Exception):
    pass


class DuplicateStudentError(Exception):
    pass


class StudentNotFoundError(Exception):
    pass


# Allot Room Function

def allot(student_name, room_no):

    if room_no not in rooms:
        raise InvalidRoomError("Room does not exist!")

    for room_students in students.values():
        if student_name in room_students:
            raise DuplicateStudentError(
                "Student already has a room!"
            )

    if len(students[room_no]) >= rooms[room_no]:
        raise RoomFullError("Room is already full!")

    students[room_no].append(student_name)

    return f"{student_name} successfully allotted to {room_no}"


# Vacate Room Function

def vacate(student_name):

    for room_no, room_students in students.items():

        if student_name in room_students:
            room_students.remove(student_name)

            return f"{student_name} vacated from {room_no}"

    raise StudentNotFoundError(
        f"{student_name} is not allotted to any room!"
    )


# Task 3 and 4: Menu Loop

while True:

    print("\n===== PG ROOM ALLOTMENT SYSTEM =====")
    print("1. Allot Room")
    print("2. Vacate Room")
    print("3. View All Rooms")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter student name: ")
        room = input("Enter room number: ").upper()

        try:
            message = allot(name, room)
            print(message)

        except InvalidRoomError as e:
            print(e)

        except RoomFullError as e:
            print(e)

        except DuplicateStudentError as e:
            print(e)

    elif choice == "2":

        name = input("Enter student name: ")

        try:
            message = vacate(name)
            print(message)

        except StudentNotFoundError as e:
            print(e)

    elif choice == "3":

        print("\n----- ROOM DETAILS -----")

        for room_no, capacity in rooms.items():

            print(f"\nRoom: {room_no}")
            print(f"Capacity: {capacity}")
            print(f"Students: {students[room_no]}")

    elif choice == "4":

        print("Thank you for using PG Allotment System!")
        break

    else:
        print("Invalid choice! Please try again.")
