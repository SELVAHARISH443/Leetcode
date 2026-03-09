class Solution {
    public int search(int[] nums, int target) {
        int l=nums.length;
        int start=0;
        int end=l-1;
        int mid=0;
        int result=-1;
        while(start<=end){
            mid=start+(end-start)/2;
            if(target>nums[mid]){
                start=mid+1;
            }
            else if(target<nums[mid]){
                end=mid-1;
            }
            else{
                result=mid;
                break;
            }
        }
        return result;
    }
}