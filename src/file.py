#-*- coding: utf-8 -*-
import os

# TODO: pickle 사용 고려
class File:
    def __init__(self, path):
        self.path = os.getcwd() + path
        self.result = dict()
        self.map = map

        try:
            file = open(self.path, 'r', encoding='UTF8')
        except Exception as error:
            print(error)
            file = open(self.path, 'w', encoding='UTF8')
            file.write('')
        lines = file.readlines()
        file.close()

        for text in lines:
            self.process_data(text)

    # 파일에서 불러온 데이터 가공
    def process_data(self, text):
        try:
            result_text = text.rstrip().split("','")
            self.result[result_text[0]] = result_text[1]
        except Exception as error:
            print(error)

    # 텍스트에 한줄 만 저장할 때
    def save_text(self, text, path=None):
        path = path if path == '' else self.path
        try:
            file = open(path, 'a')
        except Exception as error:
            print(error)
            file = open(path, 'w')
            file.write('')
        file.write("{0}\r\n".format(text))
        file.close()
        self.process_data(text)

    # 기존의 내용을 지우고 dictionary의 값으로 새롭게 저장
    def save_dict(self, dictionary, mode, path=None):
        path = path if path == '' else self.path
        try:
            file = open(path, mode)
        except Exception as error:
            print(error)
            file = open(path, 'w')
            file.write('')

        lines = ""
        for k, v in dictionary.items():
            lines += "{0}','{1}\r\n".format(k, v)
        file.write(lines)
        file.close()

    # 파일에서 값을 지움
    def remove(self, key):
        del self.result[key]
        self.save_dict(self.result, 'w', self.path)
