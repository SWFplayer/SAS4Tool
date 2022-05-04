import json
import main

IDs = '''
{
    "weaponIDs": {
        "Pistol": {
            "Extra": [
                {
                    "Type": 1
                }
            ],
            "Normal": [
                {
                    "Name": "HVM 001",
                    "ID": 22
                },
                {
                    "Name": "CM 202",
                    "ID": 23
                },
                {
                    "Name": "RIA 313",
                    "ID": 9
                },
                {
                    "Name": "Sabre",
                    "ID": 84
                },
                {
                    "Name": "RIA 1010",
                    "ID": 141
                },
                {
                    "Name": "Poison Claw",
                    "ID": 16
                },
                {
                    "Name": "CM 205",
                    "ID": 21
                },
                {
                    "Name": "Trailblazer",
                    "ID": 6
                },
                {
                    "Name": "CM 225",
                    "ID": 145
                },
                {
                    "Name": "Ronson 45",
                    "ID": 37
                },
                {
                    "Name": "Mustang",
                    "ID": 98
                }
            ],
            "Red": [
                {
                    "Name": "HVM 001",
                    "ID": 78
                },
                {
                    "Name": "CM 202",
                    "ID": 75
                },
                {
                    "Name": "RIA 313",
                    "ID": 110
                },
                {
                    "Name": "Sabre",
                    "ID": 67
                },
                {
                    "Name": "RIA 1010",
                    "ID": 161
                },
                {
                    "Name": "Poison Claw",
                    "ID": 111
                },
                {
                    "Name": "CM 205",
                    "ID": 70
                },
                {
                    "Name": "Trailblazer",
                    "ID": 116
                },
                {
                    "Name": "CM 225",
                    "ID": 165
                },
                {
                    "Name": "Ronson 45",
                    "ID": 77
                },
                {
                    "Name": "Mustang",
                    "ID": 68
                }
            ],
            "Black": [
                {
                    "Name": "Poison Claw",
                    "ID": 10111
                },
                {
                    "Name": "Ronson 45",
                    "ID": 10077
                },
                {
                    "Name": "Trailblazer",
                    "ID": 10116
                },
                {
                    "Name": "Mustang",
                    "ID": 10068
                }
            ],
            "Factions": [
                {
                    "Name": "GG17",
                    "ID": 221
                }
            ]
        },
        "SMG": {
            "Extra": [
                {
                    "Type": 2
                }
            ],
            "Normal": [
                {
                    "Name": "RIA 7",
                    "ID": 30
                },
                {
                    "Name": "HVM 002",
                    "ID": 17
                },
                {
                    "Name": "Phantom",
                    "ID": 89
                },
                {
                    "Name": "CM 330",
                    "ID": 148
                },
                {
                    "Name": "RIA T7",
                    "ID": 8
                },
                {
                    "Name": "CM 307",
                    "ID": 11
                },
                {
                    "Name": "CM 351 Sunflare",
                    "ID": 24
                },
                {
                    "Name": "Ronson 50",
                    "ID": 160
                },
                {
                    "Name": "Ronson 55",
                    "ID": 19
                }
            ],
            "Red": [
                {
                    "Name": "RIA 7",
                    "ID": 97
                },
                {
                    "Name": "HVM 002",
                    "ID": 94
                },
                {
                    "Name": "Phantom",
                    "ID": 106
                },
                {
                    "Name": "CM 330",
                    "ID": 168
                },
                {
                    "Name": "RIA T7",
                    "ID": 103
                },
                {
                    "Name": "CM 307",
                    "ID": 87
                },
                {
                    "Name": "CM 351 Sunflare",
                    "ID": 113
                },
                {
                    "Name": "Ronson 50",
                    "ID": 180
                },
                {
                    "Name": "Ronson 55",
                    "ID": 105
                }
            ],
            "Black": [
                {
                    "Name": "RIA 7",
                    "ID": 10097
                },
                {
                    "Name": "HVM 002",
                    "ID": 10094
                },
                {
                    "Name": "Phantom",
                    "ID": 10106
                },
                {
                    "Name": "CM 330",
                    "ID": 10168
                },
                {
                    "Name": "RIA T7",
                    "ID": 10103
                },
                {
                    "Name": "CM 307",
                    "ID": 10087
                },
                {
                    "Name": "CM 351 Sunflare",
                    "ID": 10113
                },
                {
                    "Name": "Ronson 50",
                    "ID": 10180
                },
                {
                    "Name": "Ronson 55",
                    "ID": 10105
                }
            ]
        },
        "Assault Rifle": {
            "Extra": [
                {
                    "Type": 3
                }
            ],
            "Normal": [
                {
                    "Name": "HVM 005 G-Class",
                    "ID": 31
                },
                {
                    "Name": "RIA 20 Para",
                    "ID": 14
                },
                {
                    "Name": "RIA 20 DSC",
                    "ID": 72
                },
                {
                    "Name": "RIA 20 Striker",
                    "ID": 41
                },
                {
                    "Name": "Raptor",
                    "ID": 90
                },
                {
                    "Name": "CM 440 Titan",
                    "ID": 146
                },
                {
                    "Name": "CM 401 Planet Stormer",
                    "ID": 7
                },
                {
                    "Name": "Heartburn",
                    "ID": 156
                },
                {
                    "Name": "CM Gigavolt",
                    "ID": 15
                },
                {
                    "Name": "Ronson 65-a",
                    "ID": 10
                },
                {
                    "Name": "Ronson 70",
                    "ID": 158
                },
                {
                    "Name": "CM 451 Starburst",
                    "ID": 36
                },
                {
                    "Name": "Hard Thorn",
                    "ID": 28
                },
                {
                    "Name": "Mixmaster",
                    "ID": 26
                },
                {
                    "Name": "Sub-Light COM2",
                    "ID": 12
                }
            ],
            "Red": [
                {
                    "Name": "HVM 005 G-Class",
                    "ID": 87
                },
                {
                    "Name": "RIA 20 Para",
                    "ID": 79
                },
                {
                    "Name": "RIA 20 DSC",
                    "ID": 69
                },
                {
                    "Name": "RIA 20 Striker",
                    "ID": 102
                },
                {
                    "Name": "Raptor",
                    "ID": 88
                },
                {
                    "Name": "CM 440 Titan",
                    "ID": 166
                },
                {
                    "Name": "CM 401 Planet Stormer",
                    "ID": 109
                },
                {
                    "Name": "Heartburn",
                    "ID": 176
                },
                {
                    "Name": "CM Gigavolt",
                    "ID": 115
                },
                {
                    "Name": "Ronson 65-a",
                    "ID": 100
                },
                {
                    "Name": "Ronson 70",
                    "ID": 178
                },
                {
                    "Name": "CM 451 Starburst",
                    "ID": 71
                },
                {
                    "Name": "Hard Thorn",
                    "ID": 99
                },
                {
                    "Name": "Mixmaster",
                    "ID": 76
                },
                {
                    "Name": "Sub-Light COM2",
                    "ID": 93
                }
            ],
            "Black": [
                {
                    "Name": "HVM 005 G-Class",
                    "ID": 10087
                },
                {
                    "Name": "RIA 20 Para",
                    "ID": 10079
                },
                {
                    "Name": "RIA 20 DSC",
                    "ID": 10069
                },
                {
                    "Name": "RIA 20 Striker",
                    "ID": 10102
                },
                {
                    "Name": "Raptor",
                    "ID": 10088
                },
                {
                    "Name": "CM 440 Titan",
                    "ID": 10166
                },
                {
                    "Name": "CM 401 Planet Stormer",
                    "ID": 10109
                },
                {
                    "Name": "Heartburn",
                    "ID": 10176
                },
                {
                    "Name": "CM Gigavolt",
                    "ID": 10115
                },
                {
                    "Name": "Ronson 65-a",
                    "ID": 10100
                },
                {
                    "Name": "Ronson 70",
                    "ID": 10178
                },
                {
                    "Name": "CM 451 Starburst",
                    "ID": 10071
                },
                {
                    "Name": "Hard Thorn",
                    "ID": 10099
                },
                {
                    "Name": "Mixmaster",
                    "ID": 10076
                },
                {
                    "Name": "Sub-Light COM2",
                    "ID": 10093
                }
            ],
            "Factions": [
                {
                    "Name": "Festungsbrecher",
                    "ID": 222
                }
            ]
        },
        "Shotgun": {
            "Extra": [
                {
                    "Type": 4
                }
            ],
            "Normal": [
                {
                    "Name": "HVM 004",
                    "ID": 33
                },
                {
                    "Name": "RIA 30 Strikeforce",
                    "ID": 29
                },
                {
                    "Name": "Stripper",
                    "ID": 13
                },
                {
                    "Name": "Shotlite Tempest",
                    "ID": 159
                },
                {
                    "Name": "1887 Shockfield",
                    "ID": 61
                }
            ],
            "Red": [
                {
                    "Name": "HVM 004",
                    "ID": 101
                },
                {
                    "Name": "RIA 30 Strikeforce",
                    "ID": 96
                },
                {
                    "Name": "Stripper",
                    "ID": 85
                },
                {
                    "Name": "Shotlite Tempest",
                    "ID": 179
                },
                {
                    "Name": "1887 Shockfield",
                    "ID": 66
                }
            ],
            "Black": [
                {
                    "Name": "HVM 004",
                    "ID": 10101
                },
                {
                    "Name": "RIA 30 Strikeforce",
                    "ID": 10096
                },
                {
                    "Name": "Stripper",
                    "ID": 10085
                },
                {
                    "Name": "Shotlite Tempest",
                    "ID": 10179
                },
                {
                    "Name": "1887 Shockfield",
                    "ID": 10066
                }
            ],
            "Factions": [
                {
                    "Name": "Thundershock",
                    "ID": 231
                }
            ]
        },
        "Sniper": {
            "Extra": [
                {
                    "Type": 5
                }
            ],
            "Normal": [
                {
                    "Name": "RIA 50",
                    "ID": 43
                },
                {
                    "Name": "CM 800 Jupiter",
                    "ID": 149
                },
                {
                    "Name": "HIKS S3000",
                    "ID": 39
                },
                {
                    "Name": "Hornet",
                    "ID": 83
                }
            ],
            "Red": [
                {
                    "Name": "RIA 50",
                    "ID": 107
                },
                {
                    "Name": "CM 800 Jupiter",
                    "ID": 169
                },
                {
                    "Name": "HIKS S3000",
                    "ID": 82
                },
                {
                    "Name": "Hornet",
                    "ID": 81
                }
            ],
            "Black": [
                {
                    "Name": "RIA 50",
                    "ID": 10107
                },
                {
                    "Name": "CM 800 Jupiter",
                    "ID": 10169
                },
                {
                    "Name": "HIKS S3000",
                    "ID": 10082
                },
                {
                    "Name": "Hornet",
                    "ID": 10081
                }
            ]
        },
        "Rocket Launcher": {
            "Extra": [
                {
                    "Type": 6
                }
            ],
            "Normal": [
                {
                    "Name": "HVM MPG",
                    "ID": 34
                },
                {
                    "Name": "T-101 Feldhaubitz",
                    "ID": 40
                },
                {
                    "Name": "Lone Star",
                    "ID": 151
                },
                {
                    "Name": "Gebirgskanone",
                    "ID": 33
                },
                {
                    "Name": "T-102 Jagdfaust",
                    "ID": 44
                },
                {
                    "Name": "Luftplatzen",
                    "ID": 154
                },
                {
                    "Name": "HIKS 3100",
                    "ID": 153
                }
            ],
            "Red": [
                {
                    "Name": "HVM MPG",
                    "ID": 73
                },
                {
                    "Name": "T-101 Feldhaubitz",
                    "ID": 108
                },
                {
                    "Name": "Lone Star",
                    "ID": 171
                },
                {
                    "Name": "Gebirgskanone",
                    "ID": 91
                },
                {
                    "Name": "T-102 Jagdfaust",
                    "ID": 92
                },
                {
                    "Name": "Luftplatzen",
                    "ID": 174
                },
                {
                    "Name": "HIKS 3100",
                    "ID": 173
                }
            ],
            "Black": [
                {
                    "Name": "HVM MPG",
                    "ID": 10073
                },
                {
                    "Name": "T-101 Feldhaubitz",
                    "ID": 10108
                },
                {
                    "Name": "Lone Star",
                    "ID": 10171
                },
                {
                    "Name": "Gebirgskanone",
                    "ID": 10091
                },
                {
                    "Name": "T-102 Jagdfaust",
                    "ID": 10092
                },
                {
                    "Name": "Luftplatzen",
                    "ID": 10174
                },
                {
                    "Name": "HIKS 3100",
                    "ID": 10173
                }
            ],
            "Factions": [
                {
                    "Name": "Depth Charge",
                    "ID": 228
                },
                {
                    "Name": "Havoc",
                    "ID": 224
                }
            ]
        },
        "Flame Thrower": {
            "Extra": [
                {
                    "Type": 8
                }
            ],
            "Normal": [
                {
                    "Name": "Ronson WP Flamethrower",
                    "ID": 18
                }
            ],
            "Red": [
                {
                    "Name": "Ronson WP Flamethrower",
                    "ID": 74
                }
            ],
            "Black": [
                {
                    "Name": "Ronson WP Flamethrower",
                    "ID": 10074
                }
            ],
            "Factions": [
                {
                    "Name": "Phoenix",
                    "ID": 223
                },
                {
                    "Name": "Avalanche",
                    "ID": 227
                }
            ]
        },
        "LMG": {
            "Extra": [
                {
                    "Type": 9
                }
            ],
            "Normal": [
                {
                    "Name": "HVM 005",
                    "ID": 38
                },
                {
                    "Name": "Ronson LBM",
                    "ID": 25
                },
                {
                    "Name": "RIA 40",
                    "ID": 142
                },
                {
                    "Name": "RIA 45 Para",
                    "ID": 144
                },
                {
                    "Name": "CM 505",
                    "ID": 20
                },
                {
                    "Name": "CM 530 BabyCOM",
                    "ID": 147  
                },
                {
                    "Name": "Tombstone",
                    "ID": 150
                },
                {
                    "Name": "Proposition",
                    "ID": 152
                },
                {
                    "Name": "RIA T40",
                    "ID": 143
                },
                {
                    "Name": "Supermarine",
                    "ID": 114
                }
            ],
            "Red": [
                {
                    "Name": "HVM 005",
                    "ID": 95
                },
                {
                    "Name": "Ronson LBM",
                    "ID": 104
                },
                {
                    "Name": "RIA 40",
                    "ID": 162
                },
                {
                    "Name": "RIA 45 Para",
                    "ID": 164
                },
                {
                    "Name": "CM 505",
                    "ID": 80
                },
                {
                    "Name": "CM 530 BabyCOM",
                    "ID": 167
                },
                {
                    "Name": "Tombstone",
                    "ID": 170
                },
                {
                    "Name": "Proposition",
                    "ID": 172
                },
                {
                    "Name": "RIA T40",
                    "ID": 163
                },
                {
                    "Name": "Supermarine",
                    "ID": 35
                }
            ],
            "Black": [
                {
                    "Name": "HVM 005",
                    "ID": 10095
                },
                {
                    "Name": "Ronson LBM",
                    "ID": 10104
                },
                {
                    "Name": "RIA 40",
                    "ID": 10162
                },
                {
                    "Name": "RIA 45 Para",
                    "ID": 10164
                },
                {
                    "Name": "CM 505",
                    "ID": 10080
                },
                {
                    "Name": "CM 530 BabyCOM",
                    "ID": 10167
                },
                {
                    "Name": "Tombstone",
                    "ID": 10170
                },
                {
                    "Name": "Proposition",
                    "ID": 10172
                },
                {
                    "Name": "RIA T40",
                    "ID": 10163
                },
                {
                    "Name": "Supermarine",
                    "ID": 10035
                }
            ],
            "Factions": [
                {
                    "Name": "Kraken",
                    "ID": 225
                }
            ]
        },
        "Disk Thrower": {
            "Extra": [
                {
                    "Type": 10
                }
            ],
            "Normal": [
                {
                    "Name": "Shredder",
                    "ID": 157
                }
            ],
            "Red": [
                {
                    "Name": "Shredder",
                    "ID": 177
                }
            ],
            "Black": [
                {
                    "Name": "Shredder",
                    "ID": 10177
                }
            ],
            "Factions": [
                {
                    "Name": "Exterminator",
                    "ID": 226
                }
            ]
        },
        "Laser": {
            "Extra": [
                {
                    "Type": 11
                }
            ],
            "Normal": [
                {
                    "Name": "Hotspot",
                    "ID": 155
                }
            ],
            "Red": [
                {
                    "Name": "Hotspot",
                    "ID": 175
                }
            ],
            "Black": [
                {
                    "Name": "Hotspot",
                    "ID": 10175
                }
            ],
            "Factions": [
                {
                    "Name": "Krakatoa",
                    "ID": 229
                }
            ]
        }
    },
    "equipmentIDs": {
        "Helmet": {
            "Extra": [
                {
                    "Type": 1
                }
            ],
            "Normal": [
                {
                    "Name": "HVM Kevlar Helmet",
                    "ID": 125
                },
                {
                    "Name": "Trooper Helmet",
                    "ID": 110
                },
                {
                    "Name": "HVM Carbon Fibre Helmet",
                    "ID": 184
                },
                {
                    "Name": "Shotlite Hummingbird H1",
                    "ID": 165
                },
                {
                    "Name": "Special Forces Helmet",
                    "ID": 107
                },
                {
                    "Name": "R1 Interceptor Helm",
                    "ID": 106
                },
                {
                    "Name": "Hardplate Helmet",
                    "ID": 173
                },
                {
                    "Name": "Medusa Helmet",
                    "ID": 194
                },
                {
                    "Name": "Graphene Combat Hood",
                    "ID": 99
                },
                {
                    "Name": "Dragonfly Helmet",
                    "ID": 206
                },
                {
                    "Name": "Titan IRN HUD",
                    "ID": 119
                }
            ],
            "Red": [
                {
                    "Name": "HVM Kevlar Helmet",
                    "ID": 155
                },
                {
                    "Name": "Trooper Helmet",
                    "ID": 162
                },
                {
                    "Name": "HVM Carbon Fibre Helmet",
                    "ID": 185
                },
                {
                    "Name": "Shotlite Hummingbird H1",
                    "ID": 158
                },
                {
                    "Name": "Special Forces Helmet",
                    "ID": 143
                },
                {
                    "Name": "R1 Interceptor Helm",
                    "ID": 136
                },
                {
                    "Name": "Hardplate Helmet",
                    "ID": 175
                },
                {
                    "Name": "Medusa Helmet",
                    "ID": 195
                },
                {
                    "Name": "Graphene Combat Hood",
                    "ID": 139
                },
                {
                    "Name": "Dragonfly Helmet",
                    "ID": 207
                },
                {
                    "Name": "Titan IRN HUD",
                    "ID": 130
                }
            ],
            "Black": [
                {
                    "Name": "HVM Kevlar Helmet",
                    "ID": 10155
                },
                {
                    "Name": "Trooper Helmet",
                    "ID": 10162
                },
                {
                    "Name": "HVM Carbon Fibre Helmet",
                    "ID": 10185
                },
                {
                    "Name": "Shotlite Hummingbird H1",
                    "ID": 10158
                },
                {
                    "Name": "Special Forces Helmet",
                    "ID": 10143
                },
                {
                    "Name": "R1 Interceptor Helm",
                    "ID": 10136
                },
                {
                    "Name": "Hardplate Helmet",
                    "ID": 10175
                },
                {
                    "Name": "Medusa Helmet",
                    "ID": 10195
                },
                {
                    "Name": "Graphene Combat Hood",
                    "ID": 10139
                },
                {
                    "Name": "Dragonfly Helmet",
                    "ID": 10207
                },
                {
                    "Name": "Titan IRN HUD",
                    "ID": 10130
                }
            ],
            "Factions": [
                {
                    "Name": "Dynamo Helmet",
                    "ID": 232
                },
                {
                    "Name": "Overwatch Helmet",
                    "ID": 227
                },
                {
                    "Name": "Mastodon Helm",
                    "ID": 237
                },
                {
                    "Name": "Vulkan Helmet",
                    "ID": 217
                },
                {
                    "Name": "Mako Helmet",
                    "ID": 222
                }
            ]
        },
        "Vest": {
            "Extra": [
                {
                    "Type": 2
                }
            ],
            "Normal": [
                {
                    "Name": "HVM Kevlar Vest",
                    "ID": 101
                },
                {
                    "Name": "Trooper Vest",
                    "ID": 104
                },
                {
                    "Name": "HVM Carbon Fibre Vest",
                    "ID": 186
                },
                {
                    "Name": "Shotlite Hummingbird V1",
                    "ID": 168
                },
                {
                    "Name": "Special Forces Vest",
                    "ID": 100
                },
                {
                    "Name": "R4 Guardian Vest",
                    "ID": 118
                },
                {
                    "Name": "Rubicon Power Assist",
                    "ID": 105
                },
                {
                    "Name": "Heavy Trooper Vest",
                    "ID": 112
                },
                {
                    "Name": "Medusa Vest",
                    "ID": 196
                },
                {
                    "Name": "Hardplate Chest",
                    "ID": 176
                },
                {
                    "Name": "Dragonfly Vest",
                    "ID": 208
                },
                {
                    "Name": "Graphene Body Suit Top",
                    "ID": 115
                },
                {
                    "Name": "Titan Teslashock",
                    "ID": 123
                }
            ],
            "Red": [
                {
                    "Name": "HVM Kevlar Vest",
                    "ID": 142
                },
                {
                    "Name": "Trooper Vest",
                    "ID": 148
                },
                {
                    "Name": "HVM Carbon Fibre Vest",
                    "ID": 187
                },
                {
                    "Name": "Shotlite Hummingbird V1",
                    "ID": 156
                },
                {
                    "Name": "Special Forces Vest",
                    "ID": 154
                },
                {
                    "Name": "R4 Guardian Vest",
                    "ID": 141
                },
                {
                    "Name": "Rubicon Power Assist",
                    "ID": 137
                },
                {
                    "Name": "Heavy Trooper Vest",
                    "ID": 164
                },
                {
                    "Name": "Medusa Vest",
                    "ID": 197
                },
                {
                    "Name": "Hardplate Chest",
                    "ID": 177
                },
                {
                    "Name": "Dragonfly Vest",
                    "ID": 209
                },
                {
                    "Name": "Graphene Body Suit Top",
                    "ID": 161
                },
                {
                    "Name": "Titan Teslashock",
                    "ID": 157
                }
            ],
            "Black": [
                {
                    "Name": "HVM Kevlar Vest",
                    "ID": 10142
                },
                {
                    "Name": "Trooper Vest",
                    "ID": 10148
                },
                {
                    "Name": "HVM Carbon Fibre Vest",
                    "ID": 10187
                },
                {
                    "Name": "Shotlite Hummingbird V1",
                    "ID": 10156
                },
                {
                    "Name": "Special Forces Vest",
                    "ID": 10154
                },
                {
                    "Name": "R4 Guardian Vest",
                    "ID": 10141
                },
                {
                    "Name": "Rubicon Power Assist",
                    "ID": 10137
                },
                {
                    "Name": "Heavy Trooper Vest",
                    "ID": 10164
                },
                {
                    "Name": "Medusa Vest",
                    "ID": 10197
                },
                {
                    "Name": "Hardplate Chest",
                    "ID": 10177
                },
                {
                    "Name": "Dragonfly Vest",
                    "ID": 10209
                },
                {
                    "Name": "Graphene Body Suit Top",
                    "ID": 10161
                },
                {
                    "Name": "Titan Teslashock",
                    "ID": 10157
                }
            ],
            "Factions": [
                {
                    "Name": "Dynamo Chest",
                    "ID": 233
                },
                {
                    "Name": "Overwatch Chest",
                    "ID": 228
                },
                {
                    "Name": "Mastodon Chest",
                    "ID": 238
                },
                {
                    "Name": "Vulkan Vest",
                    "ID": 223
                },
                {
                    "Name": "Mako Vest",
                    "ID": 218
                }
            ]
        },
        "Gloves": {
            "Extra": [
                {
                    "Type": 3
                }
            ],
            "Normal": [
                {
                    "Name": "HVM Kevlar Gloves",
                    "ID": 98
                },
                {
                    "Name": "Trooper Gloves",
                    "ID": 102
                },
                {
                    "Name": "HVM Carbon Fibre Gloves",
                    "ID": 190
                },
                {
                    "Name": "Shotlite Hummingbird G1",
                    "ID": 151
                },
                {
                    "Name": "Special Forces Gloves",
                    "ID": 128
                },
                {
                    "Name": "R6 Flamejuggler Gloves",
                    "ID": 117
                },
                {
                    "Name": "Dragonfly Gloves",
                    "ID": 212
                },
                {
                    "Name": "Hardplate Gauntlets",
                    "ID": 180
                },
                {
                    "Name": "Medusa Gloves",
                    "ID": 200
                },
                {
                    "Name": "Graphene Gloves",
                    "ID": 113
                },
                {
                    "Name": "Titan IDS 01",
                    "ID": 111
                }
            ],
            "Red": [
                {
                    "Name": "HVM Kevlar Gloves",
                    "ID": 146
                },
                {
                    "Name": "Trooper Gloves",
                    "ID": 133
                },
                {
                    "Name": "HVM Carbon Fibre Gloves",
                    "ID": 191
                },
                {
                    "Name": "Shotlite Hummingbird G1",
                    "ID": 145
                },
                {
                    "Name": "Special Forces Gloves",
                    "ID": 132
                },
                {
                    "Name": "R6 Flamejuggler Gloves",
                    "ID": 181
                },
                {
                    "Name": "Dragonfly Gloves",
                    "ID": 159
                },
                {
                    "Name": "Hardplate Gauntlets",
                    "ID": 213
                },
                {
                    "Name": "Medusa Gloves",
                    "ID": 201
                },
                {
                    "Name": "Graphene Gloves",
                    "ID": 134
                },
                {
                    "Name": "Titan IDS 01",
                    "ID": 135
                }
            ],
            "Black": [
                {
                    "Name": "HVM Kevlar Gloves",
                    "ID": 10146
                },
                {
                    "Name": "Trooper Gloves",
                    "ID": 10133
                },
                {
                    "Name": "HVM Carbon Fibre Gloves",
                    "ID": 10191
                },
                {
                    "Name": "Shotlite Hummingbird G1",
                    "ID": 10145
                },
                {
                    "Name": "Special Forces Gloves",
                    "ID": 10132
                },
                {
                    "Name": "R6 Flamejuggler Gloves",
                    "ID": 10181
                },
                {
                    "Name": "Dragonfly Gloves",
                    "ID": 10159
                },
                {
                    "Name": "Hardplate Gauntlets",
                    "ID": 10213
                },
                {
                    "Name": "Medusa Gloves",
                    "ID": 10201
                },
                {
                    "Name": "Graphene Gloves",
                    "ID": 10134
                },
                {
                    "Name": "Titan IDS 01",
                    "ID": 10135
                }
            ],
            "Factions": [
                {
                    "Name": "Dynamo Gloves",
                    "ID": 235
                },
                {
                    "Name": "Overwatch Gloves",
                    "ID": 230
                },
                {
                    "Name": "Mastodon Gloves",
                    "ID": 240
                },
                {
                    "Name": "Mako Gloves",
                    "ID": 225
                },
                {
                    "Name": "Vulkan Gloves",
                    "ID": 220
                }
            ]
        },
        "Pants": {
            "Extra": [
                {
                    "Type": 5
                }
            ],
            "Normal": [
                {
                    "Name": "HVM Kevlar Pants",
                    "ID": 108
                },
                {
                    "Name": "Trooper Pants",
                    "ID": 129
                },
                {
                    "Name": "HVM Carbon Fibre Pants",
                    "ID": 188
                },
                {
                    "Name": "Shotlite Hummingbird P1",
                    "ID": 169
                },
                {
                    "Name": "Special Forces Pants",
                    "ID": 126
                },
                {
                    "Name": "R7 Guardian Pants",
                    "ID": 120
                },
                {
                    "Name": "Hardplate Leg Protection",
                    "ID": 178
                },
                {
                    "Name": "Medusa Pants",
                    "ID": 198
                },
                {
                    "Name": "Dragonfly Pants",
                    "ID": 210
                },
                {
                    "Name": "Graphene Body Suit Bottom",
                    "ID": 117
                },
                {
                    "Name": "Titan MEM Trooper",
                    "ID": 121
                }
            ],
            "Red": [
                {
                    "Name": "HVM Kevlar Pants",
                    "ID": 147
                },
                {
                    "Name": "Trooper Pants",
                    "ID": 166
                },
                {
                    "Name": "HVM Carbon Fibre Pants",
                    "ID": 153
                },
                {
                    "Name": "Shotlite Hummingbird P1",
                    "ID": 152
                },
                {
                    "Name": "Special Forces Pants",
                    "ID": 189
                },
                {
                    "Name": "R7 Guardian Pants",
                    "ID": 138
                },
                {
                    "Name": "Hardplate Leg Protection",
                    "ID": 179
                },
                {
                    "Name": "Medusa Pants",
                    "ID": 211
                },
                {
                    "Name": "Dragonfly Pants",
                    "ID": 199
                },
                {
                    "Name": "Graphene Body Suit Bottom",
                    "ID": 163
                },
                {
                    "Name": "Titan MEM Trooper",
                    "ID": 171
                }
            ],
            "Black": [
                {
                    "Name": "HVM Kevlar Pants",
                    "ID": 10147
                },
                {
                    "Name": "Trooper Pants",
                    "ID": 10166
                },
                {
                    "Name": "HVM Carbon Fibre Pants",
                    "ID": 10153
                },
                {
                    "Name": "Shotlite Hummingbird P1",
                    "ID": 10152
                },
                {
                    "Name": "Special Forces Pants",
                    "ID": 10189
                },
                {
                    "Name": "R7 Guardian Pants",
                    "ID": 10138
                },
                {
                    "Name": "Hardplate Leg Protection",
                    "ID": 10179
                },
                {
                    "Name": "Medusa Pants",
                    "ID": 10211
                },
                {
                    "Name": "Dragonfly Pants",
                    "ID": 10199
                },
                {
                    "Name": "Graphene Body Suit Bottom",
                    "ID": 10163
                },
                {
                    "Name": "Titan MEM Trooper",
                    "ID": 10171
                }
            ],
            "Factions": [
                {
                    "Name": "Dynamo Pants",
                    "ID": 234
                },
                {
                    "Name": "Overwatch Pants",
                    "ID": 229
                },
                {
                    "Name": "Mastodon Pants",
                    "ID": 239
                },
                {
                    "Name": "Mako Pants",
                    "ID": 224
                },
                {
                    "Name": "Vulkan Pants",
                    "ID": 219
                }
            ]
        },
        "Boots": {
            "Extra": [
                {
                    "Type": 4
                }
            ],
            "Normal": [
                {
                    "Name": "HVM Kevlar Boots",
                    "ID": 114
                },
                {
                    "Name": "Trooper Boots",
                    "ID": 109
                },
                {
                    "Name": "Special Forces Boots",
                    "ID": 116
                },
                {
                    "Name": "Shotlite Starwalk Boots",
                    "ID": 144
                },
                {
                    "Name": "HVM Carbon Fibre Boots",
                    "ID": 192
                },
                {
                    "Name": "R8 Huntsman Boots",
                    "ID": 122
                },
                {
                    "Name": "Hardplate Boots",
                    "ID": 182
                },
                {
                    "Name": "Medusa Boots",
                    "ID": 202
                },
                {
                    "Name": "Dragonfly Boots",
                    "ID": 214
                },
                {
                    "Name": "Graphene Boots",
                    "ID": 103
                },
                {
                    "Name": "Titan MEM Sprint",
                    "ID": 124
                }
            ],
            "Red": [
                {
                    "Name": "HVM Kevlar Boots",
                    "ID": 131
                },
                {
                    "Name": "Trooper Boots",
                    "ID": 160
                },
                {
                    "Name": "Special Forces Boots",
                    "ID": 149
                },
                {
                    "Name": "Shotlite Starwalk Boots",
                    "ID": 152
                },
                {
                    "Name": "HVM Carbon Fibre Boots",
                    "ID": 193
                },
                {
                    "Name": "R8 Huntsman Boots",
                    "ID": 140
                },
                {
                    "Name": "Hardplate Boots",
                    "ID": 205
                },
                {
                    "Name": "Medusa Boots",
                    "ID": 183
                },
                {
                    "Name": "Dragonfly Boots",
                    "ID": 215
                },
                {
                    "Name": "Graphene Boots",
                    "ID": 170
                },
                {
                    "Name": "Titan MEM Sprint",
                    "ID": 167
                }
            ],
            "Black": [
                {
                    "Name": "HVM Kevlar Boots",
                    "ID": 10131
                },
                {
                    "Name": "Trooper Boots",
                    "ID": 10160
                },
                {
                    "Name": "Special Forces Boots",
                    "ID": 10149
                },
                {
                    "Name": "Shotlite Starwalk Boots",
                    "ID": 10152
                },
                {
                    "Name": "HVM Carbon Fibre Boots",
                    "ID": 10193
                },
                {
                    "Name": "R8 Huntsman Boots",
                    "ID": 10140
                },
                {
                    "Name": "Hardplate Boots",
                    "ID": 10205
                },
                {
                    "Name": "Medusa Boots",
                    "ID": 10183
                },
                {
                    "Name": "Dragonfly Boots",
                    "ID": 10215
                },
                {
                    "Name": "Graphene Boots",
                    "ID": 10170
                },
                {
                    "Name": "Titan MEM Sprint",
                    "ID": 10167
                }
            ],
            "Factions": [
                {
                    "Name": "Dynamo Boots",
                    "ID": 236
                },
                {
                    "Name": "Overwatch Boots",
                    "ID": 231
                },
                {
                    "Name": "Vulkan Boots",
                    "ID": 221
                },
                {
                    "Name": "Mastodon Boots",
                    "ID": 241
                },
                {
                    "Name": "Mako Boots",
                    "ID": 226
                }
            ]
        }
    },
    "TurretsIDs": {
        "Normal": [
            {
                "Name": "HVM Heavy Machine Gun Sentry",
                "ID": 54
            },
            {
                "Name": "Ronson Cryogenic Turret",
                "ID": 56
            },
            {
                "Name": "HIK Heavyshot Protector",
                "ID": 58
            },
            {
                "Name": "Teknoboom Flugkorper",
                "ID": 62
            },
            {
                "Name": "Ronson MK V Flame Turret",
                "ID": 63
            },
            {
                "Name": "CM Supernova",
                "ID": 60
            },
            {
                "Name": "CM Zeus Exclusion Zone",
                "ID": 55
            }
        ],
        "Red": [
            {
                "Name": "HVM Heavy Machine Gun Sentry",
                "ID": 133
            },
            {
                "Name": "Ronson Cryogenic Turret",
                "ID": 134
            },
            {
                "Name": "HIK Heavyshot Protector",
                "ID": 135
            },
            {
                "Name": "Teknoboom Flugkorper",
                "ID": 136
            },
            {
                "Name": "Ronson MK V Flame Turret",
                "ID": 137
            },
            {
                "Name": "CM Supernova",
                "ID": 138
            },
            {
                "Name": "CM Zeus Exclusion Zone",
                "ID": 139
            }
        ]
    }
}
'''

def createFile():
    sF = main.getSteamFolder()
    mainDir = main.getFolder(sF)
    open(f'{mainDir}\\IDs.json', 'w').close()
    with open(f'{mainDir}\\IDs.json', 'r+') as f:
        data = json.loads(IDs)
        f.seek(0)
        f.truncate()
        json.dump(data, f, indent=4)
