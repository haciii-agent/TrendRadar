import time
import hmac
import hashlib
import base64
import urllib.parse
import requests

# 你的钉钉配置
access_token = "3eb30f8d052e349dabf404d46d173ce3725a01434a21f4754c7ccc1bd1da8b80"
secret = "SECc00e1486253015c8048903db9dbdb4c3e8b1a331212bd2859c232ff16e059e33"

# 生成签名
timestamp = str(round(time.time() * 1000))
secret_enc = secret.encode('utf-8')
string_to_sign = '{}\n{}'.format(timestamp, secret)
string_to_sign_enc = string_to_sign.encode('utf-8')
hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))

# 构造请求URL
url = f"https://oapi.dingtalk.com/robot/send?access_token={access_token}&timestamp={timestamp}&sign={sign}"

# 测试消息（包含关键词「热点」）
headers = {'Content-Type': 'application/json'}
data = {
    "msgtype": "text",
    "text": {
        "content": "【热点测试】这是一条来自TrendRadar的测试消息"
    }
}

# 发送请求
response = requests.post(url, headers=headers, json=data)
print("响应结果:", response.json())
