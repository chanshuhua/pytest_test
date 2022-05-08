##### pytest版本
```
pip install pytest
pytest --version

pip install -plugins:base-url-1.4.1, dependency-0.5.1, forked-1.3.0, html-2.1.1, metadata-1.8.0, orderin
g-0.6, rerunfailures-9.1.1, selenium-1.17.0, variables-1.9.0, xdist-2.2.0

```

##### 使用pytest的命名规则
```
1、模块命名已test_开头，或_test结尾。
2、测试类名必须以Test开头，不能有_init方法。
3、测试方法必须以test开头
```

##### pytest-基础 运行参数、配置文件pytest.ini、mark、skip、--html report（自带）
```
1、主函数 
   运行所有用例  pytest.main()
   运行执行模块  pytest.main(['-sv','./testcase/test_case01.py'])  #指定文件
               pytest.main(['-sv','./testcase])  # 指定模块
               pytest.main(['-sv','./testcase/test_case01.py::Test_01::test_case01']) # 根据nodeid指定对应方法
2、命令行  
   运行所有用例  pytest
   运行执行模块  pytest -sv + (与上述运行路径一致)
              

参数详解： -s 输出调试信息，包括print打印信息
         -v 输出详细信息，包括文件所在文件位置及通过情况
         -sv 可同时使用（方便查看信息）
         -n 多线程分布式运行测试用例  # pytest -sv testcase/ -n 4
         --reruns num    # pytest -sv testcase/  --reruns 2
         -x 遇到失败用例即停下跑测试用例
         --maxfail 最大失败用例数 # pytest -sv ./testcase/  --maxfail 2
         -k 根据测试用例中包含指定字符串执行测试用例  # pytest -sv ./testcase/  -k "01"


3、pytest 默认执行按照顺序文件及测试用例顺序：从上到下
         pip install pytest-ordering         
         @pytest.mark.run(order=num) 

4、根据读取pytest.ini配置文件运行
   pytest.ini为pytest单元测试框架的核心配置文件
   文件位置：项目根目录
   文件格式：ANSI
   作用：自定义pytest运行方式，更改默认运行方式
   运行规则：命令行或者main函数均会优先读取pytest.ini配置文件
    
    [pytest]
    addopts = -sv  # 命令行参数
    testpaths = ./testcase # 测试用例路径
    python_files = test_*.py # default模块名规则
    python_classes = Test*  # default类名规则
    python_functions = test  # default方法名规则
   
    markers = DEV_SMOKE_TEST # 标记
              ENV_CHECK
              DAILY_TEST
              INIT_TEST

5、分组执行用例
    分组：冒烟、模块、接口、web
    pytest -sv -m "DEV_SMOKE_TEST" and "ENV_CHECK"  #已在pytest.ini配置分组模块名  且关系
    pytest -sv -m "DEV_SMOKE_TEST" or "ENV_CHECK"  #已在pytest.ini配置分组模块名  或关系
      
6、pytest跳过测试用例
    @pytest.mark.skip(reason="") #无条件跳过
    @pytest.mark.skipif({全局变量公式}age>18,reason="") # 有条件跳过

7、生成测试报告（pytest自带）
    addopts = --html {生成html的目录}./report/report.html

```
##### pytest 装饰器、fixtrue/conftest/params/allure
```
1、测试用例前后置、固件
    重复代码分装，类继承来引用！！
    
    # 全部用例前后置
    def setup() # 每个测试用例之前执行一次
    def teardoen() # 每个测试用例之后执行一次

    def setup_class() # 每个类之前执行一次
    def teardoen_class() # 每个类之后执行一次

2、使用fixture数据驱动-实现前后置
    2.1 fixture(scope autouse) 参数详解
    @pytest.fixture(scope="function",autouse=True) # 全局用法，需要打开autouse才可使用
        -scope:作用域
            function：在函数之前和之后执行  
                1、手动调用特定函数： 用例函数传参中输入fixture固件名称
                2、fixture固件 通过return或yield返回值，可将这个fixture值传送到测试用例中。
                
            class：在类之前和之后执行
                1、手动调用特定类： 在指定类前加上@pytest.mark.usefixture("fixture固件名称")装饰器。
                
            package/session: 在整个项目会话之气那和之后执行（仅一次）
                1、一般结合conftest.py文件一起实现。

        -autouse:False # 默认所有调用前后置调用为关闭状态
       
    2.2 前后置详解 
        # 前置：
        def func():
            do ..
        
        # 后置:
        def func():
            yield
            do ..

        # 部分用例前后置：
        1、@pytest.fixture(scope="function")
           def func():
            ...
        2、def test_case(self,func):
            pass

        # 所有用例前后置：
        1、@pytest.fixture(scope="function",autouse=True)
           def func():
            ...
        2、def test_case(self):
            pass

    
    2.2 fixture(params ids name) 参数详解
        -params: 固件内参数化 -> 参数传送到固件，用例通过固件得到参数值，实现用例多个参数化
            def func_params():
                ...
                return [list]/[{dict}]/(tuple)

            @pytest.fixture(scope='function',autouse=False,params=func_params()) #!!!
            def fixture_use(request): # !!!
            ...
            yield request.param #!!固定写法，返回list中的单个参数
            
            def test_case(self,fixture_use):
                print("fixture_use")
                # 结果中输出test_case执行 len(list)次，每一次输出list值
 
        -ids 对参数params起别名
                @pytest.fixture(scope="function",params=paramss(),ids=['aliasname1','aliasname2'])
                def func_fixture(request):
                    ...
                    yield request.param
                    ...

                #结果中输出的用例参数会携带改别名
        
        -name 对固件fixture起别名,那么本身固件fixture名称失效，全局和子目录下的name不能重名。
            @pytest.fixture(scope="function",params=paramss(),name="paramss_list")
            def func_name(request):
                yield request.param
                print("name")
            
            def test_case(self,paramss_list)
                # 调用别名才可使用
                print("paramss_list")

3、conftest.py 和 fixture 的结合使用: fixture固件可在别的文件下使用
    3.1、conftest.py
        定义：conftest.py文件为存放固件fixture的固定配置文件,则所有不同文件夹下的用例均可直接调用文件下的固件fixture。
        文件位置: 全局固件-项目根目录下、各项目分支-各项目用例目录下。
        好处: 调用时不需要导入、引用包。
        引用规范:conftest.py文件可以有多个, 且一个用例可以调用多个conftest.py文件里的fixture。
            scope=function 可在每个用例前获取某些登录参数
            scope=session 可在自动化前做好准备工作
        
4、setup/teardown/setup_class/teardown_class/fixture/conftest 优先级
    1、fixture 的session级别优先级最高
    2、fixture 的class > setup_class & teardown_class
    3、fixture 的function > setup & teardown

5、pytest执行顺序
    1、查找根目录下的conftest.py文件。
    2、查找根目录下的pytest.ini文件。
    3、查找用例目录
    4、查找用例目录下的conftest.py文件。
    5、查找py文件中是否存在util-> setup/teardown/setup_class/teardown_class 文件。
    6、根据pytest.ini下的用例目录及规则执行用例。

6、pytest断言
assert
    1、相等/大于/小于断言 1==1 1<2
    2、包含断言 'a' in 'abc'

7、pytest 结合allure-pytest 插件生成美观的报告
    1、pip install allure-pytest
    2、安装allure，项目内配置环境变量,用户变量下的Path新增bin/allure.bat文件地址。
    3、pycharm要更新环境变量。settings->console->python console 或者重启pycharm 去重新load环境变量。
    4、生成allure报告
    5、创建allure 报告临时存储文件夹。 pytest.ini 文件中需新增
    6、生成allure报告。
       6.1、生成临时allure报告
        addopts = --alluredir={存放allure报告临时文件夹}./temp  --clean-alluredir(清除上一次生成的报告文件)
       6.2、生成正式allure报告
        python main函数运行所用用例执行完成后后
            sleep(3) # 生成临时报告文件
            os.system("allure generate ./temp -o ./report/allure_reports --clean ") #生成allure报告固定写法
    7、定制化allure内容，可自定义日志，输入输出值。

```
##### pytest-高级用法 parametrize实现数据驱动、yaml测试用例、框架请求封装、接口关联封装、结合jenkins实现接口集成
```
1、使用parametrize 数据驱动-实现测试用例参数化
    若fixture为测试用例test_* 前后置执行步骤，则parametrize()则为测试用例中的数据驱动。
    执行结果： 根据参数名进行传送，根据参数值以此取数执行测试用例，最终执行用例个数等于参数值个数。

    args_name : 参数名称，用于将参数值传递给函数
    args_value : 参数值 (列表、字典列表、元组、字典元组)
    @pytest.mark.parametrize(args_name,args_value)
    def test_case05(self,args_name): # !args_name必须名称相同
       ...
    # 输出的测试用例结果中可包含输入的参数值
    
    args_name 用法：
        单参数传入 : 对a,b,c分别执行三次用例
        1、@pytest.mark.parametrize('caseinfo',['a','b','c'])
        多参数传入 : 对 a,1 , b,2 , c,3 分别执行三次用例 
        2、@pytest.mark.parametrize('arg1,arg2',[['a',1],['b',2],['c',3]])

2、yaml文件测试用例读写、封装
    1、扩展名：yaml、yml
    2、支持#注释
    3、通过缩进表示层级关系
    4、支持区分大小写
    用途：
        1、用于配置文件（yaml/ini）。exam：全局环境变量
        2、编写接口自动化测试用例。
    
    数据组成：
        1、map对象。键值对。key:( )value 
            1.1、str单值。 value为单值。 key: value  # 注意有空格
            2.1、list数组值(可层层嵌套)。值可采用list形式输入多个键值对。  fatherkey:
                                                                        - key: value1
                                                                        - key: value2 ...
 
        
        
        

```# pytest_test
