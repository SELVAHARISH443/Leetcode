class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int t = 0;
        for(int i = 0; i < operations.length; i++){
            if(operations[i].contains("++")){
                t++;
            } 
            else{
                t--;
            }
        }

        return t;
    }
}