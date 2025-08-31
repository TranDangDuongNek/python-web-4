def tim_phan_tu(nums):
    tinh_1 = len(nums)
    gioi_han = tinh_1 // 3 
    so_diem = {}
    for tinh_2 in nums:
        if tinh_2 in so_diem:
            so_diem[tinh_2] += 1
        else:
            so_diem[tinh_2] = 1
    ket_qua = []
    for key in so_diem:
        if so_diem[key] > gioi_han:
            ket_qua.append(key)
    return ket_qua

# test-------------------------------------------------------------
nums = [1,1,1,1,3,3]
print(tim_phan_tu(nums))