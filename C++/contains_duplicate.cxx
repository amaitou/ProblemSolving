class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        std::map<int, int> m;

        for (int i = 0; i < nums.size(); ++i)
            m[nums[i]] += 1;
        
        std::map<int, int>::iterator _it = m.begin();
        while (_it != m.end())
        {
            if (_it->second > 1)
                return (true);
            ++_it;
        }
        return (false);
    }
};

// https://leetcode.com/problems/contains-duplicate/
