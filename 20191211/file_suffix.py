"""

返回一个给定文件名的后缀

Version:1.0
Author:chaishuai

"""

def get_file_suffix(file_name):
    if file_name is None or file_name == '':
        return False
    file_name_r = file_name[::-1]
    file_name_suffix_r_index = file_name_r.find('.')
    if file_name_suffix_r_index == -1:
        return False
    file_name_suffix = file_name_r[:file_name_suffix_r_index][::-1]
    return file_name_suffix

if __name__ == '__main__':
    file_name = input('请输入一个文件的文件名:')
    print(get_file_suffix(file_name))

