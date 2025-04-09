class Solution:
    def digitCount(self, num: str) -> bool:
        answer = True
        counter = {}

        # count expected frequency of each digit and set dictionary
        for i in range(len(num)):
            counter.setdefault(i, int(num[i]))

        # count the actual frequency of each digit in num
        for i in range(len(num)):
            real_count = 0

            for j in range(len(num)):
                if i == int(num[j]):
                    real_count += 1
            
            # if expected frequency is different with actual, return false
            if counter[i] != real_count:
                answer = False
                return answer

        return answer