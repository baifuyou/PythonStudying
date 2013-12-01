Properties
===========

>Properties是一个Python实现的key-value工具。properties文件的格式为:

	key1 = value1
	key2 = value2

‘=’两边可以有0或者多个空格；‘=’可以用‘：’代替。

>1.  def getProperties(path) 返回一个Properties示例。    
	如果path指向一个文件，该方法将从里面读取数据，用于初始化Properties实例。   
	如果该文件不符合properties语法规范，将产生不可预知的错误。     
	如果path指向一个目录，将会抛出IOError错误。    
	如果该path不指向任何目录或者文件，将返回一个空的Properties实例。     
	该path将会作为store方法的默认path。    
>2.  def getData() 返回一个存储了properties数据的字典
>3.  def setData(self, fData) 将fData设置成实例的properties数据
>4.	def store(self, path) 将实例的properties数据保存到目标paht，如果
	path没有指定，或者指定为‘#’，将保存到默认path。
