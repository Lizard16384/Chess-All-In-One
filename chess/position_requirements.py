def return_data():
    # Restrictions
    data = {"groups":[
                {"name":"chain","amount":124,"start":[],"end":[]},
                {"name":"blockA","amount":5,"start":[],"end":[]},
                {"name":"blockB","amount":5,"start":[],"end":[]},
                {"name":"blockC","amount":5,"start":[],"end":[]},
                {"name":"blockD","amount":5,"start":[],"end":[]}
            ],
            "extra_connections":[
            ],
            "disconnections":[
            ],
            "individual":[
                ]
            ,"offsets":[
            ]
            } # e

    # Assumed that these are already neighbors.
    conditionals = []

    # Define the area to work with
    size = {"x":12,"y":1,"z":12}

    fixed_positions = {"blockA1":[2,0,0],"blockA3":[0,0,0],"blockA5":[0,0,2],
                       "blockB1":[0,0,9],"blockB3":[0,0,11],"blockB5":[2,0,11],
                       "blockC1":[9,0,11],"blockC3":[11,0,11],"blockC5":[11,0,9],
                       "blockD1":[11,0,2],"blockD3":[11,0,0],"blockD5":[9,0,0]}

    origin = [6,2,6]

    return data, fixed_positions, conditionals, size, origin
