function solution(n) {
    var answer = [n,];
    
    while(n>1){
        if(n%2 == 0){
            n /= 2;
            answer.push(n);
        }else if(n%2 == 1){
            n = 3*n+1
            answer.push(n);
        }
    }
    return answer;
}