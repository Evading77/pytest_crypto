import time
import allure

class BasePage:
    def __init__(self,driver):
        self.driver=driver

    #生成错误截图并加入到allure报告里面
    def save_screen_allure(self):
        # 获得一个时间戳的字符串
        str_time = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime())
        # 图片路径
        imge_path = "./image/" + str_time + ".png"
        # 截图
        self.driver.save_screenshot(imge_path)
        # 读取这个图片信息并且把它加入到allure报告里面
        with open(imge_path, mode="rb") as f:
            stream = f.read()
        allure.attach(body=stream, name=imge_path, attachment_type=allure.attachment_type.PNG)


