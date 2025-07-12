var a = [21, 88, 312, 477, 93, 231, 519, 145]

var b = a.sort(function(a, b){
    return a - b
})
console.log(b)

var c = a.sort(function(a, b){
    return b - a
})
console.log(c)

a.map((val) => {
    console.log("the value is", 1000 - val)
})
a.map((val) => {
    console.log("the value is", val ** 2)
})
