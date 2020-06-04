from aip import AipSpeech
import os

""" 你的 APPID AK SK """
APP_ID = '16007034'
API_KEY = '9cVZDkCrl0sZP3wpQlMeqZq2'
SECRET_KEY = 'lGTYdBrcomGUAgfPCt2jrYO9Rg68IMAB'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def change_to_mp3(content='已退出此模式', turn=1, mp3_name='17k'):
    result = client.synthesis(content, 'zh', 1, {
        'vol': 5, 'per': 0
    })
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('exit.mp3', 'wb') as f:
            f.write(result)
        if turn:
            os.system(
                "gnome-terminal -e 'ffmpeg -y  -i auido.mp3  -acodec pcm_s16le -f s16le -ac 1 -ar 16000 %s.pcm '" % (
                    mp3_name))


if __name__ == '__main__':
    change_to_mp3()
