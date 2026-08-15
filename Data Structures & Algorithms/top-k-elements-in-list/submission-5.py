class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
        #{1:1, 2:2, 3:3}
        
        frequency_and_number = []
        for number, frequency in count.items():
            frequency_and_number.append((frequency, number))
        
        frequency_and_number.sort(reverse=True)

        answer = []

        for frequency, number in frequency_and_number[:k]:
            answer.append(number)
        
        return answer
