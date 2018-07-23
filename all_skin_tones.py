import colorsys # Convert RGB values to hsv
import itertools
import pandas as pd

# Function to convert RGB values to YCbCr
def rgb_to_ycbcr(R, G, B): # in (0,255) range
    Y = .299 * R + .587 * G + .114 * B
    Cb = 128 - .168736 * R - .331364 * G + .5 * B
    Cr = 128 + .5 * R - .418688 * G - .081312 * B
#     Y = .299 * R + .287 * G + .11 * B
#     Cr = R - Y
#     Cb = B - Y
    return Y, Cb, Cr

# Construct RGB values tuple
rgb = (range(94, 256), range(40, 256), range(0, 256))

# Find all RGB combinations
comb = list(itertools.product(*rgb))

# Convert RGB values to HSV and YCbCr and add them to the end of the RGB tuple
rgbhsvycbcr = []
for i in comb:
    addToRgb = i + colorsys.rgb_to_hsv(i[0], i[1], i[2]) + rgb_to_ycbcr(i[0], i[1], i[2])
    rgbhsvycbcr.append(addToRgb)

# "Human Skin Detection Using RGB, HSV and YCbCr Color Models":
# https://arxiv.org/ftp/arxiv/papers/1708/1708.02694.pdf
# rgbhsvycbcr = [r, g, b, h, s, v, y, cb, cr]
# testRgbhsvycbcr = [(95, 40, 22, 0.16666666666666666, 0.5, 95, 54.16499999999999, 108.71552, 157.12624)]
filteredSkinTones = []
for i in rgbhsvycbcr:
    if ((i[0] > i[1]) and (i[0] > i[2]) and (i[0] - i[1] > 15) and \
    (i[3] <= 50 and i[3] >= 0 and i[4] <= 0.68 and i[4] > 0.1)) or \
    ((i[0] > i[1]) and (i[0] > i[2]) and (i[0] - i[1] > 15) and \
    (i[8] > 135 and i[7] > 85 and i[6] > 8) and \
    (i[8] <= (1.5862 * i[7]) + 34) and \
    (i[8] >= (0.3448 * i[7]) + 76.2069) and \
    (i[8] >= (-4.5652 * i[7]) + 234.5652) and \
    (i[8] <= (-1.15 * i[7]) + 301.75) and \
    (i[8] <= (-2.2857 * i[7]) + 432.85)):
        filteredSkinTones.append(i)

# Get only RGB values from rgbhsvycbcr tuples
allSkinTones = [i[0:3] for i in filteredSkinTones]

# Construct a dataframe of RGB and Hexcodes
allSkinTonesDf = pd.DataFrame(allSkinTones)
allSkinTonesDf['HexCodes'] = ['#%02x%02x%02x' % i for i in allSkinTones]
allSkinTonesDf = allSkinTonesDf.rename(index=str, columns={0: "R", 1: "G", 2: "B"})
allSkinTonesDf.head(5)

# # Create params for 3D scatter plot
# R = allSkinTonesDf['R'].astype('float64')
# G = allSkinTonesDf['G'].astype('float64')
# B = allSkinTonesDf['B'].astype('float64')
# allSkinTonesColor = allSkinTonesDf['HexCodes']