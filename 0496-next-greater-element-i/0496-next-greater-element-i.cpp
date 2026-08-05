class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        vector<int> ans;
        int i = 0, j = 0, k = 0;
        bool found = false;

        while (i < nums1.size()) {
            found = false;

            // Find nums1[i] in nums2
            for (j = 0; j < nums2.size(); j++) {
                if (nums1[i] == nums2[j]) {
                    break;
                }
            }

            // Find the next greater element
            for (k = j; k < nums2.size(); k++) {
                if (nums2[k] > nums2[j]) {
                    ans.push_back(nums2[k]);
                    found = true;
                    break;
                }
            }

            if (!found) {
                ans.push_back(-1);
            }

            i++;
        }

        return ans;
    }
};