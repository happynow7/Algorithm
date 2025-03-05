function solution(my_string, m, c) {
    var answer = '';
    const new_my_string = my_string.slice(c-1,)
    for (let i = 0; i<new_my_string.length; i += m){
         answer += new_my_string[i];
         }
    return answer;
}