# При помощи цикла for..in перебрать 
#   объект-справочник с датами рождения 
#   и смерти людей и вернуть справочник 
#   с продолжительностью их жизни. 
# Например:

"""
const persons = {
  lenin: { born: 1870, died: 1924 },
  mao: { born: 1893, died: 1976 },
  gandhi: { born: 1869, died: 1948 },
  hirohito: { born: 1901, died: 1989 },
};

console.log(ages(persons));
// {
//   lenin: 54,
//   mao: 83,
//   gandhi: 79,
//   hirohito: 88,
// }
"""

person = {
    'lenin': {
        'born': 1870,
        'died': 1924 
    },
    'mao': {
        'born': 1893,
        'died': 1976  
    },
    'gandhi': {
        'born': 1869,
        'died': 1948  
    },
    'hirohito': {
        'born': 1901,
        'died': 1989  
    }
}

def person_calculate(k: str) -> int:
    return person[k]['died'] - person[k]['born']

print(person_calculate('hirohito'))