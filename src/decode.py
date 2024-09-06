import base64
import bz2
import zlib
import lzma
import gzip
from datetime import datetime
import re

# from Crypto.Cipher import AES
# from cryptography.fernet import Fernet
# from Crypto.Cipher import ChaCha20
# 获取当前日期和时间
now = datetime.now()
count = 0
reversal = False
base_type = "b64decode"
decode_func = {
    "b85decode": base64.b85decode,
    "b64decode": base64.b64decode,
    "b32decode": base64.b32decode,
    "b16decode": base64.b16decode,
}
# 将日期和时间格式化为字符串
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")


def try_decode_reversal(data):
    if reversal:
        print("发现 [::-1] ，正在反制")
        return data[::-1]
    else:
        return data


def try_decompress(data):
    for decompress_func, method_name in [
        (gzip.decompress, "gzip"),
        (bz2.decompress, "bz2"),
        (zlib.decompress, "zlib"),
        (lzma.decompress, "lzma"),
    ]:
        try:
            decompressed_data = decompress_func(data)
            print(f"成功使用 {method_name} 解压")
            # 尝试递归解压
            return try_decompress(decompressed_data)
        except Exception as e:
            pass
    return try_decode(data)


def try_decode_base64(data):
    try:
        decode_data = decode_func[base_type](data)
        print(f"成功使用 {base_type} 解码")
        # 尝试递归解压
        return decode_data
    except Exception as e:
        pass
    return try_decode(data)


def extract_encoded_string(data):
    if type(data) == str:
        data = data.encode('utf-8')
    match = re.findall(br"b?\'([^\']{1000,}?)\'", data) or re.search(br'b?"([^\"]{1000,}?)"', data)
    if match:
        return match
    return None


def try_decode(data):
    try:
        return data.decode()
    except Exception as e:
        return data


def decrypt_nested(data):
    while True:
        global count
        count += 1
        print(f"正在进行第 {count} 层解密")
        new_data = try_decode_reversal(data)
        new_data = try_decode_base64(new_data)
        new_data = try_decompress(new_data)
        if "exec(" in str(new_data):
            # 获取所有编码字符串
            encoded_data_list = extract_encoded_string(new_data)
            if encoded_data_list == None:
                return new_data
            # 循环解密所有编码字符串
            for encoded_data in encoded_data_list:
                new_data = decrypt_nested(encoded_data)
                return new_data
                # 使用字符串替换方法更新 new_data
        else:
            print("无法进一步解密，退出循环")
            return new_data


# 解密嵌套加密数据

# 输出最终解密结果
# print("最终解密结果:")
def process_data(data):
    if isinstance(data, str):
        # 如果是字符串，则编码为字节对象
        byte_data = data.encode('utf-8')
    elif isinstance(data, bytes):
        # 如果已经是字节对象，则直接使用
        byte_data = data
    else:
        # 如果不是字符串也不是字节对象，抛出异常或做其他处理
        raise TypeError("Expected string or bytes-like object")
    return byte_data


final_data = process_data("#") + process_data(formatted_date) + process_data("\n")
with open('./input.py', 'r', encoding='utf-8') as file:
    # 读取文件内容
    content = file.read().strip()
    if "[::-1]" in content:
        reversal = True
    for func in decode_func:
        if func in content:
            base_type = func
    # 打印内容
    for encoded_data in extract_encoded_string(content):
        try:
            final_decrypted_data = decrypt_nested(encoded_data)
            final_data += process_data(final_decrypted_data)
        except Exception as e:
            print(e)

with open("./output.py", 'wb') as f:
    f.write(final_data)
