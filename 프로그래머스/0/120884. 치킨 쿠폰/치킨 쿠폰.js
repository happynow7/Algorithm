function solution(chicken) {
    var answer = 0;
    var serviceChicken = 0;
    
    while(chicken >= 10) {
        serviceChicken = Math.floor(chicken / 10);
        answer += serviceChicken;
        chicken = serviceChicken + (chicken % 10);
    }
    
    return answer;
}
