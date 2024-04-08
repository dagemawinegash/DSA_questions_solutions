class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def confusion(letter):
            start = 0
            count = 0
            res = 0
            for end in range(len(answerKey)):
                if answerKey[end] != letter:
                    count+=1
                while count > k:
                    if answerKey[start] != letter:
                        count-=1
                    start+=1
                res = max(res, end-start+1)
            return res
        return max(confusion("T"), confusion("F"))