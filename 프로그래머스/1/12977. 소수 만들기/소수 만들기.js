function solution(nums) {
  let answer = 0;

  for (let i = 0; i < nums.length; i++) {
    for (let j = i + 1; j < nums.length; j++) {
      for (let k = j + 1; k < nums.length; k++) {
        let sum = nums[i] + nums[j] + nums[k];

        if (isPrime(sum)) answer++;
      }
    }
  }
  return answer;
}

// 소수 판별하기
const isPrime = (sum) => {
  for (let i = 2; i < sum; i++) {
    if (sum % i === 0) return false;
  }
  return true;
};


// sol2
// function solution(nums) {
//   const result = [];

//   const isPrimeNumber = (n) => {
//     for (let i = 2; i <= Math.sqrt(n); i++) {
//       if (n % i === 0) return false;
//     }
//     return true;
//   };

//   const size = nums.length;

//   for (let i = 0; i < size; i++) {
//     for (let j = i + 1; j < size; j++) {
//       for (let k = j + 1; k < size; k++) {
//         const num = nums[i] + nums[j] + nums[k];
//         if (isPrimeNumber(num)) {
//           result.push(num);
//         }
//       }
//     }
//   }

//   return result.length;
// }