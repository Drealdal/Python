这个是在python的数据域json的字符串之间进行转换的工具

load(_str) 读取一个json字符串

dump() 返回内部数据的json字符串

loadJson(_file) 从文件中读取json字符串并解析,_file 需要读取的文件的路径

dumpJson(_file) 将内部数据转换成json字符串之后输出到文件_file

dumpDict() 将内部数据转换成python中的Dict数据结构，实现的是对所有数据的深拷贝

loadDict(_dict) 将_dict的数据读入

update(_dict) 使用_dict中的数据更新内部存储的数据

另外支持使用[] 进行数据的get和set
