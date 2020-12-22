 
products_list ={
    
    'id_134324':{
    'name': 'Bosh sms40t32',
    'maker' : 'Bosh',
    'appliance' : 'Dishwasher',
    'Year' : 2018,
    'image': 'id_134324.jpg',
    'Internal article number' : 'SMS40T32GB',
    'Market': 'EU',
    'problems': [
        {"id": 1, "description" : "Detergent does not dissolve"},
        {"id": 2, "description" : "Does not function"},
        {"id": 3, "description" : "Door function defective"},
        {"id": 4, "description" : "Error in the programme sequence"},
        {"id": 5, "description" : "Not draining / water in the appliance"},
        {"id": 6, "description" : "Other function problem"},
        {"id": 7, "description" : "Water not running in"},
        {"id": 8, "description" : "Error code / error display / signal"}
    ]

    },
    'id_134325':{
    'name': 'KDW60S20',
    'maker' : 'KENWOOD',
    'appliance' : 'Dishwasher',
    'Year' : 2019,
    'image': 'imma2.jpg',
    'Internal article number' : '3243256765A',
    'Market': 'EU',
        'problems': [
        {"id": 1, "description" : "Detergent does not dissolve"},
        {"id": 2, "description" : "Does not function"},
        {"id": 3, "description" : "Door function defective"},
        {"id": 4, "description" : "Error in the programme sequence"},
        {"id": 5, "description" : "Not draining / water in the appliance"},
        {"id": 6, "description" : "Other function problem"},
        {"id": 7, "description" : "Water not running in"},
        {"id": 8, "description" : "Error code / error display / signal"}
    ]
    },
    'id_134326':{
    'name': 'Bosh KUF55X18',
    'maker' : 'KENWOOD',
    'appliance' : 'Dishwasher',
    'Year' : 2018,
    'image': 'imma3.jpg',
    'Internal article number' : '4537658kL££',
    'Market': 'EU',
        'problems': [
        {"id": 1, "description" : "Detergent does not dissolve"},
        {"id": 2, "description" : "Does not function"},
        {"id": 3, "description" : "Door function defective"},
        {"id": 4, "description" : "Error in the programme sequence"},
        {"id": 5, "description" : "Not draining / water in the appliance"},
        {"id": 6, "description" : "Other function problem"},
        {"id": 7, "description" : "Water not running in"},
        {"id": 8, "description" : "Error code / error display / signal"}
    ]
    
    }

}


Resolutions_list ={
    'id_134324':{

                '1': {"id": '1' ,
                'image': 'id_134324_res.jpg',
                'targets':[{"id":15,"x":100,"y":150}],
                 "description": "Waste water pump not working",
                 "steps":[
                            {"id": 1,
                             "Description": "First always disconnect the appliance from the power supply.",
                             "target": []
                            },

                            {"id": 2,
                             "Description": "Take out top basket and bottom basket",
                             "target": []
                            },


                            {"id": 3,
                             "Description": "Remove the filters 1R",
                             "target": [15]
                            },


                            {"id": 4,
                             "Description": "Scoop out water, use a sponge if required",
                             "target": []
                            },


                            {"id": 5,
                             "Description": "Prise out the white pump cover(as illustrated) using a spoon.",
                             "target": []
                            },


                         ]
                },
               '2':  {"id": '2' ,
               'image': 'imma3_res.jpg',
                 "description": "Connect the power",
                 "steps":[
                            {"id": 1,
                             "Description": "Check if the power is connected on the back",
                             "target": []
                            }

                         ]
                }

        },
    'id_134326':{

                '1': {"id": '1' ,
                'image': 'id_134324_res.jpg',
                 "description": "Waste water pump not working",
                 "steps":[
                            {"id": 1,
                             "Description": "First always disconnect the appliance from the power supply.",
                             "target": []
                            },

                            {"id": 2,
                             "Description": "Take out top basket and bottom basket",
                             "target": []
                            },


                            {"id": 3,
                             "Description": "Remove the filters 1R",
                             "target": [15]
                            },


                            {"id": 4,
                             "Description": "Scoop out water, use a sponge if required",
                             "target": []
                            },


                            {"id": 5,
                             "Description": "Prise out the white pump cover(as illustrated) using a spoon.",
                             "target": []
                            },


                         ]
                },
               '2':  {"id": '2' ,
               'image': 'id_134324_res.jpg',
                 "description": "Connect the power",
                 "steps":[
                            {"id": 1,
                             "Description": "Check if the power is connected on the back",
                             "target": []
                            }

                         ]
                }

        }

}


recommendation_matrix ={
    'id_134324':{
    
        '1':[('1',0.90),('2',0.10)],
        '2':[('1',0.90),('2',0.10)],
        '3':[('1',0.90),('2',0.10)],
        '4':[('1',0.90),('2',0.10)],
        '5':[('1',0.90),('2',0.10)],
        '6':[('1',0.90),('2',0.10)],
        '7':[('1',0.90),('2',0.10)],
        '8':[('1',0.90),('2',0.10)],
        '9':[('1',0.90),('2',0.10)]
    },
    'id_134326':{
    
        '1':[('1',0.90),('2',0.10)],
        '2':[('1',0.90),('2',0.10)],
        '3':[('1',0.90),('2',0.10)],
        '4':[('1',0.90),('2',0.10)],
        '5':[('1',0.90),('2',0.10)],
        '6':[('1',0.90),('2',0.10)],
        '7':[('1',0.90),('2',0.10)],
        '8':[('1',0.90),('2',0.10)],
        '9':[('1',0.90),('2',0.10)]
    },
}






