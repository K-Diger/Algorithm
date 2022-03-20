const fs = require('fs')

const InputMushroom = []

const result = 0
const Mario = 0


for (i = 0; i < 10; i ++)
{
    InputMushroom.append(fs.readFileSync('dev/stdin').toString());
}

console.log(InputMushroom)
// for (j = 0; j < 10; j ++)
// {

// }
// for (Mushroom in InputMushroom):
//     Mario += Mushroom
//     if abs(mario-100) <= abs(result-100):
//         result = mario

// print(result)