import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def showGraph(trainDatas, trainOutputResult, testDatas, testOutputResult, y, interval):
    try:
        ###clear 之前的plot
        plt.clf()
        plt.figure(1, figsize=(16, 12))
        plt.subplot(221)
        plt.title("TrainSample")
        set2DPlot(trainDatas, trainOutputResult, y.shape[0], interval)
        plt.subplot(222)
        plt.title("TestSample (black point is identify error data)")
        set2DPlot(testDatas, testOutputResult, y.shape[0], interval)
    except Exception as e:
        print(e)
        pass
# 可以plot出2D的data. outputResult為資料集輸出的結果(output).
def set2DPlot(Datas, outputResult, outputHadvalue, interval):
    # Datas = np.hsplit(Datas, [1])
    # Datas = Datas[1]
    # plt.scatter(Datas[0], Datas[1], c='r', label='perceptron1')
    pointlabel = np.zeros(outputHadvalue)
    colorSelect = ['black', 'b', 'g', 'r', 'c', 'm', 'y', 'k']
    for i in range(Datas.shape[0]):
        plt.scatter(Datas[i][0], Datas[i][1], c=colorSelect[int(outputResult[i]*interval) + 1],
                    label=str(int(outputResult[i]*interval)) if pointlabel[int(outputResult[i]*interval)] == 0 else "")
        if pointlabel[int(outputResult[i]*interval)] == 0:
            pointlabel[int(outputResult[i]*interval)] = 1

    plt.xlim([-5, 5])
    plt.ylim([-8, 8])

    x = np.arange(-5, 5, 0.1)
    plt.legend()
