class Article:
    
    def __init__(self, index, lang, text):
        self.index = index
        self.lang = lang
        self.text = text
        self.frequency = []
        
    def normalize(self):
        dic = {}
        counter = 0
            
        for i in range(97, 123):
            dic[chr(i)] = 0

        for char in self.text.lower():
            if ord(char) > 96 and ord(char) < 123:
                dic[char] += 1
                counter += 1
    
        lst = []
        for key, value in dic.items():
            lst.append((key, value))
                
        for elem in sorted(lst, key=lambda x: x[0]):
            self.frequency.append(elem[1]/float(counter))
            