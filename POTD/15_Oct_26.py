class Solution {
    public int sumCounts(List<Integer> nums) {
        int res = 0;
        int n = nums.size();
        HashSet<Integer> set = new HashSet<>();
        for (int i = 0; i < n; i++ ) {
            int temp = 0;
            set.clear();
            for(int j = i;j < n;j++) {
                if(!set.contains(nums.get(j))) {
                    set.add(nums.get(j));
                    temp += 1;
                }
                res += ( temp * temp );
            }
         }

        return res;
    }
}