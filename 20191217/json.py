"""

json处理

Version:1.0
Author:chaishuai

"""

import json

def main():
    user = {'uid':'1', 'name':'老张'}
    # 将json写入文件
    with open('./20191217/json.txt', 'w', encoding='utf-8') as fs1:
        json.dump(user, fs1, ensure_ascii=False)
    # 从文件中读取json反序列化成对象
    with open('./20191217/json.txt', 'r', encoding='utf-8') as fs2:
        u1 = json.load(fs2)
        print(u1)

    # 将Python对象按照JSON格式序列化成字符串
    u2 = json.dumps(user, ensure_ascii=False)
    print(u2)
    # 将JSON字符串反序列化城对象
    u3 = json.loads(u2)
    print(u3)
if __name__ == '__main__':
    main()
