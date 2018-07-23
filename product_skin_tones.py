import pandas as pd

productsDf = pd.read_excel('../data/result_v2.xlsx')
radius = 20

productSkinTones = []
for index, row in productsDf.iterrows():
    r = productsDf['R'][index]
    g = productsDf['G'][index]
    b = productsDf['B'][index]
#     rRange = range(r-radius, r+radius if r+radius < 255 else 255)
#     gRange = range(g-radius, g+radius if g+radius < 255 else 255)
#     bRange = range(b-radius, b+radius if b+radius < 255 else 255)
    rgb = (r, g, b)
#     comb = list(itertools.product(*rgb))
    productSkinTones.append(rgb)

# productSkinTones = list(set([i for sublist in productSkinTones for i in sublist]))
productSkinTonesDf = pd.DataFrame(productSkinTones)
productSkinTonesDf['HexCodes'] = ['#%02x%02x%02x' % i for i in productSkinTones]
productSkinTonesDf = productSkinTonesDf.rename(index=str, columns={0: "R", 1: "G", 2: "B"})

# # Create params for 3D scatter plot
# x = productSkinTonesDf['R'].astype('float64')
# y = productSkinTonesDf['G'].astype('float64')
# z = productSkinTonesDf['B'].astype('float64')
# productColor = list(productSkinTonesDf['HexCodes'])
# productCoveredRange = [i/800 for i in list(productsDf['Skin Tones Covered Per Product'])]