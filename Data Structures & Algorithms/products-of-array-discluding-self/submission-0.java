class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] prefix = new int[nums.length];
        int[] suffix = new int[nums.length];

        int[] result = new int[nums.length];


        prefix[0] = 1;
        //Build prefix array
        for (int i = 1; i < nums.length; i++) {
            prefix[i] = nums[i - 1] * prefix[i - 1];
        }

        //Build suffix array
        suffix[nums.length - 1] = 1;
        for (int j = nums.length - 2; j >= 0; j--) {
            suffix[j] = nums[j + 1] * suffix[j + 1];
        }


        //Build result array
        for (int k = 0; k < nums.length; k++) {
            result[k] = prefix[k] * suffix[k];
        }

        return result;

    
    }
}  
