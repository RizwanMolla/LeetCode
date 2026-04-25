class Solution {
    public static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public void moveZeroes(int[] nums) {
        int n = nums.length;

        int j = -1;

        // find first zero
        for(int i = 0; i < n; i++){
            if(nums[i] == 0){
                j = i;
                break;
            }
        }

        if(j == -1) return; // no zero found

        // move non-zero elements forward
        for(int i = j + 1; i < n; i++){
            if(nums[i] != 0){
                swap(nums, j, i);
                j++;
            }
        }
    }
}