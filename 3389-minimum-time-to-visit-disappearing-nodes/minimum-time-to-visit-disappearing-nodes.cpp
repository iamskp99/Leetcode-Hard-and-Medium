class Solution {
public:
    vector<int> ans;
    map<int,vector<int>> graph;
    map<pair<int,int>,int> price;
    multiset<pair<int,int>> pqueue;
    
    void dijkstra(int source,vector<int>& disappear){
        ans[0] = 0;
        pqueue.insert({0,0});
        int key,node,pp,gg;
        while(pqueue.size() > 0){
            auto it = pqueue.begin();
            pair<int,int> ggg = *it;
            key = ggg.first;
            node = ggg.second;
            pqueue.erase(it);
            for(auto x:graph[node]){
                pp = price[{node,x}]+key;
                if(pp < disappear[x]){
                    if(ans[x] == 1000000000){
                        pqueue.insert({pp,x});
                        ans[x] = pp;
                    }else{
                        gg = ans[x];
                        if(pp < gg){
                            pqueue.erase({gg,x});
                            pqueue.insert({pp,x});
                            ans[x] = pp;
                        }
                    }
                }
            }
        }
    }

    vector<int> minimumTime(int n, vector<vector<int>>& edges, vector<int>& disappear) {
        int i = 0,u,v,p,t;
        set<pair<int,int>> exist; 
        while(i < edges.size()){
            u = edges[i][0];
            v = edges[i][1];
            if(u == v){
                i += 1;
                continue;
            }
            p = edges[i][2];
            pair<int,int> r1 = {u,v};
            pair<int,int> r2 = {v,u};
            if(exist.find(r1) == exist.end() && (exist.find(r2) == exist.end())){
                exist.insert(r1);
                graph[u].push_back(v);
                graph[v].push_back(u);
                price[r1] = p;
                price[r2] = p;
            }else{
                t = price[r1];
                // cout<<u<<" "<<v<<" "<<p<<" "<<t<<"\n";
                if(p < t){
                    price[r1] = p;
                    price[r2] = p;
                }
            }
            i += 1;
        }
        // cout<<price[{0,1}]<<" as \n";
        i = 0;
        while(i < n){
            ans.push_back(1e9);
            i += 1;
        }

        dijkstra(0,disappear);
        i = 0;
        while(i < n){
            if(ans[i] == 1000000000){
                ans[i] = -1;
            }

            i += 1;
        }
        return ans;
    }
};