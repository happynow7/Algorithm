function solution(order) {
    var answer = 0;
    
    answer = [...String(order)].filter((r)=> ["3", "6", "9"].includes(r)).length
    return answer;
}