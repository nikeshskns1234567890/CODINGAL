class birds {
    constructor(name, species, age) {
        this.name = name;
        this.species = species;
        this.age = age;
    }

    makeSound() {
        return 'animal sound'
    }
    whereYouLive() {
        console.log("i live in jungle")
    }
    printMyspecies() {
        return this.species
    }
    static sayHellp() {
        console.log("is saying hello")
    }
}
class LION extends animal{
    constructor(name, species, age, nationality, hairColor){
        super(name, species, age, nationality)
        this.hairColor = hairColor
    }
    doYoukill(){
        return"yes i kill"
    }
}
var b = new Animal('pookie', 'dodo', 8, 'indian')
var l = new LION('don', 'panthera leo', 14,'kenya', 'golden')
console.log(b.age)
console.log(b.age)
console.log(b.species)
console.log(b.name)
console.log(b.makeSound())
b.whereYoulive()
Animal.sayHello()

console.log(".........print for lion...........")
console.log(l.name)
console.log(l.species)
console.log(l.age)
console.log(l.natonality)
console.log(l.haircolor)
console.log(l.printMyspecies())
console.log(l.doYoukill())
console.log(l.makeSound())
l.whereYouLive
