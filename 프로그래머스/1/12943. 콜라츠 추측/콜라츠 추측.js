
function solution(num) {
    let answer = 0;

    for (let i = 0; i < 500; i++){
      //최대 500회가 반복되는 반복문 생성
        if(num != 1){
            num = num%2 == 0? num / 2 : num * 3 + 1;
          // num이 1이 아닐때 실행되는 삼항연산자
        } else{
            return answer = i;
          // 이 외의 조건은 num 이 1이라는 것이므로 반복횟수 i를 리턴
        }
    }
    return answer = -1;
  //반복문이 모두 돌 때까지 1이 안나오면 -1을 리턴
}