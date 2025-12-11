#!/usr/bin/env python3



def find_the_redheads(family_members):
   
    is_redhead = lambda name: family_members[name] == 'red'

    
    redhead_names_filter = filter(is_redhead, family_members.keys())

    
    return list(redhead_names_filter)



    
family_data = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}


redhead_list = find_the_redheads(family_data)


print(redhead_list)
