function solution(a, b) {
    var answer = 0;
    
    let Ares = String(a)+String(b);
    let Bres = 2 * a * b;
    return Math.max(Ares, Bres);
}