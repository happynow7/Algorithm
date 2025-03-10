function solution(clothes) {
    var answer = 1;
    let closet = {};
    
    clothes.forEach(([name, type]) => {
        if (closet[type]) {
            closet[type]++;
        } else {
            closet[type] = 1;
        }
    });
    
    for (const type in closet) {
        answer *= (closet[type] + 1);
    }
    
    return answer - 1;
}
