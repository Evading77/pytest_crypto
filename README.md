# Web&API自动化测试框架

## 框架介绍
- Web自动化框架：python3 + pytest-bdd + selenium + log + allure + jenkins。 
  - web自动化框架是基于pytest-bdd的行为驱动框架。
  - Web自动化框架支持运行失败时截图、用例成功运行完成后也进行截图，来保存用例成功运行的有力证据。
    这些截图会附在最后生成的allure报告中。
  - 通过pytest.ini文件配置运行参数，支持失败重跑和多线程运行。
  - 结合allure，运行后可以生成漂亮的allure测试报告。
  - 使用Jenkins持续集成。
    
- API自动化框架：python3 + pytest + requests + yaml + log + allure + jenkins。  
  - API自动化框架是基于pytest+requests，结合yaml的数据驱动框架。
  - 通过pytest.ini文件配置运行参数，支持失败重跑和多线程运行。
  - 结合allure，运行后可以生成漂亮的allure测试报告。
  - 使用Jenkins持续集成。

### 安装指南
1、pip install -r requirements.txt，导入相关依赖库。  
2、下载allure，解压，配置path路径。  
3、下载浏览器对应的driver，并放到对应路径下。  

### 用例说明
- task1:使用Chrome浏览器，访问https://crypto.com/exchange/markets，自动导航到ZIL/USDT的交易页面。
- task2：MyObservatory，在程序的9天预测页面中抓取相应接口，使用接口自动化，从响应中提取后天的相对湿度（例如，60-85%）。



