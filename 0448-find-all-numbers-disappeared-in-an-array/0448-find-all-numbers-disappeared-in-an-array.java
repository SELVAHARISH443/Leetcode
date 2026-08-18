class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        int n=nums.length;
          HashSet<Integer> st=new HashSet();
        for(int i=0;i<n;i++){
             
               st.add(nums[i]);
        }
        ArrayList<Integer> al=new ArrayList();
        for(int i=1;i<=n;i++){
            if(!st.contains(i)){
                al.add(i);
            }
        }
        return al;
    }
}