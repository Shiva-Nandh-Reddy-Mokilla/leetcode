class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        backtracking(res, new ArrayList<>(), 0, nums);
        return res;
    }
    public void backtracking(List<List<Integer>> res, List<Integer> list, int start, int[] nums){
        res.add(new ArrayList<>(list));
        for(int i = start; i<nums.length; i++){
            list.add(nums[i]);
            backtracking(res, list, i+1, nums);
            list.remove(list.size()-1);
        }
    }
}