class Solution {
    public int findNumbers(int[] nums) {
        int c=0,rem=0,t=0;
        for(int res:nums){
            t=0;
            while(res!=0){
                rem=res%10;
                t=t+1;
                res/=10;
            }
            if(t%2==0){
                c=c+1;
            }
        }
        return c;
    }
}