----------------python基础：变量------------------
变量定义
	不需要提前申明，变量在第一次赋值的时候会自动申明，变量只有被创建和赋值后才能使用。
变量动态类型
	python解析器会根据语法和操作数决定对象的类型
变量赋值过程
	python中的赋值，不是正真意义上修改内存的值，而是将变量和在内存中存在的值做一个绑定，这个就是引用
	引用的优缺点：
		好处：节省内存，多个变量可以指向同一个地址
		缺点：如果修改变量的变量值在内存中不存在需要重新申请内存，绑定变量名和地址，降低了执行效率

--------------python基础：幕后----------------------
python解析器：
	1、python解析器是c语言实现的
	2、python变量的赋值和释放需要申请和释放内存
	3、python这一系列对应于解析器来说是对应c语言的malloc和free操作
	4、malloc和free的操作，对于linux系统来说就是系统调用，程序会在内核太和用户态进行频繁切换，解析器执行效率低

-------------python的内存管理机制-------------------
python引入内存池机制和pyobject_malloc来优化频繁的小内存块申请和释放
1、内存池
	预先在内存中申请一定数量的，大小相等的内存块，申请内存较小（0～256字节），从内存池中分配内存，如果内存不够，重新申请新的内存空间，这样做能够减小内存碎片
2、pyobject_malloc
	如果申请的内存空间小于256字节，python会在内存池中申请内存空间，大于256字节则会直接执行malloc申请空间

--------------变量赋值----------------------------------
多元赋值
	x,str1 = 1,"hello"

---------------------数据类型---------------------------
数字：a = 10,b = True,c = 3.14,com = 3 + 4j
字符串：str1 = “hello world”
列表：list_ = [1,2,3,4,5]
元组：tuple_ = (1,2,3,4,5)
字典：dict_ = {1:'a',2:'b',3:'c'}
none：空值
常量：大写字母组成的变量(可以修改，只是习惯理解为常量)

type 类可以查看变量的类型
	type(变量)


---------------------语法--------------------------------
缩进：
	python使用缩进来控制代码和逻辑
	同一逻辑层次的语句必须有相同的缩进
	逻辑控制：
		a = 10
		if(a > 10):
			print("a>10")
			print(a)
		else:
			print("a < 10")
	代码块控制
		def test_func():
			print("this is test")
		class test:
			def __init__(self):
				print("init")














