from collections import deque

def count_students_unable_to_eat(sandwiches, students) -> int:
    students = deque(students)
    sandwiches = deque(sandwiches)

    count = 0
    while students and sandwiches:
        # Lấy phần tử ở đầu 2 danh sách
        if students[0] == sandwiches[0]:
            students.popleft()
            sandwiches.popleft()
            count = 0
        else:
            # nếu không trùng khớp -> đẩy student xuống cuối
            std = students.popleft()
            students.append(std)
            count += 1
            # nếu xoay hết 1 lần -> dừng
            if count == len(students):
                break

    return len(students)


# --- Demo ---
print(count_students_unable_to_eat([1,1,0,0], [0,1,0,1]))  # KQ: 0
print(count_students_unable_to_eat([1,1,1,0,0,1], [1,0,0,0,1,1]))  # KQ: 3