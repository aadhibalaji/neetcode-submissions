class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        int a = 0;
        int b = 0;
        int c = 0;

        Arrays.sort(nums);

        List<List<Integer>> res = new ArrayList<>();
        int size = res.size();

        for (int i = 0; i < nums.length; i++) {
            
            a = nums[i];

            if (a > 0) {
                break;
            }

            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            int left = i + 1;
            int right = nums.length - 1;

            

            while (left < right) {
                b = nums[left];
                c = nums[right];
                int sum = a + b + c;
                
                if (sum > 0) {
                    right--;
                } else if (sum < 0) {
                    left++;
                } else {
                    res.add(Arrays.asList(a, b, c));
                    left++;
                    right--;

                    while (left < right && nums[left] == nums[left - 1]) {
                        left++;
                    }
                }
            }
            
        }

        return res;
    }
}
