#coding=utf-8
import execjs
import requests

js=open('music163.js','r',encoding='utf8').read()
ctx=execjs.compile(js)
result=ctx.call('start')
url='https://music.163.com/weapi/v1/resource/comments/R_SO_4_501928179?csrf_token='
headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
data={
    'params':result['encText'],
    'encSecKey':result['encSecKey']
}
list=[]
response =requests.post(url,headers=headers,data=data).json()
comments=response['comments']
for i in comments:
    content=i['content'].replace("\n", " ")
    list.append(content)
print(list)























