var a = 75;
var b = 'messi'
var c = true
var d = { yoyo: "honey singh" }
var e = [6, 7, 89, 90, 76, 67]
var f = ['R9', 'CR7', 'ML10']

console.log(typeof (a))
console.log(typeof (b))
console.log(typeof (c))
console.log(typeof (d))
console.log(typeof (e))
console.log(typeof (f))

var g = String(a)
console.log(typeof (g))
var h = String(c)
console.log(typeof (h))
console.log(h)
var i = Number(c)
console.log(typeof (i))
console.log(i)
var j = '66'
var k = Number(j)
console.log(typeof (k))
console.log(k)


try {
    var q = "siuuuuuuuuuuuuuuuuuuuuu" + 'yooooooooooooooooo'
    throw new Error("diego jota and his brother andre silva passed away due to bursting, of thier car tyres")
} catch (err) {
    console.log("my error is" + err.message)
}

function multiply1(a,b,c,d){
    return a*b*c*d
}
var multiply2=(a,b,c,d)=> {return a*b*c*d}

console.log(multiply1(3,4,5,6))
console.log(multiply2(3,4,5,6))