class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int count = 0;
        int maxcount = 0;

        for(int n : nums)
        {
            if(n ==1)
            {
                count = count+1;
                maxcount = max(count,maxcount);
            }
            else
            {
                count = 0;
            }
        }
    
    return maxcount;
        
    }
};