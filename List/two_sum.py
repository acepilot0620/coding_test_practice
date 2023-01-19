'''
Two sum
정수가 저장된 배열 nums이 주어졌을 때, 
nums의 원소중 두 숫자를 더하여 target이 될 수 있으면 True
불가능하면 False를 반환 하시오.
시간복잡도 O(nlogn)
'''

def solution(nums:list, target:int)->bool:
    index_one = 0
    index_two = len(nums)-1
    sorted_nums = sorted(nums)
    for _ in sorted_nums:
        if sorted_nums[index_one]+sorted_nums[index_two] == target:
            return True
        elif index_one == index_two:
            return False
        elif sorted_nums[index_one]+sorted_nums[index_two] > target:
            index_two -= 1
        elif sorted_nums[index_one]+sorted_nums[index_two] < target:
            index_one += 1

print(solution([4,1,9,7,5,3,16], 15))
        
    
