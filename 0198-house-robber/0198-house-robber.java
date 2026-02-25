class Solution {
    public int rob(int[] nums) {
        int p1=0;
        int p2=0;
        int cur = Integer.MIN_VALUE;
        for(int i=0;i<nums.length;i++){
                int temp=p2+nums[i];
                if(temp>cur){
                    cur = temp;
                }
                p2 = p1;
                p1 = cur;
        }
        return p1;
    }
}