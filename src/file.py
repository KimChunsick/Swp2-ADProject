
# TODO: pickle 사용 고려
class File:

    def __init__(self, path):
        self.path = path
        self.result = dict()
        self.map = map

        try:
            file = open(path, 'r')
        except Exception as error:
            print(error)
            file = open(path, 'w')
            file.write('')
        lines = file.readlines()
        file.close()

        for text in lines:
            self.process_data(text)

    def process_data(self, text):
        result_text = text.rstrip().split("','")
        self.result[result_text[0]] = result_text[1]

    def save_text(self, text, path):
        try:
            file = open(path, 'a')
        except Exception as error:
            print(error)
            file = open(path, 'w')
            file.write('')
        file.write(text)
        file.close()
        self.process_data(text)

    def save_dict(self, path, mode, dictionary):
        path = self.path if path == '' else path
        try:
            file = open(path, mode)
        except Exception as error:
            print(error)
            file = open(path, 'w')
            file.write('')

        lines = ""
        for k, v in dictionary.items():
            lines += "{0}','{1}\n".format(k, v)
        file.write(lines)
        file.close()

    def remove(self, key):
        del self.result[key]
        self.save_dict(self.path, 'w', self.result)
