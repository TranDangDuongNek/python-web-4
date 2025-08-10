import csv
import sys
sys.stdout.reconfigure(encoding='utf-8')

def process_csv(file_path) -> None:
    unique_emails = set()
    company_counts = {}

    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            # Kiểm tra số lượng cột (3)
            if len(row) != 3:
                continue # Bỏ qua nếu sai định dạng
            name, comp,email  = row
            # Xóa khoảng trắng ở đầu và cuối email và công ty
            email = email.strip() 
            comp = comp.strip()
            # Kiểm tra email chưa tồn tại trong tập hợp unique_emails
            if email not in unique_emails:
                unique_emails.add(email)

                # Cập nhật số lượng công ty trong dictionary company_counts
                if comp in company_counts:
                    company_counts[comp] += 1
                else:
                    company_counts[comp] = 1

        # Sắp xếp công ty theo số lượng đại biểu giảm dần
        sorted_companies = sorted(
            company_counts.items(), key=lambda item: item[1], reverse=True
        )

        # In kết quả
        print(f"Số lượng đại biểu dự kiến tham dự: {len(unique_emails)}")
        print("Danh sách công ty và số lượng đại biểu:")
        for company, count in sorted_companies:
            print(f"{company} : {count}")

process_csv("B10_BT/data.csv")

