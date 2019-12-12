"""

打印杨辉三角

Version:1.0
Author:chaishuai

"""

def main():
   line_num = int(input('请输入行数:'))
   last_line_list = [];
   first_line_space_count = (line_num + 1) * 2 // 2 + 1 
   for x in range(1, line_num + 1):
       cur_line_list = list(range(x))
       cur_line_list[0] = 1
       cur_line_list[x - 1] = 1
       line_str = ''
       for index,value in enumerate(cur_line_list):
           if index != 0 and index != (len(cur_line_list)-1) and len(last_line_list) != 0:
               tmp = last_line_list[index] if index > 0 else 0
               value = last_line_list[index-1] + tmp
           line_str += ' ' + str(value)
           cur_line_list[index] = value
       space_count = first_line_space_count - (x - 1)
       line_str = ' ' * space_count + line_str
       print(line_str)
       last_line_list = cur_line_list

if __name__ == '__main__':
    main()