function solution(str_list, ex) {
    return str_list.filter(a => !a.includes(ex)).join('');
}


// function solution(str_list, ex) {
//     let result = '';

//     for(let i = 0; i < str_list.length; i++) {
//         if(!str_list[i].includes(ex)) {
//             result += str_list[i];
//         }
//     }    

//     return result;
// }