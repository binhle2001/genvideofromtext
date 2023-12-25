from tts.source.synthesizer import convert_text_to_speech
import os
string = """Xin chào các bạn, mình là Duyên - giảng viên khóa Tester cơ bản tại Học viện Tokyo Tech Lab. Ở video trước, mình đã giới thiệu các bạn lộ trình khóa học Tester cơ bản cũng như con đường sự nghiệp của các bạn khi bước vào ngành Tester. 
Hôm nay, chúng ta sẽ đi vào nội dung đầu tiên của khóa học, những khái niệm cơ bản về Kiểm thử phần mềm. Trong buổi học này, chúng ta sẽ bắt đầu với khái niệm Kiểm thử phần mềm, Quy trình kiểm thử phần mềm và Mục đích của Kiểm thử phần mềm. 
Trước khi đi vào nội dung chính của buổi ngày hôm nay, mình cũng thông báo, xuyên suốt khóa học, mình sẽ kết hợp sử dụng cả tiếng Việt và tiếng Anh - một số thuật ngữ thông dụng được sử dụng nhiều trong quá trình làm việc. Có 1 số thuật ngữ chuyên ngành được trình bày bằng tiếng Anh, mình sẽ cố gắng giải thích luôn, nếu các bạn có thắc mắc, hãy để lại comment hoặc liên hệ với Mentor để được hướng dẫn chi tiết nhé.
Đầu tiên chúng ta cùng tìm hiểu xem Kiểm thử phần mềm là gì?
Chắc hẳn trước khi quyết định học khóa này, các bạn cũng có tìm hiểu qua internet và bạn bè người thân về kiểm thử phần mềm và nghề tester sẽ phải làm những công việc gì rồi đúng không? 
Ở đây mình sẽ định nghĩa một cách đầy đủ và chi tiết cho các bạn. 
Kiểm thử phần mềm, hay còn gọi là Software Testing, là quá trình vận hành thử nghiệm một chương trình, một hệ thống phần mềm để xác định xem nó có đáp ứng đúng yêu cầu và tạo ra kết quả mong muốn hay không? 
Trong quá trình đó, ta xác định/tìm thấy lỗi/bug trong sản phẩm/dự án. Từ khái niệm này, chúng ta có thể hiểu Tester là người kiểm thử, kiểm thử viên, tham gia vào hoạt động tìm kiếm, phát  hiện lỗi của các sản phẩm phần mềm. Đây là khái niệm đơn giản ở mức vi mô, nói rộng ra, trách nhiệm và công việc của người kiểm thử không dừng lại ở việc tìm lỗi mà cần đi sâu vào các khía cạnh khác của một phần mềm như hiệu năng, hiệu suất làm việc, hay vấn đề bảo mật. Những yếu tố này không phải chức năng của một phần mềm nhưng ta cần đảm bảo được các yếu tố này hoạt động tốt. Tức là Tester sẽ là người đảm bảo chất lượng phần mềm chứ không đơn thuần chỉ đi tìm lỗi. 

VD: Mỗi lần nhà trường mở đăng ký tín chỉ vào 12h trưa, sinh viên vào đăng ký thì trang web luôn bị treo không thể vào được. Mặc dù các chức năng vẫn hoạt động bình thường nếu mở được chức năng đó ra, nhưng hiệu năng hoàn toàn không tốt, dẫn đến nhiều người truy cập thì trang web bị sập luôn không thể làm gì được. Đây là một lỗi không thuộc bất kỳ chức năng nào trong hệ thống nhưng nhờ đó đánh giá được chất lượng phần mềm không tốt. Lỗi này lọt ra do trách nhiệm đội kiểm thử chưa tốt. Vì thế các bạn luôn phải ghi nhớ trách nhiệm của đội ngũ kiểm thử không chỉ tìm lỗi trong phần mềm. 

Vậy kiểm thử phần mềm có quan trọng không? Câu trả lời chắc chắn là vô cùng quan trọng. Đây là mắt xích không thể thiếu trong quá trình sản xuất phần mềm để có thể cung cấp được 1 sản phẩm có chất lượng tới khách hàng. 
Và các bạn cũng biết có nhiều phần mềm trên thế giới, chỉ vì lơ là khâu kiểm thử để lọt BUG ra gây hậu quả vô cùng quan trọng khiến doanh nghiệp tốn hàng triệu đô, hay ảnh hưởng đến hàng triệu người dùng. 
Vậy trách nhiệm của người kiểm thử là phải tìm ra được các rủi ro đó để ngăn chặn ngay từ đầu nhằm giảm thiểu rủi ro, giảm thiểu chi phí bảo trì phần mềm sau này. 
"""

import time
t = time.time()
convert_text_to_speech(string)
print("Processing time = ", time.time() - t)