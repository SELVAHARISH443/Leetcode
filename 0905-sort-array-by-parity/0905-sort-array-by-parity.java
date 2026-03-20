class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int l=nums.length;
        int s=0,e=l-1;
        int[] temp=new int[l];
        for(int i=0;i<l;i++){
            if(nums[i]%2==0){
                temp[s++]=nums[i];
            }
            else{
                temp[e--]=nums[i];
            }
        }
        return temp;
            }
}