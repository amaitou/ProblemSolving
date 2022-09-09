function solution(string) {
     return string.split("").map((a) => {if (a.toUpperCase() === a) {return " " + a} else { return a }}).join("");

}

// Link: https://www.codewars.com/kata/5208f99aee097e6552000148
