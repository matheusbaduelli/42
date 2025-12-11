#!/usr/bin/env python3


women_scientists = {
"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

def famous_births(pessoas):
    odernadas  =  sorted(
        pessoas.values(),
        key=lambda pessoa: int(pessoa["date_of_birth"])
    )

    for pessoa in odernadas:
        print(pessoa)


famous_births(women_scientists)    