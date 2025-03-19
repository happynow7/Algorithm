import java.util.Arrays;

class Solution {
    public int[] solution(String my_string) {
        //my_string에서 숫자가 아닌 것은 전부 공백으로 바꿈
        my_string = my_string.replaceAll("[^0-9]", "");

        int[] answer = new int[my_string.length()];

        for(int i=0; i<my_string.length(); i++) {
            //숫자가 아스키코드로 표현되기 때문에 -'0'을 해서 숫자로 표현되게 해준다
            answer[i] = my_string.charAt(i)-'0';
        }

        Arrays.sort(answer);
        return answer;
    }
}