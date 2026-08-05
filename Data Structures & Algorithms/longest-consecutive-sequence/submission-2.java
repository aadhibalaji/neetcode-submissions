class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        
        Set<Integer> numbers = new HashSet<>();
        Set<Integer> starters = new HashSet<>();
        for (int i = 0; i < nums.length; i++) {
            numbers.add(nums[i]);
        }

        for (int num : numbers) {
            if (!numbers.contains(num - 1) && !starters.contains(num)) {
                starters.add(num);
            }
        }

        int bestCount = 1; 
        int count = 1; 
        
        for (int start : starters) {
            int i = start;
            while (numbers.contains(i + 1)) {
                count++;
                i++;
            }

            if (count > bestCount) {
                bestCount = count;
            }
            count = 1;
        }

        return bestCount;
        
    }
}
