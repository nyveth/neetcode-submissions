from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Массив ответов
        answer = defaultdict(list)

        #Цикл по массиву слов
        for word in strs:
            sort = "".join(sorted(word))
            answer[sort].append(word)

        return list(answer.values())
