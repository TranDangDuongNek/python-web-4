# De: tao chuc nang forward, backward cho web browser
# su dung 2 stack de luu
# Lop Browser: visit_page, back, forward

class Browser:
    def __init__(self):
        self.current_page = "home"
        self.back_history = []
        self.forward_history = []


    def visit_page(self, page_name):
        #  lưu trang hiện tại vào back
        self.back_history.append(self.current_page)
        # thay đổi trang hiện tại
        self.current_page = page_name
        # xoá lịch sử forward
        self.forward_history.clear()
        return f"visited: {self.current_page}"

    def back(self):
        if len(self.back_history) == 0: return "no back history"
        #  lưu trang hiện tại vào forward
        self.current_page = self.back_history.pop()
        return(f"back to {self.current_page}")

    def forward(self) :
        # Nếu không có lịch sử chuyển tiếp, trả về "No forward history"
        if len(self.foreward_history) == 0: return "No forward history"
        # Lưu trang hiện tại vào lịch sử quay lại
        self.back_history.append(self.current_page)
        # Di chuyển đến trang tiếp theo trong lịch sử chuyển tiếp
        self.current_page = self.forward_history.pop()
        # In ra thông báo chuyển trang
        return(f"Forward to: {self.current_page}")
    
def testdriver():
    # tạo obj browser
    Browser = Browser()
    functions_table = """ user number 1,2,3 for functionns:
        1. VIsit page --> INput page name
        2. <-- Back
        3. --> Forward
        4. exit
    """
    while request != "4":
        # hiển thị bảng chức năng
        print(functions_table)
        # cho người dùng nhập chức năng
        # cho người dùng yêu cầu
        request = input("Enter your choice: ")
        match request:
            case "1":
                page_name = input("Enter page name : ").split()# xoá khoang trang
                # không dien trang
                if not page_name:
                    print("Page name cannot be empty")
                    continue
                #  page name đúng yêu cầu
                print(Browser.visit_page(page_name))
            case "2":
                print(Browser.back())
            case "3":
                print(Browser.forward())
            case "4":
                print("Exiting browser")
                break
            case _:
                print("Invalid choice, please try again")

        #  xoá request
        request = ""

testdrive()
    
