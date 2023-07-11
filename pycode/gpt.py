from urllib.parse import unquote

import zhipuai

zhipuai.api_key = "389196bf710b29d5cde59d62a59df45e.hDHNPlLlh3EgCWA1"

with open('/home/duanwei/TinyWebServer-master/root/welcome.html', 'r') as file:
    content = file.read()

with open('/home/duanwei/TinyWebServer-master/root/response.txt', 'r') as file:
    question = file.read()
question = question[8:]
# question = question.encode('GBK').decode('UTF-8')
question = unquote(question)
# question = "你是谁"
# 查找并替换字符
search_char = '回答'
response = zhipuai.model_api.sse_invoke(
    model="chatglm_lite",
    prompt=[
        # {"role": "user", "content": "你好"},
        # {"role": "assistant", "content": "我是人工智能助手"},
        # {"role": "user", "content": "你叫什么名字"},
        # {"role": "assistant", "content": "我叫chatGLM"},
        {"role": "user", "content": question},
    ],
    temperature=0.95,
    top_p=0.7,
)
answer = "回答"
for event in response.events():
    if event.event == "add":
        # print(event.data,end='')
        answer += event.data
    elif event.event == "error" or event.event == "interrupted":
        # print(event.data,end='')
        answer += event.date
    elif event.event == "finish":
        # print(event.data,end='',fp = 'txt')
        answer += event.data
        # print(event.meta,end='')
    else:
        # print(event.data,end='')
        answer += event.data

# replace_char = 'b'
new_content = content.replace(search_char, answer)

# 将替换后的内容写回文件
with open('/home/duanwei/TinyWebServer-master/root/reponse.html', 'w') as file:
    file.write(new_content)