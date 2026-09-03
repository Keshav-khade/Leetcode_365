"""
1. list insertion 
          1. direct nums[8] = 4 this return index error if index not there.
          2. insert(inx,obj) this could be safe for us it's simply insert that obj at the last of the list.
2. 

"""
# nums = [0,1,2,2,3,0,4,2]
# nums =[3,2,2,3]
# nums =[]
# nums =[2,2,2]
# nums = [1,1,1]
nums = [2]
if len(nums) == 0:
          print("empty")
ele = 1
i = 0
for j in range(len(nums)):
          if nums[j] != ele:
                  nums[i] = nums[j]
                  i += 1
          
print(i)  
