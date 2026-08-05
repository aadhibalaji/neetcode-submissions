class Solution {
    public int maxArea(int[] heights) {
        int bestArea = 0;

        int left = 0; 
        int right = heights.length - 1;


        while (left < right) {
            int diff = right - left;
            int currArea;
            if (heights[right] <= heights[left]) {
                currArea = diff * heights[right];
                if (currArea > bestArea) {
                    bestArea = currArea;
                    
                }
                right--;
            } else {
                currArea = diff * heights[left];
                if (currArea > bestArea) {
                    bestArea = currArea;
                }
                left++;
            }

            
        }

        return bestArea;
    }
}
