function solution(s) {
    let answer = 0;
    const n = s.length;

    // 괄호 짝을 맞추는 함수
    function isValid(str) {
        const stack = [];
        for (let i = 0; i < str.length; i++) {
            const ch = str[i];
            if (ch === '(' || ch === '{' || ch === '[') {
                stack.push(ch);
            } else {
                if (stack.length === 0) return false;
                const last = stack.pop();
                if (
                    (ch === ')' && last !== '(') ||
                    (ch === '}' && last !== '{') ||
                    (ch === ']' && last !== '[')
                ) {
                    return false;
                }
            }
        }
        return stack.length === 0;
    }

    // 문자열을 한 칸씩 회전
    for (let i = 0; i < n; i++) {
        const rotated = s.slice(i) + s.slice(0, i);
        if (isValid(rotated)) answer++;
    }

    return answer;
}
