# ImaginaryCTF-Write-up
## 1. stings
File đính kèm: [stings](https://github.com/thune-work/ImaginaryCTF-Write-up/tree/main/stings)

Đầu tiên, ta phải kiểm tra định dạng file.

![checkStings](https://github.com/thune-work/ImaginaryCTF-Write-up/blob/main/Image/fileStings.PNG)

Như ta thấy trong hình trên, stings là file ELF 64-bit LSB pie excutetable, x86-64 => sử dụng IDApro 64-bit

Chạy thử trên máy ảo xem có gì trong trỏng.

![runStings](https://github.com/thune-work/ImaginaryCTF-Write-up/blob/main/Image/stings/runStings.PNG)

File này hoá ra là một con ong thích chơi trò mật mã. Nếu bạn đoán đúng mật khẩu thì không bị chích. Còn đoán sai thì chetcondime bạn rồi.

Giờ mới xài IDApro 64-bit phân tích file.

Nhìn qua một nùi hàm thì chỉ có hàm main là hàm sẽ giúp chúng ta không bị ong chích. Xem mã giả của hàm main.

Hàm main khai báo nguyên một nùi biến local. Để tránh quan tâm những thành phần không cần thiết, ta tìm chỗ nào có liên quan đến password trước. Đó là dòng 64 đến 79 trong mã giả.

![idaproStings](https://github.com/thune-work/ImaginaryCTF-Write-up/blob/main/Image/stings/idapro.PNG)

v13 chính là chuỗi mà chúng ta nhập vào ở dòng 64. Dựa vào vòng lặp for từ dòng 65, ta đoán được rằng password có 35 ký tự. Dòng 67-71 cho ta biết rằng password có các ký tự liên tiếp có mã ascii bằng các byte liên tiếp tương ứng trừ đi 1 tính từ byte đầu tiên của v14 (dòng 67) trên stack của hàm main (Nếu không thoả sẽ in ra dòng chữ "I'm disappointed. *stings you*" và bị ong cắn). Vậy nên, chúng ta cần quan sát các khai báo biến local của hàm main để xem thứ tự các biến trong stack như nào.

![localVar](https://github.com/thune-work/ImaginaryCTF-Write-up/blob/main/Image/stings/localvar.PNG)

Như vậy, tính từ đỉnh stack theo chiều từ dưới lên trên, kể từ v14, ta có thức tự các biến như sau v14->v15->v16->v17->v18. May thay mấy biến này đều đã được gán giá trị lại còn đủ 35 bytes và mấy nùi code rối rắm còn lại không gây ảnh hưởng đến các giá trị này và khi tới dòng 67-71 chỉ cần lấy chúng ra và quất.

![valueVar](https://github.com/thune-work/ImaginaryCTF-Write-up/blob/main/Image/stings/valueVar.PNG)

*Chú ý*: little-endian, lưu mảng bytes từ dưới lên trên stack.

v14 = 0x7375747C6775646A

v15 = 0x3473356074686F32

v16 = 0x346565326960756F

v17 = 0x623233633832606F

v18 = 0x7E3A37

*Code viết theo little-endian và chuyển sang ký tự ascii: [stings_solve.py](https://github.com/thune-work/ImaginaryCTF-Write-up/tree/main/stings/stings_solve.py)

![result](https://github.com/thune-work/ImaginaryCTF-Write-up/blob/main/Image/stings/result.PNG)

> FLAG: ictf{str1ngs_4r3nt_h1dd3n_17b21a69}




