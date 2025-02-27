function solution(n) {
    var answer = 0;
    let k = 0;
    
    if ( n%2 !== 0){
        for (let i = 1; i <= n; i += 2){
            answer += i
        }
    }else if( n%2 == 0){
        for (let i = 0; i <= n; i += 2){
            k = Math.pow(i, 2)
            answer += k
            
        }
    }
    
    return answer;
}