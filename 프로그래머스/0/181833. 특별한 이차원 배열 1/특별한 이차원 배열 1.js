function solution(n) {
    const arr = Array.from({ length: n }, () => Array(n).fill(0));
    
    for (let i = 0; i< n ; i++){
        answer[i][i] = 1;
    }
    
    return answer;
}


function solution(n) {
    const arr = Array(n).fill(Array(n).fill(0))
    
    return arr.map((a, i) => {
        return a.map((b, bi) => bi === i ? 1 : b)
    })
}
