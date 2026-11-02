class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        set<int> lookup;

        for (int i = 0; i < nums.size(); ++i) {
            if (lookup.count(nums[i])) {
                return true;
            }
            lookup.insert(nums[i]);
        }
        return false;
    }
};