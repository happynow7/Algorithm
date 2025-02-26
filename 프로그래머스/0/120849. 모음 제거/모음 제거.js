// 답안 #1 : for() 반복문과 includes()를 통해 모음에 속하지 않는 것을 리턴

function solution(my_string) {
  let answer = "";
  const vowel = ["a", "e", "i", "o", "u"];
  for (let i = 0; i < my_string.length; i++) {
    if (!vowel.includes(my_string[i])) answer += my_string[i];
  }
  return answer;
}

// 답안 #2 : for() 반복문을 중복으로 사용하고, replaceAll()하여 모음에 있는 것을 공백으로 대체하여 리턴

function solution(my_string) {
  const vowel = ["a", "e", "i", "o", "u"];
  for (let i = 0; i < my_string.length; i++) {
    for (let v of vowel) my_string = my_string.replaceAll(v, "");
  }
  return my_string;
}

// 답안 #3 : my_string을 배열로 형태로 복사하고 filter()와 includes()를 이용하여 리턴

function solution(my_string) {
  return [...my_string]
    .filter((v) => !["a", "e", "i", "o", "u"].includes(v))
    .join("");
}

// 답안 #4 : replace()와 정규식을 사용하여 모음을 공백으로 대체하여 리턴

function solution2(my_string) {
  return my_string.replace(/[aeiou]/g, "");
}
