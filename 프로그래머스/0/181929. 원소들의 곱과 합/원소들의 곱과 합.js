function solution(num_list) {
    var answer = 0;
    let newsum = 0;
    let newmul = 1;
    
    for (let i = 0; i <num_list.length; i++){
        newsum += num_list[i]
        newmul *= num_list[i]
    }
    
    if ( newmul < Math.pow(newsum, 2)){
        answer = 1
    }else{
        answer = 0
    }
    
    return answer;
}