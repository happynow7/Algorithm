function solution(str1, str2) {
    if (str1.includes(str2)) {
        return 1
    } else {
        return 2
    }
}

// const solution = (str1, str2) => str1.includes(str2) ? 1 : 2