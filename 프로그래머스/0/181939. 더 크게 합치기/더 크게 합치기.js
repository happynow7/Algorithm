function solution(a, b) {
    var answer = 0;
    
    let sola = parseInt(String(a)+String(b))
    let solb = parseInt(String(b)+String(a))
    
    if (sola > solb){
        answer = sola
    }else{
        answer = solb
    } 
    
    return answer;
}