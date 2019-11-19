## day12重点总结



#### 一 创建一个最简单的web应用程序

```python

import socket

sock=socket.socket()
sock.bind(("127.0.0.1",8800))
sock.listen(5)

while 1:
    conn,addr=sock.accept()
    data=conn.recv(1024)
    print("data",data)
    with open("jd.html","rb") as f:
        data=f.read()
    conn.send(b"HTTP/1.1 200 OK\r\n\r\n"+data)




```

#### 二 http协议

URL: 协议/IP:端口/路径?GET参数

1 基于请求响应

2 请求协议格式

```python
 '''
		  GET URL路径?a=1&b=2 HTTP  # 请求首行
		  user-agent: XXX   # 请求头   
		  accept-encoding: gzip, deflate, br   # 请求头
		  
		  a=1&b=2           # 请求体 
'''
		  注意:只有post请求方式才有请求体

```

3 响应协议格式

```python
'''
		  HTTP/1.1 200 OK   # 响应首行
		  content-length: 28297   # 响应头   
		  date: Sun, 07 Jul 2019 03:29:14 GMT
		  
		  helloyuan           # 响应体 
'''


```

#### 三 HTML

3.1 html结构

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>周末三期</title>
    <link rel="icon" href="https://www.jd.com/favicon.ico">
</head>
<body>

</body>
</html>


```

3.2 html标签格式

<开始标签 属性='属性值'  属性2='属性值'>标签体</结束标签>

<标签 属性='属性值'  属性2='属性值'>



3.3 基本标签

```python
# 块级标签: 独占一行,可设置长宽
h1-h6
p
hr
div
ul
ol
li
# 内联标签:只占内容本身,不可以设置长宽
b 
strong
span
em
a
img
input
select


```

3.4 常用标签

```python
<img src="./timg.jpg" alt="美女" title="大美女" width="200" height="300">
<a href="https://www.cnblogs.com/">点我啊!</a>
<ul>
    <li>123</li>
    <li>234</li>
    <li>345</li>
</ul>
<ol>
    <li>111</li>
    <li>222</li>
    <li>333</li>
</ol>

<dl>
    <dt>河北省</dt>
    <dd>保定市</dd>
    <dd>石家庄市</dd>
    <dd>廊坊市</dd>
</dl>

<table border="1" cellpadding="20" cellspacing="5">
     <thead>
           <tr>
               <th>姓名</th>
               <th>年龄</th>
               <th>薪水</th>
               <th>部门</th>
           </tr>
     </thead>
     <tbody>
           <tr>
               <td colspan="2">123</td>
               <td>2000</td>
               <td rowspan="3">销售</td>
           </tr>
           <tr>
               <td>张三</td>
               <td>23</td>
               <td>2000</td>
           </tr>
           <tr>
               <td>张三</td>
               <td>23</td>
               <td>2000</td>

           </tr>
     </tbody>
</table>


```

3.5 form表单标签

```python
#  input系列

#  select

# textarea

# label

<form action="http://127.0.0.1:8800" method="post">
    <p>
    <label for="user">姓名</label> <input id="user" type="text" name="user" placeholder="用户名">     </p>
    <p>密码 <input type="password" name="pwd" ></p>
    <p>爱好 <input type="checkbox" name="hobby" value="lanqiu" checked> 篮球  
    <input type="checkbox"  name="hobby" value="zuqiu">足球 
    <input type="checkbox"  name="hobby" value="shuangseqiu">双色球   
    </p>
    <p>性别 <input type="radio" name="gender" value="1" checked>男 
            <input type="radio" name="gender" value="2"> 女  
            <input type="radio" name="gender">其他
    </p>
    <p><input type="hidden" name="token" value="12312sad221312sa"></p>
    <p><input type="reset"></p>
    <p><input type="file"></p>
      <p>
            籍贯
        <select name="pro" id="" size="3" multiple>
            <option value="hebei">河北省</option>
            <option value="henan" selected>河南省</option>
            <option value="hsandong">山东省</option>
        </select>
      </p>
    <p>
        <textarea name="jianjie"  cols="30" rows="10" placeholder="个人简介"></textarea>
    </p>    
    <input type="submit">
</form>



注意:
      1  <input type="checkbox" name="hobby" value="lanqiu" checked> 篮球,其中checked是默认选中的意思,和select标签中的<option value="henan" selected>河南省</option>的selected等效.
      2  action:form表单发送请求的服务器URL;method决定请求方式get还是post
      3  总结:当用户点击submit按钮时,浏览器会将该form表单中的有效控件的name属性值为键,以value属性值为值组成键值对以application/x-www-form-urlencoded 格式发给服务器.  
      4  向服务器发送请求的方式:
         *** 1 浏览器地址栏输入URL发送请求(默认GET请求)
         *** 2 form表单发请求(get post)
         *** 3 a标签






```



相关博客:

​        1 HTML:<https://www.cnblogs.com/yuanchenqi/articles/6835654.html>

​        2 CSS:<https://www.cnblogs.com/yuanchenqi/articles/6856399.html>

​        3 JS <https://www.cnblogs.com/yuanchenqi/articles/6893904.html>

​       4 Jquery<https://www.cnblogs.com/yuanchenqi/articles/6936986.html>



今日作业:

​     1 博客中的两个表格

​     2 结合服务器程序,重现注册页面

​     3 预习CSS









