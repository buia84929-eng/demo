tai_san = [
    {
        "id": 'TS001',
        "ten_tsan": 'May tinh Dell XPS 15',
        "nguoi_sdung": 'Phòng Công Nghệ',
        "gia_ban_dau": 35000000,
        "so_nam_sdung": 5,
        "so_nam_thuc_te": 2,
        "gia_tri_con_lai": 21000000,
        "trang_thai": "Khấu hao nhanh"
    }
]



def hienthi_tsan(tsan_list):
    if len(tsan_list) == 0:
        print('Hệ thống hiện chưa có thông tin tài sản nào')
        return
    print(f"{'Mã TS':<8} | {'Tên tài sản':<20} | {'Người sử dụng':<15} | {'Nguyên giá':<15} | {'Năm hữu ích':<15} | {'Năm đã khấu hao':<15} | {'Giá trị còn lại':<20} | {'Trạng Thái':<15}")
    print('--------------------------------------------------------------------------------------------------------------------------------------------------')
    for taisan in tsan_list:
        print(f"{taisan['id']:<8} | {taisan['ten_tsan']:<20} | {taisan['nguoi_sdung']:<15} | {taisan['gia_ban_dau']:<15} | {taisan['so_nam_sdung']:<15} | {taisan['so_nam_thuc_te']:<15} | {taisan['gia_tri_con_lai']:<20} | {taisan['trang_thai']:<15}")

def them_ts(tsan_list):
    print("Tài sản mới thêm")
    id_moi = int(input("Nhập id mới: "))
    if id_moi == "":
        print("Mã tài sản không được để trống")
    ten_moi = input("Tên tài sản mới: ")
    if ten_moi == "":
        print("Tên tài sản không được để trống")
    phong_bansd = input("Tên phòng ban sử dụng: ")
    if phong_bansd == "":
        print("Phòng ban sử dụng không được để trống")
    nguyen_gia = float(input("Nguyên giá ban đầu: "))
    if nguyen_gia < 0:
        print("Nguyên giá mua ban đầu phải là số lớn hơn 0")
    nam_huuich = int(input("Số năm sử dụng hữu ích: "))
    if nam_huuich < 0:
        print("Số năm sử dụng hữu ích phải lớn hơn 0")
    nam_khauhao = int(input("Số năm khấu hao ban đầu: "))
    if nam_khauhao <= 0:
        print("Số năm thực tế phải lớn hơn hoặc bằng 0")

  

while True:
    print('''
1. Hiển thị danh sách tài sản
2. Khai báo tài sản mới
3. Cập nhật thời gian khấu hao
4. Xóa tài sản khỏi danh mục
5. Tìm kiếm tài sản
6. Thống kê trạng thái tài sản
7. Tính toán khấu hao tự động
8. Thoát chương trình
''')
    choice = int(input("Nhập lựa chọn của bạn (1-8): "))
    match choice:
        case 1:
            hienthi_tsan(tai_san)
        case 2:
            them_ts(tai_san)
        case 8:
            print("Thoát chương trình. Hẹn gặp lại")
            break
        case _:
            print("Yêu cầu nhập lại lựa chọn")