# -*- coding: utf-8 -*-
# @Author: Qilong Pan
# @Date:   2018-12-01 11:10:29
# @Last Modified by:   Qilong Pan
# @Last Modified time: 2018-12-01 11:10:52

class IMM(object):
    def __init__(self, dic_path):
        self.dictionary = set();
        self.maximum = 0
        # 读取词典
        with open(dic_path, 'r', encoding="utf8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                self.dictionary.add(line)
                self.maximum = max(self.maximum, len(line))
    
    def cut(self, text):
        result = []
        index = len(text)
        while index > 0:
            word = None
            for size in range(self.maximum, 0, -1):
                if index - size < 0:
                    continue
                piece = text[(index - size):index]
                if piece in self.dictionary:
                    word = piece
                    result.append(word)
                    index -= size
                    break
 
            if word is None:
                index -= 1
        return result[::-1]
    
def main():
    text = "南京市长江大桥"
    tokenizer = IMM('./data/imm_dic.utf8')
    print(tokenizer.cut(text))

main()