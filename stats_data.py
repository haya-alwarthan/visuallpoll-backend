import sys

data = {
    0:{
        'Completed': 150,
        'In_Progress': 200,
        'Not_assigned': 50,
    },
        1:{
        'Completed': 23,
        'In_Progress': 12,
        'Not_assigned': 7,
    },
        2:{
        'Completed': 670,
        'In_Progress': 102,
        'Not_assigned': 69,
    },

        3:{
        'Completed': 1899,
        'In_Progress': 220,
        'Not_assigned': 254,
    },
        4:{
        'Completed': 430,
        'In_Progress': 219,
        'Not_assigned': 206,
    },
        5:{
    'Completed': 90,
        'In_Progress': 123,
        'Not_assigned': 307,

    },
        6:{
      
            'Completed': 0,
        'In_Progress': 9,
        'Not_assigned': 0,

    },
        7:{
        'Completed': 102,
        'In_Progress': 289,
        'Not_assigned': 103,

    },
        8:{
        'Completed': 63,
        'In_Progress': 92,
        'Not_assigned': 54,
    },
        9:{
        'Completed': 232,
        'In_Progress': 329,
        'Not_assigned': 129,
    },
        10:{
        'Completed': 23,
        'In_Progress': 32,
        'Not_assigned': 40,
    },
}
def getClassesStats():
    return data 
def getStatusTotal():
    total={'Completed':0,'In_Progress':0,'Not_assigned':0}
    for outter in total.keys():
        for key,value in data.items():
            total[outter]+=value[outter]
    return total

print(getStatusTotal())
