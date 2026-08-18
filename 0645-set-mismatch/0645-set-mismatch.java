class Solution {
    public int[] findErrorNums(int[] nums) {

        HashMap<Integer, Integer> mp = new HashMap<>();

        for(int n : nums) {
            mp.put(n, mp.getOrDefault(n, 0) + 1);
        }

        int duplicate = 0;
        int missing = 0;

        for(int i = 1; i <= nums.length; i++) {

            if(mp.getOrDefault(i, 0) == 2) {
                duplicate = i;
            }

            if(mp.getOrDefault(i, 0) == 0) {
                missing = i;
            }
        }

        return new int[]{duplicate, missing};
    }
}