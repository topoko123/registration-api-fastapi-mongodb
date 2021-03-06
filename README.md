# registration-api-fastapi-mongodb
ชื่อเต็ม คือ Abdul registration API

ณ ปัจจุบันโลกได้มีการพัฒนา API หรือ Application Programming Interface ซึ่งจะทำหน้าที่เชื่อมระบบหนึ่งไปสู่อีกระบบหนึ่ง เพื่อให้ซอฟต์แวร์จากภายนอกสามารถเข้าถึงและอัพเดทข้อมูลนั้นได้ แต่อยู่ในขอบเขตที่ถูกกำหนดไว้ จึงได้มีนักพัฒนา หรือ องค์กรต่าง ๆ มากมายได้พัฒนาบริการต่าง ๆ เป็นของตนเอง และถูกเรียกใช้งานผ่าน API
สำนักงานวิทยาศาสตร์และคอมพิวเตอร์แห่งชาติ ( NECTEC ) เป็นสถาบันวิจัย เทคโนโลยีที่เกี่ยวข้องกับคอมพิวเตอร์ โดยของแผนก Speech and Text Understanding จะทำการวิจัยเกี่ยวกับการเข้าใจภาษาธรรมชาติ ( Natural Language ) และปัญญาดิษฐ์ ( artificial intelligence ) และยังได้พัฒนา Chatbot ออกมาในรูปแบบของ API เพื่อให้ผู้ใช้ หรือ นักพัฒนาต่าง ๆ สามารถนำไปใช้ได้
เราจึงได้พัฒนา และจัดทำระบบลงทะเบียนบริการ API ออกมาในรูปแบบของ Web Application Platform ขึ้นมาเพื่อให้นักพัฒนาต่าง ๆ สามารถนำเอา API ที่ทำระบบบริการต่าง ๆ ของตนมาฝากไว้กับระบบการจัดการข้อมูล API ของทางเรา เพื่อเผยแพร่ ให้นักพัฒนาอื่นสามารถนำไปใช้ได้ง่ายขึ้น


 
 ## ระบบลงทะเบียนบริการ api จัดทำในส่วนของ database 
 
 workflow: Frontend -> Controller -> Backend( database ) 
 โดยโปรเจ็คชิ้นนี้เป็น 1 ในส่วของโปรเจ็คทั้งหมดของ Abdul registration API โดยจะมีทั้งหมด 3 โปรเจ็คและเชื่อมเข้าหากันด้วย API  มีดังนี้
- Font End: https://github.com/javakung/ABDUL-Registerations-API
- Controller: https://github.com/taefreeze/PythonApiController
- Back End: https://github.com/topoko123/registration-api-fastapi-mongodb/

## เหตุผลที่ต้องทำแยกออกเป็น 3 ชุดแล้วเชื่อมหากัน
- มันจะช่วยให้เราเข้าใจการทำงานเป็นทีม และเข้าใจว่า Font End ควรทำอะไร Controller ควรทำอะไร Backend ควรทำอะไร
- deploy แยกกันไปคนละโปรเจ็ค เมื่อเจอปัญหาก็จะสามารถแก้ปัญหาได้ง่ายขึ้น
- จากที่หาข้อมูลสิ่งนี้น่าจะถูกเรียกว่า Thee-tier architecture

 ### จัดทำให้กับ
 คุณชัชวาล สังคีตตระการ นักวิจัย ทีมวิจัยการเข้าใจเสียงและข้อความ กลุ่มวิจัยปัญญาประดิษฐ์ จากศูนย์เทคโนโลยีอิเล็กทรอนิกส์และ คอมพิวเตอร์แห่งชาติ (NECTEC)
