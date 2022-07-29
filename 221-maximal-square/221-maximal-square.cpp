class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int m = matrix.size(), n = matrix[0].size();
        vector<vector<int>>dp(m+1,vector<int>(n+1));
        
        int largest=0;
        for(int i = 0 ; i < m+1 ; i++){
            for(int j = 0 ; j < n+1 ; j++){
                if(i == 0 || j == 0)dp[i][j] = 0;
            }
        }
        
        for(int i = 1 ; i < m+1 ; i++){
            for(int j = 1 ; j < n+1 ; j++){
                if(matrix[i-1][j-1] == '1'){
                    dp[i][j] = 1+min(dp[i-1][j-1],min(dp[i-1][j],dp[i][j-1])) ;
                }
                if(largest < dp[i][j]){
                    largest=dp[i][j];
                }
            }
        }
        return largest*largest;
        
    }
};