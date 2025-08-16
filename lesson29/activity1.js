const soumil = {
    name: 'soumil',
    age: 15,
    city: 'Delhi',
    country: 'India',
    continent: 'Asia',
    planet: 'Earth'
};

const myjson = JSON.stringify(soumil);
console.log(myjson);

const newParsedObj = JSON.parse(myjson);
console.log(newParsedObj);

async function add(a, b, c, d) {
    let res = await a + b;
    display(res);
}

function display(some) {
    console.log(some);
}

add(5, 20, 60);
let mypromise = new Promise(function (myResolve, myReject) {
    let x = 0;
    if (x == 2) {
        myResolve("OK");
    } else {
        myReject("Error");
    }
});

mypromise.then(
    function (value) {
        console.log(value);
    },
    function (error) {
        console.log(error);
    }
);
