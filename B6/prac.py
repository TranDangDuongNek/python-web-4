


try:
    # input 
    n = int(input())
    if n <= 0:
        raise ValueError("n must be a positive integer")
    arr = [int(x) for x in input().split(" ")]
    if len(arr) != n:
        raise ValueError("The number of elements does not match n")
    target = int(input())

    # thuc thi thuat toan
    arr.sort()
    result = binary_search_loop(arr, target)
    print(result)
except Exception as e:
    print("Error:", e)
