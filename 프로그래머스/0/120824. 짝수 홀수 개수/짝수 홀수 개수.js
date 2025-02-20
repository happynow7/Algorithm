function solution(num_list) {
    var answer = [];
    const obj = { 'even': 0, 'odd': 0 }
  for (let i = 0; i < num_list.length; i++) {
    if (num_list[i] % 2 === 1) {
      obj['odd'] += 1
    } else {
      obj['even'] += 1
    }
  }
    answer = [obj['even'], obj['odd']]
    return answer;
}