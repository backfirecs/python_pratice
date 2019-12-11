"""

打印杨辉三角

Version:1.0
Author:chaishuai

"""

def main():
   line_num = int(input('请输入行数:'))
   last_line_list = [];
   for x in range(1, line_num + 1):
       cur_line_list = list(range(1, x + 1))
       cur_line_list[0] = 1
       cur_line_list[x - 1] = 1
       line_str = ''
       for value in cur_line_list:
           line_str += str(value)
       print(line_str)
       last_line_list = cur_line_list

if __name__ == '__main__':
    main()