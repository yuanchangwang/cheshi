import struct
# pack   把任意长度的数字转化成具有固定长度的4个字节的值,组成字节流
# unpack 把4个字节的值恢复成原有数据,最终返回的是一个元组

# i => int 我要转化的这个数据类型是整型
res = struct.pack("i",130000000)
print(res)
print(len(res))

res = struct.unpack("i",res)
print(res)
 







