class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        HashMap<Integer, Integer> vals = new HashMap<>();


        for (int i = 0; i < nums.length; i++) {
            int difference = target - nums[i];

            if (!vals.containsKey(difference)) {
                
                vals.put(nums[i], i);
            } else {
                return new int[]{vals.get(difference), i};
                
            }
        }

        return new int[]{};
    }
}
