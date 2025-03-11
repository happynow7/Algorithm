function solution(k, score) {
    var answer = [];
    box = [];
    
    score.forEach(num => {
        box.push(num);
        box.sort((a,b) => b-a).splice(k);
        answer.push(Math.min.apply(null, box));
    });
    
    return answer;
}