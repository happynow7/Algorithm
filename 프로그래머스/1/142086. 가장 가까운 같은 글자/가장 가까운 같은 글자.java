import java.util.*;

class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];

        HashMap<Character, Integer> map = new HashMap<>();
        for(int i=0; i<s.length(); i++) {
            if(!map.containsKey(s.charAt(i))) {
                answer[i] = -1;
                map.put(s.charAt(i), i);
            }else {
                int before = map.get(s.charAt(i));
                answer[i] = i - before;
                map.put(s.charAt(i), i);
            }
        }
        return answer;
    }
}