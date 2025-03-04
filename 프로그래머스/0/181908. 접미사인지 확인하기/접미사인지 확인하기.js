function solution(my_string, is_suffix) {
    var answer = 0;
    
    answer = +(my_string.endsWith(is_suffix))
    
    return answer;
}