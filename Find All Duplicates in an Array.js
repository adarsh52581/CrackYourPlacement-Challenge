/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDuplicates = function(nums) {
    let result = [];
    for(let i=0;i<nums.length;i++){
        let num=Math.abs(nums[i]);
        let index = num - 1;
        if (nums[index] < 0) result.push(num)
        else nums[index] = -nums[index]
    }     
    return result;
};