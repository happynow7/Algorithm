class Solution {
    public String solution(String myString, String pat) {
        int temp = myString.lastIndexOf(pat);
        if (temp == -1) {
            return "";
        }
        String answer = myString.substring(0,temp+pat.length());
        return answer;
    }
}