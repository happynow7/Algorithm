function solution(s){
    var answer = true;
    const bucket = [];
    
    for (let i = 0; i<s.length; i++){
        if(s[i] == "("){
            bucket.push(s[i])
        }
        if(s[i] == ")"){
            if(bucket.length === 0) return false;
            bucket.pop()
        }
    }
    
    if(bucket.length == 0) return true
    else return false
    
    return answer;
}