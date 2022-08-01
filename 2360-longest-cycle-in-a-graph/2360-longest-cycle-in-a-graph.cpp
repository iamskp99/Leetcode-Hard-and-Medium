class Solution {
public:
    unordered_set<int> visited;
    unordered_map<int,int> cur;
    int ans;
    void dfs(int node,vector<int>& edges,int cnt){
        if(node == -1){
            return;
        }
        if(visited.find(node) != visited.end()){
            if(cur.find(node) != cur.end()){
                int rep = cnt-cur[node];
                ans = max(ans,rep); 
            }
           return; 
        }
        visited.insert(node);
        cur[node] = cnt;
        dfs(edges[node],edges,cnt+1);
        cur.erase(node);
        return;
    }
    
    int longestCycle(vector<int>& edges) {
        int i,n;
        n = edges.size();
        ans = 0;
        i = 0;
        while(i < n){
            if(visited.find(i) == visited.end()){
                dfs(i,edges,0);
            }
            i += 1;
        }
        if(ans == 0){
            return -1;
        }
        return ans;
    }
};