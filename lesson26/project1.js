class Footballer {
    constructor(name, club, age) {
        this.name = name;
        this.club = club;
        this.age = age;
    }

    makeSound() {
        return 'Goal celebration!'
    }
    whereYouPlay() {
        console.log("I play in a stadium")
    }
    printMyClub() {
        return this.club
    }
    static sayHello() {
        console.log("is greeting the fans")
    }
}

class Striker extends Footballer {
    constructor(name, club, age, nationality, bootColor) {
        super(name, club, age)
        this.nationality = nationality
        this.bootColor = bootColor
    }
    doYouScore() {
        return "Yes, I score goals!"
    }
}

var player1 = new Footballer('Mbappé', 'Paris Saint-Germain', 25)
var striker1 = new Striker('Haaland', 'Manchester City', 24, 'Norwegian', 'neon green')

console.log(player1.age)
console.log(player1.age)
console.log(player1.club)
console.log(player1.name)
console.log(player1.makeSound())
player1.whereYouPlay()
Footballer.sayHello()

console.log(".........print for striker...........")
console.log(striker1.name)
console.log(striker1.club)
console.log(striker1.age)
console.log(striker1.nationality)
console.log(striker1.bootColor)
console.log(striker1.printMyClub())
console.log(striker1.doYouScore())
console.log(striker1.makeSound())
striker1.whereYouPlay()
