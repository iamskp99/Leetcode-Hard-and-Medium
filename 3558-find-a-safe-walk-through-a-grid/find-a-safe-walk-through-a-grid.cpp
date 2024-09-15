class Solution {
public:
    bool findSafeWalk(vector<vector<int>>& grid, int health) {
        //idea --> find shortest path --> to go from 0-1 edge it has edwt 1,1-1 has edwt 1 others 0
        //performing 0-1 bfs
        //there is a graph which has edgewts only 0 & 1.0-1 bfs is best
        int n = grid.size();
        int m = grid[0].size();
        deque<pair<int,int>>dq;
        dq.push_front({0,0});
        int dx[4] = {-1,+1,0,0};
        int dy[4] = {0,0,-1,+1};
        vector<vector<int>>dist(n,vector<int>(m,INT_MAX));
        dist[0][0] = (grid[0][0]==1)?1:0;
        while(!dq.empty()){
            int r = dq.front().first;
            int c = dq.front().second;
            dq.pop_front();
            for(int i = 0;i<4;++i){
                int nr = r+dx[i];
                int nc = c+dy[i];
                if(nr>=0&&nc>=0&&nr<n&&nc<m){
                    if(grid[nr][nc]==0 && dist[r][c]<dist[nr][nc]){
                        dist[nr][nc] = dist[r][c];
                        dq.push_front({nr,nc});
                    }
                    else if(grid[nr][nc]==1 && dist[r][c]+1<dist[nr][nc]){
                        dist[nr][nc] = dist[r][c]+1;
                        dq.push_back({nr,nc});
                    }   
                }
            }
        }
        cout<<dist[n-1][m-1];
        if(health-dist[n-1][m-1]>=1){
            return true;
        }
        return false;
    }
};