import requests

username = os.environ["HAO4K_USERNAME"]
password = os.environ["HAO4K_PASSWORD"]

loginurl = 'https://www.hao4k.cn/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LT3b2&inajax=1'
signinurl = 'https://www.hao4k.cn/plugin.php?id=k_misign:sign&operation=qiandao&formhash=25c49317&format=empty'
form_data = {
    'formhash': "03909abf",
    'referer': "https://www.hao4k.cn/",
    'username': username,
    'password': password,
    'questionid': "0",
    'answer': ""
}

def run(form_data):
    s = requests.Session()
    response = s.post(loginurl)
    print(response.status_code)
    if response.status_code == 200:
        signin_resp = s.get(signinurl)
        print(signin_resp.status_code)

if __name__ == "__main__":
    run(form_data)
    print("run once.")
