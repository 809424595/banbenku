import requests

header = {
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
}
url1 = 'http://114.96.100.79:5674/zentao/user-login.html'
data1 = {
    'account': 'admin',
    'password': '123456',
    'passwordStrength': '0',
    'referer': '%2Fzentao%2F',
    'verifyRand': '30397001',
    'keepLogin': '0'}
req = requests.post(url1, data=data1, headers=header)
cookie = req.cookies