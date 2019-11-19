HTML

CSS

JS(javascript)

JS: 

   1  ECMAScipt(变量,数据类型 函数,...)  

   2  BOM: browser object model 

   3  DOM:document object model 



### ECMAScipt

1 变量

2 数据类型

3 运算符

```
++        -- 
```



4 流程控制语句

5 函数



new 类型(参数)

类(参数)







DOM

节点对象:

document: 根节点

element:  标签节点





DOM:

​      (1) 查找标签

​                <1>  直接查找                

```js
            document.getElementById(“idname”)        # 返回值标签对象(dom对象)
            document.getElementsByTagName(“tagname”) # 返回数组  [dom对象1,...]
            document.getElementsByName(“name”)       # 返回数组  [dom对象1,...]
            document.getElementsByClassName(“name”)  # 返回数组  [dom对象1,...]
```

​      <2> 导航查找

```
dom对象.parentElement           // 父节点标签元素

dom对象.children                // 所有子标签

dom对象.firstElementChild       // 第一个子标签元素

dom对象.lastElementChild        // 最后一个子标签元素

dom对象.nextElementtSibling     // 下一个兄弟标签元素

dom对象.previousElementSibling  // 上一个兄弟标签元素
```



 (2) 操作标签(操作dom)

1、获取文本节点的值： innerHTML

2  dom的属性操作

3 dom的value操作

4 dom的class属性操作

5 改变css样式：`document.getElementById(``"p2"``).style.color``=``"blue"``;`

6 节点操作: 

   **创建节点：**

 ```
createElement(标签名)
 ```



