import csv

data = """
Rack 0, Sensor 0: 31.5°C
Rack 1, Sensor 0: 30.6°C
Rack 2, Sensor 0: 33°C
Rack 3, Sensor 0: 30.6°C
Rack 4, Sensor 0: 30.6°C
Rack 5, Sensor 0: 31.5°C
Rack 6, Sensor 0: 30.6°C
Rack 7, Sensor 0: 33°C
Rack 8, Sensor 0: 30.6°C
Rack 9, Sensor 0: 30.6°C
-----------------------
Rack 0, Sensor 0: 33.075°C
Rack 1, Sensor 0: 31.212°C
Rack 2, Sensor 0: 36.3°C
Rack 3, Sensor 0: 31.212°C
Rack 4, Sensor 0: 31.212°C
Rack 5, Sensor 0: 33.075°C
Rack 6, Sensor 0: 31.212°C
Rack 7, Sensor 0: 36.3°C
Rack 8, Sensor 0: 31.212°C
Rack 9, Sensor 0: 31.212°C
-----------------------
Rack 0, Sensor 0: 34.7288°C
Rack 1, Sensor 0: 31.8362°C
Rack 2, Sensor 0: 39.93°C
Rack 3, Sensor 0: 31.8362°C
Rack 4, Sensor 0: 31.8362°C
Rack 5, Sensor 0: 34.7288°C
Rack 6, Sensor 0: 31.8362°C
Rack 7, Sensor 0: 39.93°C
Rack 8, Sensor 0: 31.8362°C
Rack 9, Sensor 0: 31.8362°C
-----------------------
Rack 0, Sensor 0: 36.4652°C
Rack 1, Sensor 0: 32.473°C
Rack 2, Sensor 0: 43.923°C
Rack 3, Sensor 0: 32.473°C
Rack 4, Sensor 0: 32.473°C
Rack 5, Sensor 0: 36.4652°C
Rack 6, Sensor 0: 32.473°C
Rack 7, Sensor 0: 43.923°C
Rack 8, Sensor 0: 32.473°C
Rack 9, Sensor 0: 32.473°C
-----------------------
Rack 0, Sensor 0: 38.2884°C
Rack 1, Sensor 0: 33.1224°C
Rack 2, Sensor 0: 48.3153°C
Rack 3, Sensor 0: 33.1224°C
Rack 4, Sensor 0: 33.1224°C
Rack 5, Sensor 0: 38.2884°C
Rack 6, Sensor 0: 33.1224°C
Rack 7, Sensor 0: 48.3153°C
Rack 8, Sensor 0: 33.1224°C
Rack 9, Sensor 0: 33.1224°C
-----------------------
Rack 0, Sensor 0: 40.2029°C
Rack 1, Sensor 0: 33.7849°C
Rack 2, Sensor 0: 53.1468°C
Rack 3, Sensor 0: 33.7849°C
Rack 4, Sensor 0: 33.7849°C
Rack 5, Sensor 0: 40.2029°C
Rack 6, Sensor 0: 33.7849°C
Rack 7, Sensor 0: 53.1468°C
Rack 8, Sensor 0: 33.7849°C
Rack 9, Sensor 0: 33.7849°C
-----------------------
Rack 0, Sensor 0: 42.213°C
Rack 1, Sensor 0: 34.4606°C
Rack 2, Sensor 0: 58.4615°C
Rack 3, Sensor 0: 34.4606°C
Rack 4, Sensor 0: 34.4606°C
Rack 5, Sensor 0: 42.213°C
Rack 6, Sensor 0: 34.4606°C
Rack 7, Sensor 0: 58.4615°C
Rack 8, Sensor 0: 34.4606°C
Rack 9, Sensor 0: 34.4606°C
-----------------------
Rack 0, Sensor 0: 44.3237°C
Rack 1, Sensor 0: 35.1498°C
Rack 2, Sensor 0: 61.6736°C
Rack 3, Sensor 0: 35.1498°C
Rack 4, Sensor 0: 35.1498°C
Rack 5, Sensor 0: 44.3237°C
Rack 6, Sensor 0: 35.1498°C
Rack 7, Sensor 0: 61.4284°C
Rack 8, Sensor 0: 35.1498°C
Rack 9, Sensor 0: 35.1498°C
-----------------------
Rack 0, Sensor 0: 46.5398°C
Rack 1, Sensor 0: 35.8528°C
Rack 2, Sensor 0: 64.8543°C
Rack 3, Sensor 0: 35.8528°C
Rack 4, Sensor 0: 35.8528°C
Rack 5, Sensor 0: 46.5398°C
Rack 6, Sensor 0: 35.8528°C
Rack 7, Sensor 0: 64.6176°C
Rack 8, Sensor 0: 35.8528°C
Rack 9, Sensor 0: 35.8528°C
-----------------------
Rack 0, Sensor 0: 48.8668°C
Rack 1, Sensor 0: 36.5698°C
Rack 2, Sensor 0: 68.1057°C
Rack 3, Sensor 0: 36.5698°C
Rack 4, Sensor 0: 36.5698°C
Rack 5, Sensor 0: 48.8668°C
Rack 6, Sensor 0: 36.5698°C
Rack 7, Sensor 0: 67.4762°C
Rack 8, Sensor 0: 36.5698°C
Rack 9, Sensor 0: 36.5698°C
-----------------------
Rack 0, Sensor 0: 51.3102°C
Rack 1, Sensor 0: 37.3012°C
Rack 2, Sensor 0: 74.9163°C
Rack 3, Sensor 0: 37.3012°C
Rack 4, Sensor 0: 37.3012°C
Rack 5, Sensor 0: 51.3102°C
Rack 6, Sensor 0: 37.3012°C
Rack 7, Sensor 0: 74.2238°C
Rack 8, Sensor 0: 37.3012°C
Rack 9, Sensor 0: 37.3012°C
-----------------------
Rack 0, Sensor 0: 53.8757°C
Rack 1, Sensor 0: 38.0473°C
Rack 2, Sensor 0: 82.4079°C
Rack 3, Sensor 0: 38.0473°C
Rack 4, Sensor 0: 38.0473°C
Rack 5, Sensor 0: 53.8757°C
Rack 6, Sensor 0: 38.0473°C
Rack 7, Sensor 0: 81.6462°C
Rack 8, Sensor 0: 38.0473°C
Rack 9, Sensor 0: 38.0473°C
-----------------------
Rack 0, Sensor 0: 56.5695°C
Rack 1, Sensor 0: 38.8082°C
Rack 2, Sensor 0: 85.3423°C
Rack 3, Sensor 0: 38.8082°C
Rack 4, Sensor 0: 38.8082°C
Rack 5, Sensor 0: 56.5695°C
Rack 6, Sensor 0: 38.8082°C
Rack 7, Sensor 0: 84.8188°C
Rack 8, Sensor 0: 38.8082°C
Rack 9, Sensor 0: 38.8082°C
-----------------------
Rack 0, Sensor 0: 57.7306°C
Rack 1, Sensor 0: 39.5844°C
Rack 2, Sensor 0: 84.1204°C
Rack 3, Sensor 0: 39.5844°C
Rack 4, Sensor 0: 39.5844°C
Rack 5, Sensor 0: 57.7745°C
Rack 6, Sensor 0: 39.5844°C
Rack 7, Sensor 0: 87.9146°C
Rack 8, Sensor 0: 39.5844°C
Rack 9, Sensor 0: 39.5844°C
-----------------------
Rack 0, Sensor 0: 58.9108°C
Rack 1, Sensor 0: 40.3761°C
Rack 2, Sensor 0: 82.9075°C
Rack 3, Sensor 0: 40.3761°C
Rack 4, Sensor 0: 40.3761°C
Rack 5, Sensor 0: 59.084°C
Rack 6, Sensor 0: 40.3761°C
Rack 7, Sensor 0: 86.6131°C
Rack 8, Sensor 0: 40.3761°C
Rack 9, Sensor 0: 40.3761°C
-----------------------
Rack 0, Sensor 0: 60.1507°C
Rack 1, Sensor 0: 41.1836°C
Rack 2, Sensor 0: 81.6497°C
Rack 3, Sensor 0: 41.1836°C
Rack 4, Sensor 0: 41.1836°C
Rack 5, Sensor 0: 60.2151°C
Rack 6, Sensor 0: 41.1836°C
Rack 7, Sensor 0: 85.3795°C
Rack 8, Sensor 0: 41.1836°C
Rack 9, Sensor 0: 41.1836°C
-----------------------
Rack 0, Sensor 0: 61.2543°C
Rack 1, Sensor 0: 42.0072°C
Rack 2, Sensor 0: 80.4962°C
Rack 3, Sensor 0: 42.0072°C
Rack 4, Sensor 0: 42.0072°C
Rack 5, Sensor 0: 61.3453°C
Rack 6, Sensor 0: 42.0072°C
Rack 7, Sensor 0: 84.1026°C
Rack 8, Sensor 0: 42.0072°C
Rack 9, Sensor 0: 42.0072°C
-----------------------
Rack 0, Sensor 0: 62.3887°C
Rack 1, Sensor 0: 42.8474°C
Rack 2, Sensor 0: 79.308°C
Rack 3, Sensor 0: 42.8474°C
Rack 4, Sensor 0: 42.8474°C
Rack 5, Sensor 0: 62.4739°C
Rack 6, Sensor 0: 42.8474°C
Rack 7, Sensor 0: 82.9787°C
Rack 8, Sensor 0: 42.8474°C
Rack 9, Sensor 0: 42.8474°C
-----------------------
Rack 0, Sensor 0: 63.7085°C
Rack 1, Sensor 0: 43.7043°C
Rack 2, Sensor 0: 78.16°C
Rack 3, Sensor 0: 43.7043°C
Rack 4, Sensor 0: 43.7043°C
Rack 5, Sensor 0: 63.6867°C
Rack 6, Sensor 0: 43.7043°C
Rack 7, Sensor 0: 81.6941°C
Rack 8, Sensor 0: 43.7043°C
Rack 9, Sensor 0: 43.7043°C
-----------------------
Rack 0, Sensor 0: 64.9433°C
Rack 1, Sensor 0: 44.5784°C
Rack 2, Sensor 0: 76.9949°C
Rack 3, Sensor 0: 44.5784°C
Rack 4, Sensor 0: 44.5784°C
Rack 5, Sensor 0: 64.927°C
Rack 6, Sensor 0: 44.5784°C
Rack 7, Sensor 0: 80.4787°C
Rack 8, Sensor 0: 44.5784°C
Rack 9, Sensor 0: 44.5784°C
-----------------------
Rack 0, Sensor 0: 66.1519°C
Rack 1, Sensor 0: 45.47°C
Rack 2, Sensor 0: 75.6809°C
Rack 3, Sensor 0: 45.47°C
Rack 4, Sensor 0: 45.47°C
Rack 5, Sensor 0: 66.0913°C
Rack 6, Sensor 0: 45.47°C
Rack 7, Sensor 0: 79.209°C
Rack 8, Sensor 0: 45.47°C
Rack 9, Sensor 0: 45.47°C
-----------------------
Rack 0, Sensor 0: 69.4595°C
Rack 1, Sensor 0: 46.3794°C
Rack 2, Sensor 0: 74.465°C
Rack 3, Sensor 0: 46.3794°C
Rack 4, Sensor 0: 46.3794°C
Rack 5, Sensor 0: 69.3959°C
Rack 6, Sensor 0: 46.3794°C
Rack 7, Sensor 0: 77.9396°C
Rack 8, Sensor 0: 46.3794°C
Rack 9, Sensor 0: 46.3794°C
-----------------------
Rack 0, Sensor 0: 72.9324°C
Rack 1, Sensor 0: 47.307°C
Rack 2, Sensor 0: 73.2769°C
Rack 3, Sensor 0: 47.307°C
Rack 4, Sensor 0: 47.307°C
Rack 5, Sensor 0: 72.8657°C
Rack 6, Sensor 0: 47.307°C
Rack 7, Sensor 0: 76.6435°C
Rack 8, Sensor 0: 47.307°C
Rack 9, Sensor 0: 47.307°C
-----------------------
Rack 0, Sensor 0: 76.5791°C
Rack 1, Sensor 0: 48.2531°C
Rack 2, Sensor 0: 72.1146°C
Rack 3, Sensor 0: 48.2531°C
Rack 4, Sensor 0: 48.2531°C
Rack 5, Sensor 0: 76.509°C
Rack 6, Sensor 0: 48.2531°C
Rack 7, Sensor 0: 75.466°C
Rack 8, Sensor 0: 48.2531°C
Rack 9, Sensor 0: 48.2531°C
-----------------------
Rack 0, Sensor 0: 77.8568°C
Rack 1, Sensor 0: 49.2182°C
Rack 2, Sensor 0: 70.8124°C
Rack 3, Sensor 0: 49.2182°C
Rack 4, Sensor 0: 49.2182°C
Rack 5, Sensor 0: 77.6243°C
Rack 6, Sensor 0: 49.2182°C
Rack 7, Sensor 0: 74.1571°C
Rack 8, Sensor 0: 49.2182°C
Rack 9, Sensor 0: 49.2182°C
-----------------------
Rack 0, Sensor 0: 79.0725°C
Rack 1, Sensor 0: 50.2025°C
Rack 2, Sensor 0: 69.6935°C
Rack 3, Sensor 0: 50.2025°C
Rack 4, Sensor 0: 50.2025°C
Rack 5, Sensor 0: 78.7666°C
Rack 6, Sensor 0: 50.2025°C
Rack 7, Sensor 0: 72.9112°C
Rack 8, Sensor 0: 50.2025°C
Rack 9, Sensor 0: 50.2025°C
-----------------------
Rack 0, Sensor 0: 80.3683°C
Rack 1, Sensor 0: 51.2066°C
Rack 2, Sensor 0: 68.5167°C
Rack 3, Sensor 0: 51.2066°C
Rack 4, Sensor 0: 51.2066°C
Rack 5, Sensor 0: 79.8807°C
Rack 6, Sensor 0: 51.2066°C
Rack 7, Sensor 0: 71.8068°C
Rack 8, Sensor 0: 51.2066°C
Rack 9, Sensor 0: 51.2066°C
-----------------------
Rack 0, Sensor 0: 81.569°C
Rack 1, Sensor 0: 52.2307°C
Rack 2, Sensor 0: 67.4029°C
Rack 3, Sensor 0: 52.2307°C
Rack 4, Sensor 0: 52.2307°C
Rack 5, Sensor 0: 81.0332°C
Rack 6, Sensor 0: 52.2307°C
Rack 7, Sensor 0: 70.4933°C
Rack 8, Sensor 0: 52.2307°C
Rack 9, Sensor 0: 52.2307°C
-----------------------
Rack 0, Sensor 0: 82.8675°C
Rack 1, Sensor 0: 53.2753°C
Rack 2, Sensor 0: 66.1157°C
Rack 3, Sensor 0: 53.2753°C
Rack 4, Sensor 0: 53.2753°C
Rack 5, Sensor 0: 82.1918°C
Rack 6, Sensor 0: 53.2753°C
Rack 7, Sensor 0: 69.2745°C
Rack 8, Sensor 0: 53.2753°C
Rack 9, Sensor 0: 53.2753°C
-----------------------
Rack 0, Sensor 0: 84.0501°C
Rack 1, Sensor 0: 54.3408°C
Rack 2, Sensor 0: 64.8484°C
Rack 3, Sensor 0: 54.3408°C
Rack 4, Sensor 0: 54.3408°C
Rack 5, Sensor 0: 83.4046°C
Rack 6, Sensor 0: 54.3408°C
Rack 7, Sensor 0: 68.0276°C
Rack 8, Sensor 0: 54.3408°C
Rack 9, Sensor 0: 54.3408°C
-----------------------
Rack 0, Sensor 0: 85.267°C
Rack 1, Sensor 0: 55.4277°C
Rack 2, Sensor 0: 63.7398°C
Rack 3, Sensor 0: 55.4277°C
Rack 4, Sensor 0: 55.4277°C
Rack 5, Sensor 0: 84.6009°C
Rack 6, Sensor 0: 55.4277°C
Rack 7, Sensor 0: 66.7226°C
Rack 8, Sensor 0: 55.4277°C
Rack 9, Sensor 0: 55.4277°C
-----------------------
Rack 0, Sensor 0: 83.9622°C
Rack 1, Sensor 0: 56.1269°C
Rack 2, Sensor 0: 62.5772°C
Rack 3, Sensor 0: 55.9537°C
Rack 4, Sensor 0: 56.0481°C
Rack 5, Sensor 0: 85.7788°C
Rack 6, Sensor 0: 56.1228°C
Rack 7, Sensor 0: 65.5861°C
Rack 8, Sensor 0: 55.9263°C
Rack 9, Sensor 0: 56.0745°C
-----------------------
Rack 0, Sensor 0: 82.6798°C
Rack 1, Sensor 0: 56.7784°C
Rack 2, Sensor 0: 61.4268°C
Rack 3, Sensor 0: 56.4939°C
Rack 4, Sensor 0: 56.6366°C
Rack 5, Sensor 0: 84.5277°C
Rack 6, Sensor 0: 56.8509°C
Rack 7, Sensor 0: 64.3566°C
Rack 8, Sensor 0: 56.4449°C
Rack 9, Sensor 0: 56.7189°C
-----------------------
Rack 0, Sensor 0: 81.4831°C
Rack 1, Sensor 0: 57.5024°C
Rack 2, Sensor 0: 60.2392°C
Rack 3, Sensor 0: 57.0269°C
Rack 4, Sensor 0: 57.2619°C
Rack 5, Sensor 0: 83.2273°C
Rack 6, Sensor 0: 57.5209°C
Rack 7, Sensor 0: 63.2091°C
Rack 8, Sensor 0: 56.9904°C
Rack 9, Sensor 0: 57.3701°C
-----------------------
Rack 0, Sensor 0: 80.3506°C
Rack 1, Sensor 0: 58.2212°C
Rack 2, Sensor 0: 58.9981°C
Rack 3, Sensor 0: 57.5249°C
Rack 4, Sensor 0: 57.88°C
Rack 5, Sensor 0: 82.0655°C
Rack 6, Sensor 0: 58.2281°C
Rack 7, Sensor 0: 62.0415°C
Rack 8, Sensor 0: 57.4897°C
Rack 9, Sensor 0: 57.945°C
-----------------------
Rack 0, Sensor 0: 79.2094°C
Rack 1, Sensor 0: 58.8661°C
Rack 2, Sensor 0: 57.7757°C
Rack 3, Sensor 0: 58.0214°C
Rack 4, Sensor 0: 58.4487°C
Rack 5, Sensor 0: 80.766°C
Rack 6, Sensor 0: 58.8518°C
Rack 7, Sensor 0: 60.9137°C
Rack 8, Sensor 0: 57.9934°C
Rack 9, Sensor 0: 58.5787°C
-----------------------
Rack 0, Sensor 0: 77.8927°C
Rack 1, Sensor 0: 59.5915°C
Rack 2, Sensor 0: 56.5252°C
Rack 3, Sensor 0: 58.5148°C
Rack 4, Sensor 0: 59.0812°C
Rack 5, Sensor 0: 79.5848°C
Rack 6, Sensor 0: 59.4989°C
Rack 7, Sensor 0: 59.7626°C
Rack 8, Sensor 0: 58.5053°C
Rack 9, Sensor 0: 59.1556°C
-----------------------
Rack 0, Sensor 0: 76.7592°C
Rack 1, Sensor 0: 60.2921°C
Rack 2, Sensor 0: 55.3975°C
Rack 3, Sensor 0: 59.0459°C
Rack 4, Sensor 0: 59.6492°C
Rack 5, Sensor 0: 78.3209°C
Rack 6, Sensor 0: 60.1191°C
Rack 7, Sensor 0: 58.4536°C
Rack 8, Sensor 0: 58.9685°C
Rack 9, Sensor 0: 59.7629°C
-----------------------
Rack 0, Sensor 0: 75.6204°C
Rack 1, Sensor 0: 60.9325°C
Rack 2, Sensor 0: 54.122°C
Rack 3, Sensor 0: 59.5714°C
Rack 4, Sensor 0: 60.2714°C
Rack 5, Sensor 0: 77.0081°C
Rack 6, Sensor 0: 60.8084°C
Rack 7, Sensor 0: 57.1865°C
Rack 8, Sensor 0: 59.4354°C
Rack 9, Sensor 0: 60.3278°C
-----------------------
Rack 0, Sensor 0: 74.406°C
Rack 1, Sensor 0: 61.5532°C
Rack 2, Sensor 0: 53.0067°C
Rack 3, Sensor 0: 60.0485°C
Rack 4, Sensor 0: 60.8722°C
Rack 5, Sensor 0: 75.7278°C
Rack 6, Sensor 0: 61.4896°C
Rack 7, Sensor 0: 55.9203°C
Rack 8, Sensor 0: 59.8985°C
Rack 9, Sensor 0: 60.8951°C
-----------------------
Rack 0, Sensor 0: 73.086°C
Rack 1, Sensor 0: 62.1893°C
Rack 2, Sensor 0: 51.7109°C
Rack 3, Sensor 0: 60.5183°C
Rack 4, Sensor 0: 61.5319°C
Rack 5, Sensor 0: 74.6159°C
Rack 6, Sensor 0: 62.2071°C
Rack 7, Sensor 0: 54.8043°C
Rack 8, Sensor 0: 60.3572°C
Rack 9, Sensor 0: 61.5467°C
-----------------------
Rack 0, Sensor 0: 71.8553°C
Rack 1, Sensor 0: 62.8224°C
Rack 2, Sensor 0: 50.575°C
Rack 3, Sensor 0: 61.0126°C
Rack 4, Sensor 0: 62.1824°C
Rack 5, Sensor 0: 73.3356°C
Rack 6, Sensor 0: 62.8621°C
Rack 7, Sensor 0: 53.5828°C
Rack 8, Sensor 0: 60.8686°C
Rack 9, Sensor 0: 62.1464°C
-----------------------
Rack 0, Sensor 0: 70.6041°C
Rack 1, Sensor 0: 63.4457°C
Rack 2, Sensor 0: 49.3582°C
Rack 3, Sensor 0: 61.5403°C
Rack 4, Sensor 0: 62.7658°C
Rack 5, Sensor 0: 72.0173°C
Rack 6, Sensor 0: 63.5437°C
Rack 7, Sensor 0: 52.2897°C
Rack 8, Sensor 0: 61.3955°C
Rack 9, Sensor 0: 62.7656°C
-----------------------
Rack 0, Sensor 0: 69.4963°C
Rack 1, Sensor 0: 64.1482°C
Rack 2, Sensor 0: 48.0749°C
Rack 3, Sensor 0: 62.0835°C
Rack 4, Sensor 0: 63.4119°C
Rack 5, Sensor 0: 70.7344°C
Rack 6, Sensor 0: 64.2745°C
Rack 7, Sensor 0: 51.0261°C
Rack 8, Sensor 0: 61.9367°C
Rack 9, Sensor 0: 63.4238°C
-----------------------
Rack 0, Sensor 0: 68.2496°C
Rack 1, Sensor 0: 64.8201°C
Rack 2, Sensor 0: 46.9388°C
Rack 3, Sensor 0: 62.6179°C
Rack 4, Sensor 0: 64.0597°C
Rack 5, Sensor 0: 69.6175°C
Rack 6, Sensor 0: 64.9651°C
Rack 7, Sensor 0: 49.8715°C
Rack 8, Sensor 0: 62.4527°C
Rack 9, Sensor 0: 63.999°C
-----------------------
Rack 0, Sensor 0: 66.9955°C
Rack 1, Sensor 0: 65.47°C
Rack 2, Sensor 0: 45.7665°C
Rack 3, Sensor 0: 63.0974°C
Rack 4, Sensor 0: 64.6178°C
Rack 5, Sensor 0: 68.3782°C
Rack 6, Sensor 0: 65.6035°C
Rack 7, Sensor 0: 48.6283°C
Rack 8, Sensor 0: 62.9579°C
Rack 9, Sensor 0: 64.6559°C
-----------------------
Rack 0, Sensor 0: 65.8339°C
Rack 1, Sensor 0: 66.7794°C
Rack 2, Sensor 0: 44.5463°C
Rack 3, Sensor 0: 63.6217°C
Rack 4, Sensor 0: 65.1803°C
Rack 5, Sensor 0: 67.1745°C
Rack 6, Sensor 0: 66.9156°C
Rack 7, Sensor 0: 47.3979°C
Rack 8, Sensor 0: 63.5027°C
Rack 9, Sensor 0: 65.2555°C
-----------------------
Rack 0, Sensor 0: 64.6599°C
Rack 1, Sensor 0: 68.115°C
Rack 2, Sensor 0: 43.2598°C
Rack 3, Sensor 0: 64.1199°C
Rack 4, Sensor 0: 66.4839°C
Rack 5, Sensor 0: 66.0738°C
Rack 6, Sensor 0: 68.2539°C
Rack 7, Sensor 0: 46.222°C
Rack 8, Sensor 0: 64.0159°C
Rack 9, Sensor 0: 66.5606°C
-----------------------
Rack 0, Sensor 0: 63.3765°C
Rack 1, Sensor 0: 69.4773°C
Rack 2, Sensor 0: 42.1084°C
Rack 3, Sensor 0: 64.6401°C
Rack 4, Sensor 0: 67.8136°C
Rack 5, Sensor 0: 64.8675°C
Rack 6, Sensor 0: 69.619°C
Rack 7, Sensor 0: 45.016°C
Rack 8, Sensor 0: 64.5022°C
Rack 9, Sensor 0: 67.8918°C
-----------------------
Rack 0, Sensor 0: 62.1199°C
Rack 1, Sensor 0: 70.8668°C
Rack 2, Sensor 0: 40.9682°C
Rack 3, Sensor 0: 65.1555°C
Rack 4, Sensor 0: 69.1699°C
Rack 5, Sensor 0: 63.7585°C
Rack 6, Sensor 0: 71.0113°C
Rack 7, Sensor 0: 43.8249°C
Rack 8, Sensor 0: 65.0244°C
Rack 9, Sensor 0: 69.2496°C
-----------------------
Rack 0, Sensor 0: 60.8716°C
Rack 1, Sensor 0: 72.2841°C
Rack 2, Sensor 0: 39.7279°C
Rack 3, Sensor 0: 66.4586°C
Rack 4, Sensor 0: 70.5533°C
Rack 5, Sensor 0: 62.5822°C
Rack 6, Sensor 0: 72.4316°C
Rack 7, Sensor 0: 42.6843°C
Rack 8, Sensor 0: 66.3248°C
Rack 9, Sensor 0: 70.6346°C
-----------------------
Rack 0, Sensor 0: 59.6376°C
Rack 1, Sensor 0: 73.7298°C
Rack 2, Sensor 0: 38.49°C
Rack 3, Sensor 0: 67.7877°C
Rack 4, Sensor 0: 71.9643°C
Rack 5, Sensor 0: 61.3214°C
Rack 6, Sensor 0: 73.8802°C
Rack 7, Sensor 0: 41.5121°C
Rack 8, Sensor 0: 67.6513°C
Rack 9, Sensor 0: 72.0473°C
-----------------------
Rack 0, Sensor 0: 58.3747°C
Rack 1, Sensor 0: 75.2044°C
Rack 2, Sensor 0: 37.3455°C
Rack 3, Sensor 0: 69.1435°C
Rack 4, Sensor 0: 73.4036°C
Rack 5, Sensor 0: 60.0188°C
Rack 6, Sensor 0: 75.3578°C
Rack 7, Sensor 0: 40.2614°C
Rack 8, Sensor 0: 69.0044°C
Rack 9, Sensor 0: 73.4883°C
-----------------------
Rack 0, Sensor 0: 57.131°C
Rack 1, Sensor 0: 75.847°C
Rack 2, Sensor 0: 36.1283°C
Rack 3, Sensor 0: 70.5264°C
Rack 4, Sensor 0: 74.8717°C
Rack 5, Sensor 0: 58.8995°C
Rack 6, Sensor 0: 76.0008°C
Rack 7, Sensor 0: 38.9684°C
Rack 8, Sensor 0: 70.3845°C
Rack 9, Sensor 0: 74.958°C
-----------------------
Rack 0, Sensor 0: 55.8801°C
Rack 1, Sensor 0: 76.4695°C
Rack 2, Sensor 0: 35.0039°C
Rack 3, Sensor 0: 71.9369°C
Rack 4, Sensor 0: 76.3691°C
Rack 5, Sensor 0: 57.72°C
Rack 6, Sensor 0: 76.6823°C
Rack 7, Sensor 0: 37.7379°C
Rack 8, Sensor 0: 71.7921°C
Rack 9, Sensor 0: 76.4572°C
-----------------------
Rack 0, Sensor 0: 54.6334°C
Rack 1, Sensor 0: 77.1159°C
Rack 2, Sensor 0: 33.7332°C
Rack 3, Sensor 0: 73.3756°C
Rack 4, Sensor 0: 76.9508°C
Rack 5, Sensor 0: 56.5475°C
Rack 6, Sensor 0: 77.3167°C
Rack 7, Sensor 0: 36.4213°C
Rack 8, Sensor 0: 73.228°C
Rack 9, Sensor 0: 77.0076°C
-----------------------
Rack 0, Sensor 0: 53.3514°C
Rack 1, Sensor 0: 77.7676°C
Rack 2, Sensor 0: 32.5918°C
Rack 3, Sensor 0: 74.8431°C
Rack 4, Sensor 0: 77.5489°C
Rack 5, Sensor 0: 55.2366°C
Rack 6, Sensor 0: 78.0401°C
Rack 7, Sensor 0: 35.153°C
Rack 8, Sensor 0: 74.6926°C
Rack 9, Sensor 0: 77.6345°C
-----------------------
Rack 0, Sensor 0: 52.2248°C
Rack 1, Sensor 0: 78.4625°C
Rack 2, Sensor 0: 31.4074°C
Rack 3, Sensor 0: 76.34°C
Rack 4, Sensor 0: 78.184°C
Rack 5, Sensor 0: 53.9291°C
Rack 6, Sensor 0: 78.7632°C
Rack 7, Sensor 0: 33.8634°C
Rack 8, Sensor 0: 76.1864°C
Rack 9, Sensor 0: 78.2069°C
-----------------------
Rack 0, Sensor 0: 50.9502°C
Rack 1, Sensor 0: 79.1406°C
Rack 2, Sensor 0: 30.2419°C
Rack 3, Sensor 0: 76.8813°C
Rack 4, Sensor 0: 78.8341°C
Rack 5, Sensor 0: 52.6368°C
Rack 6, Sensor 0: 79.4352°C
Rack 7, Sensor 0: 32.6367°C
Rack 8, Sensor 0: 76.6597°C
Rack 9, Sensor 0: 78.787°C
-----------------------
Rack 0, Sensor 0: 49.66°C
Rack 1, Sensor 0: 79.8119°C
Rack 2, Sensor 0: 29.0399°C
Rack 3, Sensor 0: 77.4174°C
Rack 4, Sensor 0: 79.4386°C
Rack 5, Sensor 0: 51.4728°C
Rack 6, Sensor 0: 80.0683°C
Rack 7, Sensor 0: 31.3861°C
Rack 8, Sensor 0: 77.1847°C
Rack 9, Sensor 0: 79.3523°C
-----------------------
Rack 0, Sensor 0: 48.4273°C
Rack 1, Sensor 0: 80.4832°C
Rack 2, Sensor 0: 31.9439°C
Rack 3, Sensor 0: 77.9526°C
Rack 4, Sensor 0: 80.0683°C
Rack 5, Sensor 0: 50.3336°C
Rack 6, Sensor 0: 80.7066°C
Rack 7, Sensor 0: 30.1765°C
Rack 8, Sensor 0: 77.6541°C
Rack 9, Sensor 0: 79.9175°C
-----------------------
Rack 0, Sensor 0: 47.248°C
Rack 1, Sensor 0: 81.134°C
Rack 2, Sensor 0: 35.1383°C
Rack 3, Sensor 0: 78.4964°C
Rack 4, Sensor 0: 80.7182°C
Rack 5, Sensor 0: 49.0967°C
Rack 6, Sensor 0: 81.42°C
Rack 7, Sensor 0: 28.8965°C
Rack 8, Sensor 0: 78.1579°C
Rack 9, Sensor 0: 80.5044°C
-----------------------
Rack 0, Sensor 0: 46.0612°C
Rack 1, Sensor 0: 81.8256°C
Rack 2, Sensor 0: 38.6522°C
Rack 3, Sensor 0: 79.0105°C
Rack 4, Sensor 0: 81.2967°C
Rack 5, Sensor 0: 47.9634°C
Rack 6, Sensor 0: 82.0399°C
Rack 7, Sensor 0: 31.7861°C
Rack 8, Sensor 0: 78.6262°C
Rack 9, Sensor 0: 81.1256°C
-----------------------
Rack 0, Sensor 0: 44.8812°C
Rack 1, Sensor 0: 82.472°C
Rack 2, Sensor 0: 42.5174°C
Rack 3, Sensor 0: 79.4992°C
Rack 4, Sensor 0: 81.8568°C
Rack 5, Sensor 0: 46.7694°C
Rack 6, Sensor 0: 82.7653°C
Rack 7, Sensor 0: 34.9647°C
Rack 8, Sensor 0: 79.138°C
Rack 9, Sensor 0: 81.7048°C
-----------------------
Rack 0, Sensor 0: 43.6363°C
Rack 1, Sensor 0: 83.1762°C
Rack 2, Sensor 0: 46.7691°C
Rack 3, Sensor 0: 80.0022°C
Rack 4, Sensor 0: 82.4241°C
Rack 5, Sensor 0: 45.4752°C
Rack 6, Sensor 0: 83.4529°C
Rack 7, Sensor 0: 38.4612°C
Rack 8, Sensor 0: 79.6438°C
Rack 9, Sensor 0: 82.2776°C
-----------------------
Rack 0, Sensor 0: 42.4136°C
Rack 1, Sensor 0: 83.8394°C
Rack 2, Sensor 0: 51.446°C
Rack 3, Sensor 0: 80.5367°C
Rack 4, Sensor 0: 83.0174°C
Rack 5, Sensor 0: 44.3214°C
Rack 6, Sensor 0: 84.1038°C
Rack 7, Sensor 0: 42.3073°C
Rack 8, Sensor 0: 80.169°C
Rack 9, Sensor 0: 82.8979°C
-----------------------
Rack 0, Sensor 0: 41.097°C
Rack 1, Sensor 0: 84.4918°C
Rack 2, Sensor 0: 56.5906°C
Rack 3, Sensor 0: 81.0773°C
Rack 4, Sensor 0: 83.5824°C
Rack 5, Sensor 0: 43.131°C
Rack 6, Sensor 0: 84.7156°C
Rack 7, Sensor 0: 46.5381°C
Rack 8, Sensor 0: 80.6991°C
Rack 9, Sensor 0: 83.5331°C
-----------------------
Rack 0, Sensor 0: 39.9324°C
Rack 1, Sensor 0: 85.117°C
Rack 2, Sensor 0: 59.8167°C
Rack 3, Sensor 0: 81.6017°C
Rack 4, Sensor 0: 84.1378°C
Rack 5, Sensor 0: 41.9322°C
Rack 6, Sensor 0: 85.4473°C
Rack 7, Sensor 0: 51.1919°C
Rack 8, Sensor 0: 81.2223°C
Rack 9, Sensor 0: 84.1063°C
-----------------------
Rack 0, Sensor 0: 38.7281°C
Rack 1, Sensor 0: 83.8266°C
Rack 2, Sensor 0: 62.6183°C
Rack 3, Sensor 0: 82.0691°C
Rack 4, Sensor 0: 84.7299°C
Rack 5, Sensor 0: 40.7658°C
Rack 6, Sensor 0: 84.2027°C
Rack 7, Sensor 0: 56.3111°C
Rack 8, Sensor 0: 81.7548°C
Rack 9, Sensor 0: 84.6707°C
-----------------------
Rack 0, Sensor 0: 37.6168°C
Rack 1, Sensor 0: 82.7149°C
Rack 2, Sensor 0: 65.6201°C
Rack 3, Sensor 0: 82.5991°C
Rack 4, Sensor 0: 85.3561°C
Rack 5, Sensor 0: 39.5685°C
Rack 6, Sensor 0: 83.0765°C
Rack 7, Sensor 0: 59.3854°C
Rack 8, Sensor 0: 82.2662°C
Rack 9, Sensor 0: 85.279°C
"""

# Split data into lines
lines = data.strip().split('\n')

# Open CSV file for writing
with open('temperature_data.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(['Rack', 'Sensor', 'Temperature'])  # Write header

    # Write data to CSV
    for line in lines:
        if line.startswith('Rack'):
            # rack, sensor, temperature = line.split(':')
            racksensor, temperature = line.split(':')
            rack, sensor = racksensor.split(',')
            rack_id = int(rack.split()[1])
            sensor_id = int(sensor.split()[1])
            temperature_value = float(temperature.strip('°C'))
            csvwriter.writerow([rack_id, sensor_id, temperature_value])