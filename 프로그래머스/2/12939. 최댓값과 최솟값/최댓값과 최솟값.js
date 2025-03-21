function solution(s) {
    var answer = '';
    let max = Math.max(...s.split(' '))
    let min = Math.min(...s.split(' '))
    answer = min + ' ' +max
    return answer;
}