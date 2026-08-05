class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
        }
        
        int[] solution = new int[k];
        
        for (int j = 0; j < k; j++) {
            Map.Entry<Integer, Integer> maxEntry = null;
            for (Map.Entry<Integer, Integer> e : map.entrySet()) {
                if (maxEntry == null || e.getValue() > maxEntry.getValue()) {
                    maxEntry = e;
                }
            }

            // maxEntry holds the key with the highest frequency
            solution[j] = maxEntry.getKey();
            map.remove(maxEntry.getKey());
        }

        return solution;

        
    }
}
