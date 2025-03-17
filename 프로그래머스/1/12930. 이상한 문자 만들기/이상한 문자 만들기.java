class Solution {
    public String solution(String s) {
        StringBuilder answer = new StringBuilder();
        int count = 0;
        String[] str = s.split("");
        
        for (String ss : str) {
            if (ss.equals(" ")) {
                count = 0;
            } else {
                ss = (count % 2 == 0) ? ss.toUpperCase() : ss.toLowerCase();
                count++;
            }
            answer.append(ss);
        }
        return answer.toString();
    }
}
