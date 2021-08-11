FOREGROUNDCOLORS = {
    "colors": {
        "black": 30, "red": 31,
        "green": 32, "yellow": 33,
        "blue": 34, "purple": 35,
        "darkGreen": 36, "white": 37
    },
    "keys": [
        "black", "red", "green", "yellow", "blue", "purple", "darkGreen", "white"
    ],
    "length": 8
}

BACKGROUNDCOLORS = {
    "colors": {
        "black": 40, "red": 41,
        "green": 42, "yellow": 43,
        "blue": 44, "purple": 45,
        "darkGreen": 46, "white": 47
    },
    "keys": [
        "black", "red", "green", "yellow", "blue", "purple", "darkGreen", "white"
    ],
    "length": 8
}


def paintedStr(s, color):
    return "\u001b[%dm%s\u001b[0m" % (FOREGROUNDCOLORS["colors"][color], s)


def paintedStrBg(s, color):
    return "\u001b[%dm%s\u001b[0m" % (BACKGROUNDCOLORS["colors"][color], s)

