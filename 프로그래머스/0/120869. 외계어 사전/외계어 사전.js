function solution(spell, dic) {
    const word = spell.sort().join('');
    const arr = [];
    
    for (let i = 0; i < dic.length; i++){
     arr.push(dic[i].split("").sort().join(""))
    }
    
    if (arr.includes(word)){
        return 1;
    }else{
        return 2;
    }
    
}