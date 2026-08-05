class Solution {
    public boolean isPalindrome(String s) {
        
        

        s = s.replaceAll("[^a-zA-Z0-9]", "");
        s = s.toLowerCase();
        System.out.println(s);

        int right = s.length() - 1;
        int left = 0;
        System.out.println(right);

        while (right >= left || left <= right) {
            if (s.charAt(left) == s.charAt(right)) {
                left++;
                right--;
                continue;
            }

            return false;
        }

        return true;
    }
}
