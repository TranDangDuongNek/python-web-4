import time

def running_time(func) -> None:
    print("Bat dau chay ham----------------- ")
    start_time = time.time()  # lấy thời gian hiện tại
    result = func()
    end_time = time.time()
    print(f"Ket qua chay ham: {result}")
    print(f"Thoi gian thuc thi: {(end_time - start_time):.6f} giay")
    print("Ket thuc chay ham----------------")
