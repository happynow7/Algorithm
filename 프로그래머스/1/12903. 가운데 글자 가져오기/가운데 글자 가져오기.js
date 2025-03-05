function solution(s) {
    var answer = '';
    
    if(s.length%2 == 1){
        answer = s[Math.floor(s.length/2)]
    }else if(s.length%2 == 0){
        const sl = Math.floor(s.length/2)
        answer += s[sl-1] + s[sl]
     }
    
    return answer;
}