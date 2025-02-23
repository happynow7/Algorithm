function solution(arr) {
    const arrLength = arr.length;
    let num = 0;
    
    while(Math.pow(2, num) < arrLength) num ++;
    let fillNum = Math.pow(2, num) - arrLength;
    const zArr = Array(fillNum).fill(0);
    return arr.concat(zArr);
}