function solution(price) {
    var answer = 0;
    
    if(price >=  100000 && price<=299999){
        return price = price * 0.95;
    }else if (price >=  300000 && price<=499999){
        return price = price * 0.9;
    }else if (price >=  500000){
        return price = price * 0.8;
    }
}



function solution(price) {
    return (price >= 500000) ? ~~(price * 0.8)
         : (price >= 300000) ? ~~(price * 0.9)
         : (price >= 100000) ? ~~(price * 0.95)
         : price;
}