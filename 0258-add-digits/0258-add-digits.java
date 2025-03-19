class Solution {
    public int addDigits(int num) {
        int rem1=0,rem2=0,s=0;
        while(num!=0){
            rem1=num%10;
            s+=rem1;
            num/=10;
        }
        while(s>9){
            int t=0;
            while(s!=0){
                rem2=s%10;
                t+=rem2;
                s/=10;
            }
            s=t;
        }
        return s;
    }
}