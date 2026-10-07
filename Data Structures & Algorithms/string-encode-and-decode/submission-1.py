class Solution:

    def encode(self, strs: List[str]) -> str:
        change_words = []
        for word in strs:
            change_words.append(str(len(word)) + "#" + word)

        encoded_string = "".join(change_words)
        return encoded_string
    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i = 0
        while i < len(s):
            #  Поиск индекса числа в массиве обозначающего длину строки
            j = s.find("#", i)
            k = int(s[i:j])
            decoded_strs.append(s[j + 1 : j + 1 + k])
            i = j + 1 + k
        return decoded_strs