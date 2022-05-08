import numpy as np


def positions():
    return {
        1: "Goalkeepers",
        2: "Defenders",
        3: "Midfielders",
        4: "Forwards"
    }


# list of possible formations
def formations():
    return (
        {
            "Goalkeepers": 1,
            "Defenders": 5,
            "Midfielders": 4,
            "Forwards": 1
        },
        {
            "Goalkeepers": 1,
            "Defenders": 5,
            "Midfielders": 3,
            "Forwards": 2
        },
        {
            "Goalkeepers": 1,
            "Defenders": 5,
            "Midfielders": 2,
            "Forwards": 3
        },
        {
            "Goalkeepers": 1,
            "Defenders": 4,
            "Midfielders": 5,
            "Forwards": 1
        },
        {
            "Goalkeepers": 1,
            "Defenders": 4,
            "Midfielders": 4,
            "Forwards": 2
        },
        {
            "Goalkeepers": 1,
            "Defenders": 4,
            "Midfielders": 3,
            "Forwards": 3
        },
        {
            "Goalkeepers": 1,
            "Defenders": 3,
            "Midfielders": 5,
            "Forwards": 2
        },
        {
            "Goalkeepers": 1,
            "Defenders": 3,
            "Midfielders": 4,
            "Forwards": 3
        },
    )
