function solution(my_string, s, e) {
    const reversed = my_string
        .slice(s, e + 1)          // s부터 e까지 자름 (e 포함)
        .split('')                // 배열로 변환
        .reverse()                // 뒤집기
        .join('');                // 다시 문자열로

    return my_string.slice(0, s) + reversed + my_string.slice(e + 1);
}
