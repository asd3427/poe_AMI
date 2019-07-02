import re
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
import win32clipboard
class Poe_AM:

    def __init__(self):
        pass

    @staticmethod
    def open_data():
        with open('29174_poe2.txt', 'r', encoding='utf-8') as f:
            data = f.read().split('\n')
            return data

    def recmop(self):
        """
        :param input_text: 需要匹配的字
        :return:
        """

        data = self.open_data()
        win32clipboard.OpenClipboard()
        copy_data= win32clipboard.GetClipboardData()
        win32clipboard.CloseClipboard()
        copy_data=copy_data.replace('-','').split('\n')
        print(copy_data)
        i = 0

        for input_text in copy_data:
            if input_text is not "":
                #print(input_text)
                r= fuzz.SequenceMatcher(input_text,data)
                print(r.b)
a = Poe_AM().recmop()


