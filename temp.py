import math
d2r = math.pi/180

def convert_stars_to_radians(stars, d2r):
    for i in range(len(stars)):
        print(stars[i])
        stars[i][2] *= d2r
        stars[i][3] *= d2r
    return stars

# Usage
stars = [[677,2.1,2.097,29.09],[746,2.3,2.295,59.15],[765,3.9,2.353,-45.75],[1067,2.8,3.309,15.18],[1562,3.6,4.857,-8.82],[1599,4.2,5.018,-64.87],[1645,5.4,5.149,8.19],
[2021,2.8,6.438,-77.25],[2072,3.9,6.551,-43.68],[2081,2.4,6.571,-42.31],[2484,4.4,7.886,-62.96],
[2920,3.7,9.243,53.9],[3092,3.3,9.832,30.86],[3179,2.2,10.127,56.54],[3419,2,10.897,-17.99],
[3760,5.9,12.073,7.3],[3821,3.5,12.276,57.82],[3881,4.5,12.454,41.08],[4427,2.1,14.177,60.72],
[4436,3.9,14.188,38.5],[4577,4.3,14.652,-29.36],[4889,5.5,15.705,31.8],[4906,4.3,15.736,7.89],
[5165,3.3,16.521,-46.72],[5348,3.9,17.096,-55.25],[5364,3.5,17.147,-10.18],[5447,2.1,17.433,35.62],
[5742,4.7,18.437,24.58],[6193,4.7,19.867,27.26],[6537,3.6,21.006,-8.18],[6686,2.7,21.454,60.24],
[6867,3.4,22.091,-43.32],[7007,4.8,22.546,6.14],[7083,3.9,22.813,-49.07],[7097,3.6,22.871,15.35],
[7588,0.5,24.429,-57.24],[7607,3.6,24.498,48.63],[7884,4.5,25.358,5.49],[8102,3.5,26.017,-15.94],
[8198,4.3,26.348,9.16],[8645,3.7,27.865,-10.34],[8796,3.4,28.27,29.58],[8832,3.9,28.383,19.29],
[8833,4.6,28.389,3.19],[8837,4.4,28.411,-46.3],[8886,3.4,28.599,63.67],[8903,2.6,28.66,20.81],
[9007,3.7,28.989,-51.61],[9236,2.9,29.692,-61.57],[9347,4,30.001,-21.08],[9487,3.8,30.512,2.76],
[9598,4,30.859,72.42],[9640,2.1,30.975,42.33],[9884,2,31.793,23.46],[10064,3,32.386,34.99],
[10324,4.4,33.25,8.85],[10559,5.3,33.985,33.36],[10602,3.6,34.127,-51.51],[10826,6.5,34.837,-2.98],
[11001,4.1,35.437,-68.66],[11345,4.9,36.488,-12.29],[11407,4.2,36.746,-47.7],[11484,4.3,37.04,8.46],
[11767,2,37.955,89.26],[11783,4.7,38.022,-15.24],[12093,4.9,38.969,5.59],[12387,4.1,39.871,0.33],
[12390,4.8,39.891,-11.87],[12394,4.1,39.897,-68.27],[12413,4.7,39.95,-42.89],[12484,5.2,40.165,-54.55],
[12486,4.1,40.167,-39.86],[12706,3.5,40.825,3.24],[12770,4.2,41.031,-13.86],[12828,4.3,41.236,10.11],
[12843,4.5,41.276,-18.57],[13147,4.5,42.273,-32.41],[13209,3.6,42.496,27.26],[13254,4.2,42.646,38.32],
[13268,3.8,42.674,55.9],[13531,3.9,43.564,52.76],[13701,3.9,44.107,-8.9],[13847,2.9,44.565,-40.3],
[13954,4.7,44.929,8.91],[14135,2.5,45.57,4.09],[14146,4.1,45.598,-23.62],[14240,5.1,45.903,-59.74],
[14328,2.9,46.199,53.51],[14354,3.3,46.294,38.84],[14576,2.1,47.042,40.96],[14668,3.8,47.374,44.86],
[14879,3.8,48.019,-28.99],[15197,4.8,48.958,-8.82],[15474,3.7,49.879,-21.76],[15510,4.3,49.982,-43.07],
[15863,1.8,51.081,49.86],[15900,3.6,51.203,9.03],[16083,3.7,51.792,9.73],[16228,4.2,52.267,59.94],
[16537,3.7,53.233,-9.46],[16611,4.3,53.447,-21.63],[17358,3,55.731,47.79],[17378,3.5,55.812,-9.76],
[17440,3.8,56.05,-64.81],[17448,3.8,56.08,32.29],[17499,3.7,56.219,24.11],[17529,3.8,56.298,42.58],
[17573,3.9,56.457,24.37],[17651,4.2,56.712,-23.25],[17678,3.3,56.81,-74.24],[17702,2.9,56.871,24.11],
[17797,4.3,57.149,-37.62],[17847,3.6,57.291,24.05],[17874,4.2,57.364,-36.2],[17959,4.6,57.59,71.33],
[18246,2.8,58.533,31.88],[18505,5,59.356,63.07],[18532,2.9,59.463,40.01],[18543,3,59.507,-13.51],
[18597,4.6,59.686,-61.4],[18614,4,59.741,35.79],[18724,3.4,60.17,12.49],[18907,3.9,60.789,5.99],
[19343,4,62.165,47.71],[19747,3.9,63.5,-42.29],[19780,3.3,63.606,-62.47],[19893,4.3,64.007,-51.49],
[19921,4.4,64.121,-59.3],[20042,3.5,64.474,-33.8],[20205,3.6,64.948,15.63],[20455,3.8,65.734,17.54],
[20535,4,66.009,-34.02],[20648,4.3,66.372,17.93],[20885,3.8,67.144,15.96],[20889,3.5,67.154,19.18],
[20894,3.4,67.166,15.87],[21060,5.1,67.709,-44.95],[21281,3.3,68.499,-55.04],[21393,3.8,68.888,-30.56],
[21421,0.9,68.98,16.51],[21444,3.9,69.08,-3.35],[21594,3.9,69.545,-14.3],[21770,4.4,70.14,-41.86],
[21861,5,70.515,-37.14],[21881,4.3,70.561,22.96],[21949,5.5,70.767,-70.93],[22109,4,71.376,-3.25],
[22449,3.2,72.46,6.96],[22509,4.3,72.653,8.9],[22549,3.7,72.802,5.61],[22701,4.4,73.224,-5.45],
[22730,5.3,73.345,2.51],[22783,4.3,73.513,66.34],[22797,3.7,73.563,2.44],[22845,4.6,73.724,10.15],
[23015,2.7,74.248,33.17],[23123,4.5,74.637,1.71],[23416,3,75.492,43.82],[23453,3.7,75.62,41.08],
[23685,3.2,76.365,-22.37],[23767,3.2,76.629,41.23],[23875,2.8,76.962,-5.09],[23972,4.3,77.287,-8.75],
[24244,4.5,78.075,-11.87],[24305,3.3,78.233,-16.21],[24327,4.4,78.308,-12.94],[24436,0.2,78.634,-8.2],
[24608,0.1,79.172,46],[24674,3.6,79.402,-6.84],[24845,4.3,79.894,-13.18],[24873,5.3,79.996,-12.32],
[25110,5.1,80.64,79.23],[25281,3.4,81.119,-2.4],[25336,1.6,81.283,6.35],
[25428,1.6,81.573,28.61],[25606,2.8,82.061,-20.76],[25859,3.9,82.803,-35.47],[25918,5.2,82.971,-76.34],
[25930,2.3,83.002,-0.3],[25985,2.6,83.183,-17.82],[26069,3.8,83.406,-62.49],[26207,3.4,83.784,9.93],
[26241,2.8,83.858,-5.91],[26311,1.7,84.053,-1.2],[26451,3,84.411,21.14],[26549,3.8,84.687,-2.6],
[26634,2.6,84.912,-34.07],[26727,1.7,85.19,-1.94],[27072,3.6,86.116,-22.45],[27100,4.3,86.193,-65.74],
[27288,3.5,86.739,-14.82],[27321,3.9,86.821,-51.07],[27366,2.1,86.939,-9.67],[27530,4.5,87.457,-56.17],
[27628,3.1,87.74,-35.77],[27654,3.8,87.83,-20.88],[27673,4,87.872,39.15],[27890,4.7,88.525,-63.09],
[27913,4.4,88.596,20.28],[27989,0.5,88.793,7.41],[28103,3.7,89.101,-14.17],[28199,4.4,89.384,-35.28],
[28328,4,89.787,-42.82],[28358,3.7,89.882,54.28],[28360,1.9,89.882,44.95],[28380,2.6,89.93,37.21],
[28614,4.1,90.596,9.65],[28691,5.1,90.864,19.69],[28734,4.2,91.03,23.26],[28910,4.7,91.539,-14.94],
[29038,4.4,91.893,14.77],[29151,5.7,92.241,2.5],[29426,4.5,92.985,14.21],[29651,4,93.714,-6.27],
[29655,3.3,93.719,22.51],[29807,4.4,94.138,-35.14],[30060,4.4,94.906,59.01],[30122,3,95.078,-30.06],
[30277,3.9,95.528,-33.44],[30324,2,95.675,-17.96],[30343,2.9,95.74,22.51],[30419,4.4,95.942,4.59],
[30438,-0.6,95.988,-52.7],[30867,3.8,97.204,-7.03],[30883,4.1,97.241,20.21],[31416,4.5,98.764,-22.96],
[31592,4,99.171,-19.26],[31681,1.9,99.428,16.4],[31685,3.2,99.44,-43.2],[32246,3.1,100.983,25.13],
[32349,-1.4,101.287,-16.72],[32362,3.4,101.322,12.9],[32607,3.2,102.048,-61.94],[32759,3.5,102.46,-32.51],
[32768,2.9,102.484,-50.61],[33018,3.6,103.197,33.96],[33152,3.9,103.533,-24.18],[33160,4.1,103.547,-12.04],
[33165,6.7,103.554,-23.93],[33347,4.4,104.034,-17.05],[33449,4.3,104.319,58.42],[33579,1.5,104.656,-28.97],
[33856,3.5,105.43,-27.93],[33977,3,105.756,-23.83],[34045,4.1,105.94,-15.63],[34088,4,106.027,20.57],
[34444,1.8,107.098,-26.39],[34481,3.8,107.187,-70.5],[34693,4.4,107.785,30.25],[34769,4.2,107.966,-0.49],
[35037,4,108.703,-26.77],[35228,4,109.208,-67.96],[35264,2.7,109.286,-37.1],[35350,3.6,109.523,16.54],
[35550,3.5,110.031,21.98],[35904,2.5,111.024,-29.3],[36046,3.8,111.432,27.8],[36145,4.6,111.679,49.21],
[36188,2.9,111.788,8.29],[36377,3.3,112.308,-43.3],[36850,1.6,113.649,31.89],[36962,4.1,113.981,26.9],
[37229,3.8,114.708,-26.8],[37279,0.4,114.825,5.22],[37447,3.9,115.312,-9.55],[37504,3.9,115.455,-72.61],
[37677,3.9,115.952,-28.95],[37740,3.6,116.112,24.4],[37819,3.6,116.314,-37.97],[37826,1.2,116.329,28.03],
[38146,5.3,117.257,-24.91],[38170,3.3,117.324,-24.86],[38414,3.7,118.054,-40.58],[38827,3.5,119.195,-52.98],
[39429,2.2,120.896,-40],[39757,2.8,121.886,-24.3],[39794,4.3,121.982,-68.62],[39863,4.4,122.149,-2.98],
[39953,1.8,122.383,-47.34],[40526,3.5,124.129,9.19],[40702,4,124.631,-76.92],[40843,5.1,125.016,27.22],
[41037,1.9,125.628,-59.51],[41075,4.3,125.709,43.19],[41307,3.9,126.415,-3.91],[41312,3.8,126.434,-66.14],
[41704,3.4,127.566,60.72],[42313,4.1,129.414,5.7],[42402,4.5,129.689,3.34],[42515,4,130.026,-35.31],
[42536,3.6,130.073,-52.92],[42568,4.3,130.154,-59.76],[42570,3.8,130.157,-46.65],[42799,4.3,130.806,3.4],
[42806,4.7,130.821,21.47],[42828,3.7,130.898,-33.19],[42911,3.9,131.171,18.15],[42913,1.9,131.176,-54.71],
[43023,3.9,131.507,-46.04],[43103,4,131.674,28.76],[43109,3.4,131.694,6.42],[43234,4.3,132.108,5.84],
[43409,4,132.633,-27.71],[43783,3.8,133.762,-60.64],[43813,3.1,133.848,5.95],[44066,4.3,134.622,11.86],
[44127,3.1,134.802,48.04],[44248,4,135.16,41.78],[44382,4,135.612,-66.4],[44471,3.6,135.906,47.16],
[44511,3.8,136.039,-47.1],[44700,4.6,136.632,38.45],[44816,2.2,136.999,-43.43],[45080,3.4,137.742,-58.97],
[45101,4,137.82,-62.32],[45238,1.7,138.3,-69.72],[45336,3.9,138.591,2.31],[45556,2.2,139.273,-59.28],
[45688,3.8,139.711,36.8],[45860,3.1,140.264,34.39],[45941,2.5,140.528,-55.01],[46390,2,141.897,-8.66],
[46509,4.6,142.287,-2.77],[46651,3.6,142.675,-40.47],[46701,3.2,142.805,-57.03],[46733,3.6,142.882,63.06],
[46776,4.5,142.996,-1.18],[46853,3.2,143.214,51.68],[46952,4.5,143.556,36.4],[47431,3.9,144.964,-1.14],
[47508,3.5,145.288,9.89],[47854,3.7,146.312,-62.51],[47908,3,146.463,23.77],[48002,2.9,146.776,-65.07],
[48319,3.8,147.747,59.04],[48356,4.1,147.87,-14.85],[48402,4.5,148.026,54.06],[48455,3.9,148.191,26.01],
[48774,3.5,149.216,-54.57],[48926,5.2,149.718,-35.89],[49583,3.5,151.833,16.76],[49593,4.5,151.857,35.24],
[49641,4.5,151.985,-0.37],[49669,1.4,152.093,11.97],[49841,3.6,152.647,-12.35],[50099,3.3,153.434,-70.04],
[50191,3.9,153.684,-42.12],[50335,3.4,154.173,23.42],[50371,3.4,154.271,-61.33],[50372,3.5,154.274,42.91],
[50583,2,154.993,19.84],[50801,3.1,155.582,41.5],[50954,4,156.099,-74.03],[51069,3.8,156.523,-16.84],
[51172,4.3,156.788,-31.07],[51232,3.8,156.97,-58.74],[51233,4.2,156.971,36.71],[51437,5.1,157.573,-0.64],
[51576,3.3,158.006,-61.69],[51624,3.8,158.203,9.31],[51839,4.1,158.867,-78.61],[51986,3.8,159.326,-48.23],
[52419,2.7,160.739,-64.39],[52468,4.6,160.885,-60.57],[52727,2.7,161.692,-49.42],[52943,3.1,162.406,-16.19],
[53229,3.8,163.328,34.21],[53253,3.8,163.374,-58.85],[53740,4.1,164.944,-18.3],[53910,2.3,165.46,56.38],
[54061,1.8,165.932,61.75],[54463,3.9,167.147,-58.98],[54539,3,167.416,44.5],[54682,4.5,167.915,-22.83],
[54872,2.6,168.527,20.52],[54879,3.3,168.56,15.43],[55219,3.5,169.62,33.09],
[55282,3.6,169.835,-14.78],[55425,3.9,170.252,-54.49],[55687,4.8,171.152,-10.86],[55705,4.1,171.221,-17.68],
[56211,3.8,172.851,69.33],[56343,3.5,173.25,-31.86],[56480,4.6,173.69,-54.26],[56561,3.1,173.945,-63.02],
[56633,4.7,174.17,-9.8],[57283,4.7,176.191,-18.35],[57363,3.6,176.402,-66.73],[57380,4,176.465,6.53],
[57399,3.7,176.513,47.78],[57632,2.1,177.265,14.57],[57757,3.6,177.674,1.76],[57936,4.3,178.227,-33.91],
[58001,2.4,178.458,53.69],[58188,5.2,179.004,-17.15],[59196,2.6,182.09,-50.72],[59199,4,182.103,-24.73],
[59316,3,182.531,-22.62],[59449,4,182.913,-52.37],[59747,2.8,183.786,-58.75],[59774,3.3,183.857,57.03],
[59803,2.6,183.952,-17.54],[60000,4.2,184.587,-79.31],[60030,5.9,184.668,-0.79],[60129,3.9,184.976,-0.67],
[60260,3.6,185.34,-60.4],[60718,0.8,186.65,-63.1],[60742,4.3,186.734,28.27],[60823,3.9,187.01,-50.23],
[60965,2.9,187.466,-16.52],[61084,1.6,187.791,-57.11],[61174,4.3,188.018,-16.2],[61199,3.8,188.117,-72.13],
[61281,3.9,188.371,69.79],[61317,4.2,188.436,41.36],[61359,2.6,188.597,-23.4],[61585,2.7,189.296,-69.14],
[61622,3.9,189.426,-48.54],[61932,2.2,190.379,-48.96],[61941,2.7,190.415,-1.45],[62322,3,191.57,-68.11],
[62434,1.3,191.93,-59.69],[62956,1.8,193.507,55.96],[63090,3.4,193.901,3.4],[63125,2.9,194.007,38.32],
[63608,2.9,195.544,10.96],[63613,3.6,195.568,-71.55],[64166,4.9,197.264,-23.12],[64241,4.3,197.497,17.53],
[64394,4.2,197.968,27.88],[64962,3,199.73,-23.17],[65109,2.8,200.149,-36.71],[65378,2.2,200.981,54.93],
[65474,1,201.298,-11.16],[65477,4,201.306,54.99],[65936,3.9,202.761,-39.41],[66249,3.4,203.673,-0.6],
[66657,2.3,204.972,-53.47],[67301,1.9,206.885,49.31],[67459,4,207.369,15.8],[67464,3.4,207.376,-41.69],
[67472,3.5,207.404,-42.47],[67927,2.7,208.671,18.4],[68002,2.5,208.885,-47.29],[68245,3.8,209.568,-42.1],
[68282,3.9,209.67,-44.8],[68520,4.2,210.412,1.54],[68702,0.6,210.956,-60.37],[68756,3.7,211.097,64.38],
[68895,3.3,211.593,-26.68],[68933,2.1,211.671,-36.37],[69427,4.2,213.224,-10.27],[69673,-0.1,213.915,19.18],
[69701,4.1,214.004,-6],[69996,3.5,214.851,-46.06],[70576,4.3,216.545,-45.38],[70638,4.3,216.73,-83.67],
[71053,3.6,217.957,30.37],[71075,3,218.019,38.31],[71352,2.3,218.877,-42.16],[71536,4,219.472,-49.43],
[71681,1.4,219.896,-60.84],[71683,-0,219.902,-60.83],[71795,3.8,220.287,13.73],[71860,2.3,220.482,-47.39],
[71908,3.2,220.627,-64.98],[71957,3.9,220.765,-5.66],[72105,2.4,221.247,27.07],[72220,3.7,221.562,1.89],
[72370,3.8,221.965,-79.04],[72607,2.1,222.676,74.16],[72622,2.8,222.72,-16.04],[73273,2.7,224.633,-43.13],
[73334,3.1,224.79,-42.1],[73555,3.5,225.487,40.39],[73714,3.3,226.018,-25.28],[73807,3.9,226.28,-47.05],
[74376,3.9,227.984,-48.74],[74395,3.4,228.071,-52.1],[74666,3.5,228.876,33.31],[74785,2.6,229.252,-9.38],
[74824,4.1,229.379,-58.8],[74946,2.9,229.727,-68.68],[75097,3,230.182,71.83],[75141,3.2,230.343,-40.65],
[75177,3.6,230.452,-36.26],[75264,3.4,230.67,-44.69],[75323,4.5,230.844,-59.32],[75458,3.3,231.232,58.97],
[75695,3.7,231.957,29.11],[76127,4.1,233.232,31.36],[76267,2.2,233.672,26.71],[76276,3.8,233.701,10.54],
[76297,2.8,233.785,-41.17],[76333,3.9,233.882,-14.79],[76470,3.6,234.256,-28.14],[76552,4.3,234.513,-42.57],
[76600,3.7,234.664,-29.78],[76952,3.8,235.686,26.3],[77055,4.3,236.015,77.79],[77070,2.6,236.067,6.43],
[77233,3.6,236.547,15.42],[77450,4.1,237.185,18.14],[77512,4.6,237.399,26.07],[77516,3.5,237.405,-3.43],
[77622,3.7,237.704,4.48],[77634,4,237.74,-33.63],[77760,4.6,238.169,42.45],[77853,4.1,238.456,-16.73],
[77952,2.8,238.786,-63.43],[78072,3.9,239.113,15.66],[78104,3.9,239.221,-29.21],[78159,4.1,239.397,26.88],
[78265,2.9,239.713,-26.11],[78384,3.4,240.031,-38.4],[78401,2.3,240.083,-22.62],[78493,5,240.361,29.85],
[78527,4,240.472,58.57],[78639,4.7,240.804,-49.23],[78820,2.6,241.359,-19.81],[78933,3.9,241.702,-20.67],
[78970,5.7,241.818,-36.76],[79509,5,243.37,-54.63],[79593,2.7,243.586,-3.69],[79664,3.9,243.859,-63.69],
[79822,5,244.376,75.76],[79882,3.2,244.58,-4.69],[79992,3.9,244.935,46.31],[80000,4,244.96,-50.16],
[80112,2.9,245.297,-25.59],[80170,3.7,245.48,19.15],[80331,2.7,245.998,61.51],[80582,4.5,246.796,-47.55],
[80763,1.1,247.352,-26.43],[80816,2.8,247.555,21.49],[80883,3.8,247.728,1.98],[81065,3.9,248.363,-78.9],
[81126,4.2,248.526,42.44],[81266,2.8,248.971,-28.22],[81377,2.5,249.29,-10.57],[81693,2.8,250.322,31.6],
[81833,3.5,250.724,38.92],[81852,4.2,250.769,-77.52],[82080,4.2,251.493,82.04],[82273,1.9,252.166,-69.03],
[82363,3.8,252.446,-59.04],[82396,2.3,252.541,-34.29],[82514,3,252.968,-38.05],[82545,3.6,253.084,-38.02],
[82671,4.7,253.499,-42.36],[82729,3.6,253.646,-42.36],[83000,3.2,254.417,9.38],[83081,3.1,254.655,-55.99],
[83207,3.9,255.072,30.93],[83895,3.2,257.197,65.71],[84012,2.4,257.595,-15.72],[84143,3.3,258.038,-43.24],
[84345,2.8,258.662,14.39],[84379,3.1,258.758,24.84],[84380,3.2,258.762,36.81],[84606,4.6,259.418,37.29],
[84880,4.3,260.207,-12.85],[84970,3.3,260.502,-25],[85112,4.2,260.921,37.15],[85258,2.8,261.325,-55.53],
[85267,3.3,261.349,-56.38],[85670,2.8,262.608,52.3],[85693,4.4,262.685,26.11],[85696,2.7,262.691,-37.3],
[85727,3.6,262.775,-60.68],[85755,4.8,262.854,-23.96],[85792,2.8,262.96,-49.88],[85822,4.3,263.054,86.59],
[85829,4.9,263.067,55.17],[85927,1.6,263.402,-37.1],[86032,2.1,263.734,12.56],[86228,1.9,264.33,-43],
[86263,3.5,264.397,-15.4],[86414,3.8,264.866,46.01],[86565,4.2,265.354,-12.88],[86670,2.4,265.622,-39.03],
[86742,2.8,265.868,4.57],[86929,3.6,266.433,-64.72],[86974,3.4,266.615,27.72],[87072,4.5,266.89,-27.83],
[87073,3,266.896,-40.13],[87108,3.8,266.973,2.71],[87261,3.2,267.465,-37.04],[87585,3.7,268.382,56.87],
[87808,3.9,269.063,37.25],[87833,2.2,269.152,51.49],[87933,3.7,269.441,29.25],[88048,3.3,269.757,-9.77],
[88192,3.9,270.161,2.93],[88635,3,271.452,-30.42],[88714,3.6,271.658,-50.09],[88771,3.7,271.837,9.56],
[88794,3.8,271.886,28.76],[88866,4.3,272.145,-63.67],[89341,3.8,273.441,-21.06],[89642,3.1,274.407,-36.76],
[89931,2.7,275.249,-29.83],[89937,3.5,275.264,72.73],[89962,3.2,275.328,-2.9],[90098,4.3,275.807,-61.49],
[90139,3.9,275.925,21.77],[90185,1.8,276.043,-34.38],[90422,3.5,276.743,-45.97],[90496,2.8,276.993,-25.42],
[90568,4.1,277.208,-49.07],[90595,4.7,277.299,-14.57],[90887,5.2,278.089,-39.7],[91117,3.9,278.802,-8.24],
[91262,0,279.235,38.78],[91792,4,280.759,-71.43],[91875,5.1,280.946,-38.32],[91971,4.3,281.193,37.61],
[92041,3.2,281.414,-26.99],[92175,4.2,281.794,-4.75],[92202,5.4,281.871,-5.71],[92420,3.5,282.52,33.36],
[92609,4.2,283.054,-62.19],[92791,4.2,283.626,36.9],[92814,5.1,283.68,-15.6],[92855,2,283.816,-26.3],
[92946,4.6,284.055,4.2],[92953,5.3,284.071,-42.71],[92989,5.4,284.169,-37.34],[93015,4.4,284.238,-67.23],
[93085,3.5,284.433,-21.11],[93174,4.8,284.681,-37.11],[93194,3.3,284.736,32.69],[93244,4,284.906,15.07],
[93506,2.6,285.653,-29.88],[93542,4.7,285.779,-42.1],[93683,3.8,286.171,-21.74],[93747,3,286.353,13.86],
[93805,3.4,286.562,-4.88],[93825,4.2,286.605,-37.06],[93864,3.3,286.735,-27.67],[94005,4.6,287.087,-40.5],
[94114,4.1,287.368,-37.9],[94141,2.9,287.441,-21.02],[94160,4.1,287.507,-39.34],[94376,3.1,288.139,67.66],
[94779,3.8,289.276,53.37],[94820,4.9,289.409,-18.95],[95168,3.9,290.418,-17.85],[95241,4,290.66,-44.46],
[95294,4.3,290.805,-44.8],[95347,4,290.972,-40.62],[95501,3.4,291.375,3.11],[95771,4.4,292.176,24.66],
[95853,3.8,292.426,51.73],[95947,3,292.68,27.96],[96406,5.6,294.007,-24.72],[96757,4.4,295.024,18.01],
[96837,4.4,295.262,17.48],[97165,2.9,296.244,45.13],[97278,2.7,296.565,10.61],[97365,3.7,296.847,18.53],
[97433,3.8,297.043,70.27],[97649,0.8,297.696,8.87],[97804,3.9,298.118,1.01],[98032,4.1,298.815,-41.87],
[98036,3.7,298.828,6.41],[98110,3.9,299.077,35.08],[98337,3.5,299.689,19.49],[98412,4.4,299.934,-35.28],
[98495,4,300.148,-72.91],[98543,4.7,300.275,27.75],[98688,4.4,300.665,-27.71],[98920,5.1,301.29,19.99],
[99240,3.5,302.182,-66.18],[99473,3.2,302.826,-0.82],[99675,3.8,303.408,46.74],[99848,4,303.868,47.71],
[100064,3.6,304.514,-12.54],[100345,3,305.253,-14.78],[100453,2.2,305.557,40.26],[100751,1.9,306.412,-56.74],
[101421,4,308.303,11.3],[101769,3.6,309.387,14.6],[101772,3.1,309.392,-47.29],[101958,3.8,309.91,15.91],
[102098,1.3,310.358,45.28],[102281,4.4,310.865,15.07],[102395,3.4,311.24,-66.2],[102422,3.4,311.322,61.84],
[102485,4.1,311.524,-25.27],[102488,2.5,311.553,33.97],[102532,4.3,311.665,16.12],[102618,3.8,311.919,-9.5],
[102831,4.9,312.492,-33.78],[102978,4.1,312.955,-26.92],[103227,3.7,313.703,-58.45],[103413,3.9,314.293,41.17],
[103738,4.7,315.323,-32.26],[104060,3.7,316.233,43.93],[104139,4.1,316.487,-17.23],[104521,4.7,317.585,10.13],
[104732,3.2,318.234,30.23],[104858,4.5,318.62,10.01],[104887,3.7,318.698,38.05],[104987,3.9,318.956,5.25],
[105140,4.7,319.485,-32.17],[105199,2.5,319.645,62.59],[105319,4.4,319.967,-53.45],[105515,4.3,320.562,-16.83],
[105570,5.2,320.723,6.81],[105858,4.2,321.611,-65.37],[105881,3.8,321.667,-22.41],[106032,3.2,322.165,70.56],
[106278,2.9,322.89,-5.57],[106481,4,323.495,45.59],[106985,3.7,325.023,-16.66],[107089,3.7,325.369,-77.39],
[107310,4.5,326.036,28.74],[107315,2.4,326.046,9.88],[107354,4.1,326.161,25.65],[107556,2.9,326.76,-16.13],
[107608,5,326.934,-30.9],[108085,3,328.482,-37.36],[108661,5.4,330.209,-28.45],[109074,3,331.446,-0.32],
[109111,4.5,331.529,-39.54],[109139,4.3,331.609,-13.87],[109176,3.8,331.753,25.35],[109268,1.7,332.058,-46.96],
[109352,5.6,332.307,33.17],[109422,4.9,332.537,-32.55],[109427,3.5,332.55,6.2],[109492,3.4,332.714,58.2],
[109937,4.1,333.992,37.75],[110003,4.2,334.208,-7.78],[110130,2.9,334.625,-60.26],[110395,3.9,335.414,-1.39],
[110538,4.4,335.89,52.23],[110609,4.5,336.129,49.48],[110960,3.6,337.208,-0.02],[110997,4,337.317,-43.5],
[111022,4.3,337.383,47.71],[111104,4.5,337.622,43.12],[111123,4.8,337.662,-10.68],[111169,3.8,337.823,50.28],
[111188,4.3,337.876,-32.35],[111497,4,338.839,-0.12],[111954,4.2,340.164,-27.04],[112029,3.4,340.366,10.83],
[112122,2.1,340.667,-46.88],[112158,2.9,340.751,30.22],[112405,4.1,341.515,-81.38],[112440,4,341.633,23.57],
[112447,4.2,341.673,12.17],[112623,3.5,342.139,-51.32],[112716,4,342.398,-13.59],[112724,3.5,342.42,66.2],
[112748,3.5,342.501,24.6],[112961,3.7,343.154,-7.58],[113136,3.3,343.663,-15.82],[113246,4.2,343.987,-32.54],
[113368,1.2,344.413,-29.62],[113638,4.1,345.22,-52.75],[113726,3.6,345.48,42.33],[113881,2.4,345.944,28.08],
[113963,2.5,346.19,15.21],[114131,4.3,346.72,-43.52],[114341,3.7,347.362,-21.17],[114421,3.9,347.59,-45.25],
[114855,4.2,348.973,-9.09],[114971,3.7,349.291,3.28],[114996,4,349.357,-58.24],[115102,4.4,349.706,-32.53],
[115438,4,350.743,-20.1],[115738,5,351.733,1.26],[115830,4.3,351.992,6.38],[116231,4.4,353.243,-37.82],
[116584,3.8,354.391,46.46],[116727,3.2,354.837,77.63],[116771,4.1,354.988,5.63],[116928,4.5,355.512,1.78],
[118268,4,359.828,6.86]];
# Call the function to convert stars to radians
stars_in_radians = convert_stars_to_radians(stars, d2r)

# Define the file name
output_file = "stars_in_radians.txt"

# Write the result to a text file
with open(output_file, "w") as file:
    file.write("[")
    for star in stars_in_radians:
        file.write(f"{star},")
    file.write("]")

print(f"Output saved to {output_file}")
