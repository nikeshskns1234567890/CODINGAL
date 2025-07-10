var a = [65 , 56 , 657, 774, 54 , 654 , 689 , 342]

var b = a.sort(function(a,b){
    return a - b
})
console.log(b)

var c =a.sort(function(a,b){
    return b - a
})
console.log(c)

a.map((val) => {
    console.log("the value is", val)
})
a.map((val) => {
    console.log("the value is", val*val)
})
