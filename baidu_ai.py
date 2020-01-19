# baidu_ai.py 文件内容
from aip import AipSpeech


APP_ID ='18308446'
API_KEY='ZCU9ew1M7cxIVnMn7FOSjlAz'
SECRET_KEY ='XUXRO2Pa6oF3Cp0XN4IqrnBzGrhvhcqF'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)


def audio_to_text(pcm_file):
    # 读取文件 , 终于得到了PCM文件
    with open(pcm_file, 'rb') as fp:
        file_context = fp.read()

    # 识别本地文件
    res = client.asr(file_context, 'pcm', 16000, {
        'dev_pid': 1536,
    })


    res_str = res.get("result")[0]

    return res_str


def text_to_audio(res_str):
    synth_file = "synth.mp3"
    synth_context = client.synthesis(res_str, "zh", 1, {
        "vol": 5,
        "spd": 4,
        "pit": 9,
        "per": 4
    })

    with open(synth_file, "wb") as f:
        f.write(synth_context)

    return synth_file