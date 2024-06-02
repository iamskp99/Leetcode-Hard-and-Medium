class Solution {
public:

    int merge(int start,int mid,int end,vector<int>& nums){
        int ans = 0;
        vector<int> arr1;
        vector<int> arr2;
        int ptr,j,i = start;
        while(i <= mid){
            arr1.push_back(nums[i]);
            i += 1;
        }

        while(i <= end){
            arr2.push_back(nums[i]);
            i += 1;
        }

        i = 0;
        j = 0;
        while(i < arr1.size()){
            while((j < arr2.size())&&(arr1[i] > (long long) 2*arr2[j])){
                j += 1;
            }
            ans += j;
            i += 1;
        }
        
        i = 0;
        j = 0;
        ptr = start;
        while((i < arr1.size())&&(j < arr2.size())){
            if (arr1[i] < arr2[j]) {
                nums[ptr] = arr1[i];
                i++;
            }
            else {
                nums[ptr] = arr2[j];
                j++;
            }
            ptr++;
        }

        while(i < arr1.size()){
            nums[ptr] = arr1[i];
            ptr++;
            i += 1;
        }

        while(j < arr2.size()){
            nums[ptr] = arr2[j];
            ptr++;
            j += 1;
        }

        return ans;
    }


    int mergeSort(int start,int end,vector<int>& nums){
        if(start >= end){
            return 0;
        }

        int mid = ((end-start)/2)+start;
        int ans = mergeSort(start,mid,nums)+mergeSort(mid+1,end,nums);
        ans += merge(start,mid,end,nums);
        return ans;
    }

    int reversePairs(vector<int>& nums) {
        return mergeSort(0,nums.size()-1,nums);
    }
};