class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        Arrays.sort(letters);
        for(char res:letters){
            if(res>target){
                return res;
                
            }
        }
       return letters[0];
    }
}