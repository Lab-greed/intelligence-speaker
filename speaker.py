#!/usr/bin/python3
import pyrec  # 录音函数文件
import wav2pcm  # wav转换pcm 函数文件
import baidu_ai  # 语音合成函数,语音识别函数 文件
import playmp3  # 播放mp3 函数 文件
import FAQ
import tuling
import sizhi

pyrec.rec("1.wav")  # 录音并生成wav文件,使用方式传入文件名

pcm_file = wav2pcm.wav_to_pcm("1.wav")  # 将wav文件 转换成pcm文件 返回 pcm的文件名

res_str = baidu_ai.audio_to_text(pcm_file) # 将转换后的pcm音频文件识别成 文字 res_str

ter=sizhi.speak(res_str)
Q_str = str (ter)
synth_file = baidu_ai.text_to_audio(Q_str)
playmp3.play_mp3(synth_file)