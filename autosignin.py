import requests
import os
import re


username = os.environ["HAO4K_USERNAME"]
password = os.environ["HAO4K_PASSWORD"]

bot_token = os.environ["TG_BOT_TOKEN"]
chat_id = os.environ["TG_CHAT_ID"]
api_url = "https://api.telegram.org/bot%s/sendMessage" % (bot_token)
send_message = "Server ERROR"
params = {
    'chat_id': chat_id,
    'text': send_message
}

user_url = "https://www.hao4k.cn/member.php?mod=logging&action=login&phonelogin=no"
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}
base_url = "https://www.hao4k.cn/"
signin_url = "https://www.hao4k.cn/plugin.php?id=k_misign:sign&operation=qiandao&formhash={formhash}&format=empty"
form_data = {
    'formhash': "",
    'referer': "https://www.hao4k.cn/",
    'username': username,
    'password': password,
    'questionid': "0",
    'answer': ""
}
inajax = '&inajax=1'

def run(form_data):
    s = requests.Session()
    user_resp = s.get(user_url, headers=headers)
    login_text = re.findall('action="(.*?)"', user_resp.text)
    for loginhash in login_text:
        if 'loginhash' in loginhash:
            login_url = base_url + loginhash +inajax
            login_url =login_url.replace("amp;", "")
            print(login_url)
    form_text =re.search('formhash=(.*?)\'', user_resp.text)
    print(form_text.group(1))
    form_data['formhash'] = form_text.group(1)
    print(form_data)

    login_resp = s.post(login_url, data=form_data, headers=headers)
    test_resp = s.get('https://www.hao4k.cn/k_misign-sign.html', headers=headers)
    if username in test_resp.text:
        print('Login succeed!')
    else:
        return('Login failed!')
    signin_text = re.search('formhash=(.*?)"', test_resp.text)
    signin_resp = s.get(signin_url.format(formhash=signin_text.group(1)), headers=headers)
    test_resp = s.get('https://www.hao4k.cn/k_misign-sign.html', headers=headers)
    if '您的签到排名' in test_resp.text:
        print('Signin succeed!')
    else:
        return('Signin failed!')

if __name__ == "__main__":
    signin_log = run(form_data)
    if signin_log is None:
        send_message = "hao4K每日签到成功！"
        print('Signin automaticlly!')
    else:
        send_message = signin_log
        print(signin_log)
    r = requests.get(api_url, params=params)
    if r.status_code == requests.codes.ok:
        print("签到消息已发送至我的Telegram Bot。")
    else:
        print(r.status_code)
