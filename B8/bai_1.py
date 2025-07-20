# ĐỀ 1
def check_duplicate(arr1, arr2) -> list:
    # Kiểm tra ngoại lệ: nếu 1 trong 2 mảng rỗng thì trả về mảng rỗng
    if not arr1 or not arr2:
        return []

    d = []  # Danh sách chứa phần tử chung của cả 2 mảng, không trùng

    # Duyệt mảng ngắn hơn để tối ưu
    if len(arr1) < len(arr2):
        for item in arr1:
            # Nếu phần tử có trong arr2 và chưa có trong danh sách kết quả
            if item in arr2:
                if item not in d:
                    d.append(item)
    else:
        for item in arr2:
            if item in arr1 and item not in d:
                d.append(item)

    return d



# input:
# nhập mang 1:
len_arr1 = int(input("Do dai mang 1: "))
arr1 = []
if len_arr1 > 0:
    for i in range(len_arr1):
        item = input(f"Phan tu thu {i + 1}: ")
        if item:
            arr1.append(item)
    print(f"Mang 1 la: {arr1}")

# -------------------------------------
# nhập mang 2: 
len_arr2 = int(input("Do dai mang 1: "))
arr2 = []
if len_arr2 > 0:
    for i in range(len_arr2):
        item = input(f"Phan tu thu {i + 1}: ")
        if item:
            arr2.append(item)
    print(f"Mang 2 la: {arr2}")

# so sánh và in kết quả
dup = [item for item in arr1 if item in arr2]
print(f"Danh sách phần tử có ở cả 2 mảng: {dup}")


