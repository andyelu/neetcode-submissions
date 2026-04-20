class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int l = 0;
        int r = matrix[0].size()-1;
        int t = 0;
        int b = matrix.size()-1;

        vector<int> res;

        int direction = 1;

        while (res.size() < matrix.size() * matrix[0].size()) {
            switch (direction % 4) {
                case 1: {
                    // left
                    for (int i = l; i <= r; i++) {
                        res.push_back(matrix[t][i]);
                    }
                    t++;
                    break;
                }

                case 2: {
                    // down
                    for (int i = t; i <= b; i++) {
                        res.push_back(matrix[i][r]);
                    }
                    r--;
                    break;
                }

                case 3: {
                    // right
                    for (int i = r; i >= l; i--) {
                        res.push_back(matrix[b][i]);
                    }
                    b--;
                    break;
                }

                case 0: {
                    // up
                    for (int i = b; i >= t; i--) {
                        res.push_back(matrix[i][l]);
                    }
                    l++;
                    break;
                }
            }

            direction++;
        }

        return res;
    }
};
