## day13

上周回顾



基本标签:    h1-h6   p    b strong   em  hr   br

常用标签:    img  a  ul ol  li  table  

form表单标签:  input:   type=text,password,checkbox,radio,submit,reset,hidden,file

​                             select :  option

​                             textarea



总结:  发送请求的形式:

​          (1) 地址栏请求   (GET请求)

​          (2) a标签    (GET请求)

​          (3) form标签  (get/post)





CSS:

​     功能:  1 渲染样式  2 定位布局

CSS语法:  

```css
 selector {
              color: red;
              backgroundColor: green;
              property: value
              }
```

​    

css的优先级：

​     行内式：1000

​     id选择器 ：  100

​    class选择器： 10

​    标签选择器：1

​    bug： ！important；

css样式继承

#### css的属性操作

（1） 文本操作



布局障碍:如何能将多个可设置长宽的元素在一行显示!

解决:(1) display:inline-block  (2)  float





float的定位规则:

​     假如某个div元素A是浮动的，如果A元素上一个元素也是浮动的，那么A元素会跟随在上一个元素的后边(如果一行放不下这两个元素，那么A元素会被挤到下一行)；如果A元素上一个元素是标准流中的元素，那么A的相对垂直位置不会改变，也就是说A的顶部总是和上一个元素的底部对齐。此外，浮动的框之后的block元素元素会认为这个框不存在，但其中的文本依然会为这个元素让出位置。 浮动的框之后的inline元素，会为这个框空出位置，然后按顺序排列。





position:  static/absolute/relative/fixed



定位:

​       固定定位:

​                  1 完全脱离文档流

​                   2 以屏幕参照物

​      相对定位:

​                   1 不脱离文档流

​                    2 以自己所在原位置为参照物                   

​       绝对定位:

​                   1 脱离文档流

​                   2 按已经定位了的父元素为参照物,如果父元素没有定位，一直向外延申，直到最外层标签



绝对定位+相对定位使用布局





   

