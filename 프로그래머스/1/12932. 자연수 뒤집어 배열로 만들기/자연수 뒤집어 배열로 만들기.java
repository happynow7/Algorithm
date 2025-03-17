class Solution {
    public int[] solution(long n) {
        String str = String.valueOf(n);
        StringBuffer bf = new StringBuffer(str);
        bf.reverse();
        int[] answer = new int[bf.length()];
        for (int i = 0; i<bf.length(); i++){
            answer[i] = Character.getNumericValue(bf.charAt(i));
        }
        return answer;
    }
}