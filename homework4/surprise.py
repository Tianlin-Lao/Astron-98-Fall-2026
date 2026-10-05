# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
# 2) Write a function that uses a loop to print the name of each star with its spectral type.
# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
# 4) Look up another target, add all the necessary information to the targets list. 
# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
# 6) What is your favorite constellation?
def name_print(targets):
    for i in targets:
        print(i)

name_print(targets)

def name_spec_print(targets):
    for i in targets:
        print(i, targets[i]['RA'])

name_spec_print(targets)

def greater(targets):
    ans = []
    for i in targets:
        if targets[i]['Magnitude'] < 0.1:
            ans.append(i)
    return ans

print(greater(targets))

targets['Alpha_Centauri'] = {'RA': '14h 39m 36.5s', 'Dec': 	'−60° 50′ 02″', 'Magnitude': 0.01, 'Spectral Type': 'G2V'}
print(targets)

def find_bright_20(targets):
    ans = None
    m = -9999999999
    for i in targets:
        dec = abs(float(targets[i]['Dec'][1:2]) - 20)
        if dec + targets[i]['Magnitude'] > m:
            ans = i
            m = dec - targets[i]['Magnitude']
    return ans

print(find_bright_20(targets))

print('Gemini')


