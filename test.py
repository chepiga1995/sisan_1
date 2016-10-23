import numpy as np




Y = np.matrix([[198.0, 199.0], [269.0, 253.0], [220.0, 253.0], [172.0, 253.0], [132.0, 132.0], [318.0, 290.0], [367.0, 381.0], [489.0, 381.0], [636.0, 749.0], [1144.0, 1238.0], [38.0, 23.0], [40.0, 24.0], [92.0, 70.0], [138.0, 117.0], [10.0, 15.0], [35.0, 64.0], [19.0, 23.0], [28.0, 29.0], [31.0, 22.0], [120.0, 124.0], [30.0, 35.0], [33.0, 39.0], [61.0, 40.0], [76.0, 45.0], [23.0, 28.0], [69.0, 21.0], [33.0, 28.0], [27.0, 22.0], [77.0, 28.0], [27.0, 27.0], [274.0, 102.0], [368.0, 102.0], [32.0, 74.0], [63.0, 74.0], [106.0, 138.0], [208.0, 136.0], [20.0, 23.0], [29.0, 29.0], [71.0, 44.0], [26.0, 30.0], [36.0, 41.0], [40.0, 74.0], [52.0, 74.0], [60.0, 74.0], [72.0, 54.0], [72.0, 41.0], [18.0, 18.0], [20.0, 28.0], [40.0, 36.0], [62.0, 38.0]])
F = np.matrix( [[18.613393793312362, 135.96020496547783], [304.4548501183643, 263.2556609521199], [304.4548501183643, 263.2556609521199], [304.4548501183643, 263.2556609521199], [147.28932610547412, 166.36051222007998], [384.75919744144005, 283.0956333186985], [399.77450284538986, 417.0045565707037], [399.77450284538986, 417.0045565707037], [656.3458985315909, 706.5603438862], [950.5137809987999, 1215.494621519377], [101.02805243889483, 43.946298902393664], [75.05983004234442, 45.6435312674791], [103.76094978242207, 80.5561091265259], [139.23958183942997, 123.14346559066914], [66.84892964955284, 37.11798228442284], [133.73460706287264, 74.88142777235814], [66.92489647981765, 41.176545309182345], [102.83926208023128, 48.61848019843352], [75.56294401416268, 41.659959420393875], [97.79748338401072, 122.70595543082567], [114.77329213227618, 52.8961117634061], [82.8362680384698, 64.19165529607207], [62.06579975792962, 58.64233766044391], [52.33088556786917, 65.83734678299454], [47.52363821762593, 46.113179715067545], [102.9650760483252, 39.982837752194655], [67.84369154262612, 46.323199291498355], [89.79145293382682, 41.37451032485621], [92.88576270289799, 46.10864661072726], [76.02785161837795, 45.73457981243652], [235.19859464166277, 92.15121265334673], [235.19859464166277, 92.15121265334673], [67.81944537605528, 80.54116954957414], [67.81944537605528, 80.54116954957414], [173.29371085841817, 145.77801036611206], [176.3067171543441, 145.28820416994608], [73.7520942522587, 43.39938152273835], [83.53158250818299, 48.40579989602343], [93.48027943995784, 63.313034919924775], [68.76975166952701, 48.59346124770585], [73.41636468201288, 58.8169152171221], [121.16832224687082, 87.08530059019274], [117.06974378679259, 87.07067935273054], [117.06974378679259, 87.07067935273054], [99.19096413266901, 68.07107103264354], [85.09512279996412, 56.74421025495242], [90.31456520945221, 39.28234212940421], [94.99468081872324, 46.07687190514086], [96.99582724160231, 54.00408763395431], [88.42589204873349, 53.084043567885516]])
n = 50

from plot import plot

plot(Y, F, n)