# -*- coding: utf-8 -*-

from pyaudio import PyAudio, paInt16
import numpy as np
import wave
from aip import AipSpeech
import re


class recoder:
    NUM_SAMPLES = 2000  # pyaudio内置缓冲大小
    SAMPLING_RATE = 16000  # 取样频率
    LEVEL = 500  # 声音保存的阈值
    COUNT_NUM = 20  # NUM_SAMPLES个取样之内出现COUNT_NUM个大于LEVEL的取样则记录声音
    SAVE_LENGTH = 8  # 声音记录的最小长度：SAVE_LENGTH * NUM_SAMPLES 个取样
    TIME_COUNT = 100  # 录音时间，单位s

    Voice_String = []

    def savewav(self, filename):
        wf = wave.open(filename, 'wb')
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(self.SAMPLING_RATE)
        wf.writeframes(np.array(self.Voice_String).tostring())
        # wf.writeframes(self.Voice_String.decode())
        wf.close()

    def recoder(self):
        pa = PyAudio()
        stream = pa.open(format=paInt16, channels=1, rate=self.SAMPLING_RATE, input=True,
                         frames_per_buffer=self.NUM_SAMPLES)
        save_count = 0
        save_buffer = []
        time_count = self.TIME_COUNT

        while True:
            time_count -= 1

            # 读入NUM_SAMPLES个取样
            string_audio_data = stream.read(self.NUM_SAMPLES)
            # 将读入的数据转换为数组
            audio_data = np.fromstring(string_audio_data, dtype=np.short)
            # 计算大于LEVEL的取样的个数
            large_sample_count = np.sum(audio_data > self.LEVEL)
            print('.', end='')
            # 如果个数大于COUNT_NUM，则至少保存SAVE_LENGTH个块
            if large_sample_count > self.COUNT_NUM:
                save_count = self.SAVE_LENGTH
            else:
                save_count -= 1

            if save_count < 0:
                save_count = 0

            if save_count > 0:
                # 将要保存的数据存放到save_buffer中
                save_buffer.append(string_audio_data)
            else:
                # 将save_buffer中的数据写入WAV文件，WAV文件的文件名是保存的时刻

                if len(save_buffer) > 0:
                    self.Voice_String = save_buffer
                    save_buffer = []
                    print('')
                    print("Recode a piece of  voice successfully!")
                    return True
            if time_count == 0:
                if len(save_buffer) > 0:
                    self.Voice_String = save_buffer
                    save_buffer = []
                    print('')
                    print("Recode a piece of  voice successfully!")
                    return True
                else:
                    return False

    def get_file_content(self, filename):
        with open(filename, 'rb') as fp:
            return fp.read()

    def identify(self):
        APP_ID = '11594055'
        API_KEY = 'FKQrE66hjEgSmUsdVwQ7ctaL'
        SECRET_KEY = 'jOF0FgcIAVuV88PRAfGGzW7q8vdMGc1c'

        client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

        res = client.asr(self.get_file_content('test.wav'), 'wav', 16000, {
            'dev_pid': 1737,
        })
        print(res['result'])
        return res['result'][0]

    def sort(self, message):

        pattern = r'.*drug [a|b|c].*'
        res = re.match(pattern, message)
        if res != None:
            if message.find('a') != -1:
                return 'drug A'
            elif message.find('b') != -1:
                return 'drug B'
            else:
                return 'drug C'
        else:
            print('can not identify your instruction')
            return None


if __name__ == "__main__":
    r = recoder()
    str = input('please tap r to start record ： ')
    count = 0
    while True:
        if str == 'r':
            r.recoder()
            r.savewav("test.wav")
            message = r.identify()
            print(message)
            res = r.sort(message)
            if res:
                print('succeed')
                exit(0)
            else:
                count += 1
                str = input('please tap r to start record ： ')
