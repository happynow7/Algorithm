class Solution {
    public int solution(int n) {
        int i = 0;
        while (true) {
            if (n == Math.pow(i, 2)) {
                return 1;
            } else if (Math.pow(i , 2) > n) {
                return 2;
            }
            i++;
        }
    }
}
