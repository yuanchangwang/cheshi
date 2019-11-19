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

BOM:

​       window对象

​              window.alert()

​              window.confirm()

​              window.prompt()

​              window.open()

​            ID= window.setInterval(function(){

​             },1000)

​            window.clearInterval(ID)

DOM

节点对象:

​       document: 根节点

​       element:  标签节点





DOM:

###       (1) 查找标签

​                <1>  直接查找                

```js
            document.getElementById(“idname”)        # 返回值标签对象(dom对象)
            document.getElementsByTagName(“tagname”) # 返回数组  [dom对象1,...]
            document.getElementsByName(“name”)       # 返回数组  [dom对象1,...]
            document.getElementsByClassName(“name”)  # 返回数组  [dom对象1,...]
```

​               <2> 导航查找

```
dom对象.parentElement           // 父节点标签元素

dom对象.children                // 所有子标签

dom对象.firstElementChild       // 第一个子标签元素

dom对象.lastElementChild        // 最后一个子标签元素

dom对象.nextElementtSibling     // 下一个兄弟标签元素

dom对象.previousElementSibling  // 上一个兄弟标签元素
```

###   操作标签(操作dom)

1、获取文本节点的值： innerHTML

2  dom的属性操作

```
dom.setAttribute("id","123")
dom.getAttribute("id")
dom.removeAttribute("id")
```

3 dom的value操作

```
# 针对 input select rextarea三个标签

dom.value
dom.vaue=""
```

4 dom的class属性操作

```js
<div class='c1'>123</div>
dom.classlist.add("c2")
dom.classlist.remove("c2")
```

5 改变css样式：`document.getElementById("p2").style.color="blue";`

6 节点操作: 

   **创建节点：**

 ```js
// 创建节点
document.createElement(标签名)
// 添加节点
parent.appendChild(添加节点)
// 删除节点
parent.removeChild(删除节点)
// 替换节点
parent.replacewith("新节点"，"旧节点")
 ```



### 作业

1 tab切换





### 今日内容



### dom的事件







### jquery库





Jquery==$

```js
$(选择器).操作方法()

         jquery对象转成dom对象
$(".c1")---------------------->$(".c1")[0]
                                   
                                   dom对象转换成jquery对象
dom=document.getElementbyId("i1")-------------------------->$(dom)
```

#### 选择器

```js
// 基本选择器

// 组合选择器‘

// 筛选器

// 属性选择器

// 表单选择器


```

```js
// 导航查找
 查找子标签：         $("div").children(".test")      $("div").find(".test")  
                               
 向下查找兄弟标签：    $(".test").next()               $(".test").nextAll()     
                     $(".test").nextUntil() 
                           
 向上查找兄弟标签：    $("div").prev()                  $("div").prevAll()       
                     $("div").prevUntil()   
 查找所有兄弟标签：    $("div").siblings()  
              
 查找父标签：         $(".test").parent()              $(".test").parents()     
                     $(".test").parentUntil()
```

#### 操作方法

事件绑定

```js
  /*
                  jquery对象.事件(funcition(){})

      */
```

操作方法

```js
// 1 操作文本
       // 取本文
       $("").html().
       // 赋值文本
       $("").html(参数).
// 2 属性操作
       $("#i1").attr("class")
       $("#i1").attr("class","c2")
       $("#i1").removeAttr("id")
// 3 class操作
       $("#i1").addClass("c3")
       $("#i1").removeClass("c3")   
// 4 value操作
        $(".c1").val()
        $(".c1").val("alex")

// 5 css操作
       $().css("样式属性","值")
// 6 节点操作 ******
// 创建节点:  $("标签名"),比如 $("<p>")
// 添加节点: 
          $("父亲节点").append（子节点或者子节点字符串）
          var $img=$("<img src=''>");
        $img.attr("src","https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2121206715,2955288754&fm=27&gp=0.jpg")
        // $(".c1").append($img)
        // 方式2
        // $(".c1").append("<img    src='https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=2121206715,2955288754&fm=27&gp=0.jpg'>")
        // 方式3
        // $img.appendTo(".c1");
        // 方式4
         $(".c3:first").after($img)
// 替换节点
$("被替换节点").replaceWith("替换节点或者替换节点字符串")
// 删除系欸但
$("删除节点").remove()

```













### bootstrap插件