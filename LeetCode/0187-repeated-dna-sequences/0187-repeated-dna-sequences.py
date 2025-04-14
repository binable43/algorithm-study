class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        dna_dict = {}
        for i in range(0, len(s) - 9):
           dna = s[i:i+10]
           dna_dict.setdefault(dna, 0)
        
        for j in range(0, len(s) - 9):
            dna_check_if_repeat = s[j:j+10]
            if dna_check_if_repeat in dna_dict:
                dna_dict[dna_check_if_repeat] += 1
        
        output = []
        for dna, count in dna_dict.items():
            if count >= 2:
                output.append(dna)
        
        return output