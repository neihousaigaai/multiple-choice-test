# Hướng dẫn sử dụng

Đầu tiên, khi các bạn khởi động chương trình, các bạn sẽ thấy có cửa sổ có dạng như sau:

![init_window.png](/how_to_use_pic/init_window.png)

Có 4 thông tin bạn cần quan tâm:

- **"Number of questions:"** số câu hỏi trong bài kiểm tra của bạn.
- **"Subject:"** môn kiểm tra.
- **"Name:"** tên của bạn.
- **"Time (min):"** thời gian làm bài (tính theo phút)

Sau khi nhập đầy đủ thông tin, bạn có thể nhấn phím Enter để bắt đầu vào "phòng thi".

> **To developers:** Nút OK mình không đặt trạng thái DISABLED, tuy vậy dữ liệu đầu vào luôn được kiểm tra, đảm bảo người dùng nhập vào đúng chuẩn.

Khi bạn bỏ trống bất kì 1 field nào hay nhập không hợp lệ, sẽ có thông báo "Invalid input!" hiện lên cho bạn.

Một ví dụ nhập thông tin hợp lệ:

![try_info.png](/how_to_use_pic/try_info.png)

Sau khi nhập thông tin hợp lệ, bạn hãy ấn OK. Cửa sổ "phòng thi" sẽ hiện lên. Dưới đây là ví dụ cửa sổ "phòng thi" với các thông tin như ví dụ trên:

![test_window.png](/how_to_use_pic/test_window.png)

Giao diện cũng rất thuận tiện cho người sử dụng. Bạn hãy chú ý 4 khu vực trên cửa sổ này:

- Khu vực các button:
    - **Start:** bắt đầu làm bài. Ban đầu, chỉ có nút Start có thể ấn được, còn các button còn lại đều ở trạng thái DISABLED.
    - **Stop:** nộp bài. Nút này có hiệu lực sau khi bạn đã bắt đầu làm bài và trước khi hết giờ làm bài, và bạn chỉ được dừng làm bài **một lần duy nhất**. Đi thi thật, giám thị thường nhắc bạn làm hết 2/3 thời gian mới được nộp bài ra về, hay thảm hơn là không được nộp sớm trong các kì thi trắc nghiệm; nhưng ở đây, các bạn có thể nộp bài lúc nào tuỳ thích (nhưng nộp rồi là không được lấy bài về đâu nhé). Nộp giấy trắng cũng không sao :smile:
    - **Check:** chấm bài. Nút này sẽ chuyển sang trạng thái ENABLED sau khi bạn đã nộp bài. Nộp bài rồi cũng phải chấm điểm chứ :smile: Bạn chỉ cần nạp file kết quả và ấn nút, thế là xong.
    - **Export:** Bạn có thể lưu lại kết quả bài kiểm tra sau khi đã chấm xong vào 1 file '.txt'. Về sau, nếu bạn muốn theo dõi quá trình luyện tập của mình, bạn có thể mở các file kết quả cũ để xem mình tiến bộ đến đâu. Thật tiện lợi phải không nào?
- Khu vực đồng hồ đếm ngược: bạn có thể trực tiếp xem bạn còn bao nhiêu thời gian làm bài.
- Khu vực điểm (cái khung hơi lõm bên góc trên phải): Hệ thống sẽ cho biết bạn đã được bao nhiêu điểm.
- Khu vực làm bài: gồm số hiệu câu hỏi và các phương án trả lời trắc nghiệm A, B, C, D. Có 4 cột câu hỏi. Trước giờ làm bài và sau khi nộp bài, bạn sẽ không thể thay đổi đáp án ở khu vực làm bài.

    > **To developers:** Hiện tại mình chưa viết code config phần trình bày các cột câu hỏi. Có gì sau này sẽ viết lại.

- Hướng dẫn:
    - Bắt đầu làm bài, bạn ấn nút Start. Đồng hồ đếm ngược bắt đầu đếm. Các bạn có thể thấy, các nút Start, Check và Export đang ở trạng thái DISABLED.
    
    ![testing.png](/how_to_use_pic/testing.png)

    - Khi bạn muốn nộp bài sớm, hãy ấn nút Stop. Sẽ có thông báo hiện ra cho bạn:
    
    ![want_to_stop.png](/how_to_use_pic/want_to_stop.png)
    
    Hãy suy nghĩ thật kĩ trước khi ấn Yes, bạn sẽ không có cơ hội để làm lại đâu! Sau khi bạn ấn Yes, sẽ có thông báo xác nhận bạn đã ấn Yes.
    
    ![stopped.png](/how_to_use_pic/stopped.png)
    
    Bạn có thể thấy, phần làm bài đã bị khoá, bạn không thể làm gì được nữa.

    - Sau khi nộp bài, bạn có thể tự chấm bài. Hệ thống yêu cầu bạn tự chuẩn bị trước một file `.txt` lưu trữ đáp án đúng. Bạn có thể tự tạo nó, hoặc copy từ file đáp án của đề rồi paste vào file này.
    
    Lưu ý khi nhập thông tin vào file, bạn nên viết mỗi câu trên 1 dòng. Hệ thống chỉ chấp nhận thông tin có dạng `<câu hỏi><đáp án>` (viết liền) hoặc `<câu hỏi> <đáp án>` (có dấu cách). Ví dụ như hình:
    
    ![answer_file.png](/how_to_use_pic/answer_file.png)

    Ấn vào nút Check. Một cửa sổ hiện ra, bạn tìm đến nơi chứa file đáp án vừa rồi và chọn "Open".
    
    ![choose_answer_file.png](/how_to_use_pic/choose_answer_file.png)
    
    Và... úm ba la!

    ![checked.png](/how_to_use_pic/checked.png)

    Có các dấu tick đúng và sai, giúp các bạn theo dõi các câu đúng, câu sai dễ dàng hơn. Có vẻ như khả năng lụi của mình hơi tệ :smile:

    - Sau khi chấm xong, bạn có thể lưu kết quả lại để lần sau có thể theo dõi. Khi bạn ấn "Export", một cửa sổ hiện ra để bạn có thể lựa chọn nơi lưu trữ kết quả.

    ![save_result.png](/how_to_use_pic/save_result.png)

    Sẽ có 1 thông báo hiện ra sau khi bạn lưu thành công:

    ![saved_result.png](/how_to_use_pic/saved_result.png)

    Ta sẽ thử xem file kết quả như thế nào:

    ![result_file.png](/how_to_use_pic/result_file.png)

    Các bạn có thể thấy, những thông tin cần thiết đều đã được lưu trong file `result.txt` để các bạn có thể biết được mình đã làm bài kiểm tra vào lúc nào, được bao nhiêu câu, sai bao nhiêu câu, bỏ bao nhiêu câu, từ đó có thể đưa ra phương án học và ôn luyện tốt nhất.
