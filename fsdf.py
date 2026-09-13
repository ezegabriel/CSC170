def threeSumClosest(nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        b_bool, i_count, i_beg, i_end, l_temp, l_list, b_list = False, 0, -2, 1, [], [], True

        while not b_bool:
            l_temp = []
            if i_count != len(nums) - 2:
                for i in range(i_count, len(nums)):
                    l_temp.append(nums[i])
                    if len(l_temp) == 3:
                        l_list.append(sum(l_temp))
                        i_count += 1
            else:
                for i in range(i_beg, i_end):
                    l_temp.append(nums[i])
                    if len(l_temp) == 3 and not sum(l_temp) in l_list:
                        l_list.append(sum(l_temp))
                        i_beg += 1
                        i_end += 1
                    else:
                        b_bool = True

        l_check = l_list + []
        for item in l_list:
            if item < 0:
                b_list = False
         
        if not b_list:
            for i in range(len(l_check)):
                l_check[i] = abs(l_check[i] - target)
            return l_check, l_list
        
        elif b_list and target > 0:
            for i in range(len(l_check)):
                l_check[i] = abs(target - l_check[i])
            return l_list[l_check.index(min(l_check))]
        
        else:
            return min(l_list)

a = threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2)
print(a)
