from aip import AipSpeech
import os

""" 你的 APPID AK SK """
APP_ID = '16007034'
API_KEY = '9cVZDkCrl0sZP3wpQlMeqZq2'
SECRET_KEY = 'lGTYdBrcomGUAgfPCt2jrYO9Rg68IMAB'
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def change_to_mp3(content='已到达,开始为您进行介绍。计算机软件与理论主要研究软件设计、开发、维护和使用过程中涉及的软件理论、方法和技术，探讨计算机科学与技术发展的理论基础。计算机系统结构研究计算机硬件与软件的功能分配、软硬件界面的划分、计算机硬件结构、组成与实现方法与技术。计算机应用技术研究应用计算机到各个领域的原理、方法和技术，所涉及的研究内容非常广泛。', turn=1, mp3_name='17k'):
    result = client.synthesis(content, 'zh', 1, {
        'vol': 5, 'per': 0
    })
    # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
    if not isinstance(result, dict):
        with open('museum.mp3', 'wb') as f:
            f.write(result)
        if turn:
            os.system(
                "gnome-terminal -e 'ffmpeg -y  -i auido.mp3  -acodec pcm_s16le -f s16le -ac 1 -ar 16000 %s.pcm '" % (
                    mp3_name))


if __name__ == '__main__':
    change_to_mp3()
