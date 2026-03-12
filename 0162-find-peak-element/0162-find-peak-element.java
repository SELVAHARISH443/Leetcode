class Solution {
    public int findPeakElement(int[] nums) {

        int max=nums[0];
        int k=0;
        int len =nums.length;
        for(int i=1;i<=len-1;i++)
        {
              if(max<nums[i])
              {
                max=nums[i];
                k=i;

              }
        }
        return k;
        
    }
}