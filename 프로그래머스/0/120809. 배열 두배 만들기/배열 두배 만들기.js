function solution(numbers) {
    var answer = [];
    
    for (let i = 0; i<numbers.length; i++){
        numbers[i] = numbers[i]*2
        answer.push(numbers[i])
    }
    
    return answer;
}