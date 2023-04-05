import ObjDetection
from time import sleep


trafficLights = [(0,0),
                 (1,0),
                 (2,0),
                 (3,0)]

def main():
    dt = ObjDetection.ObjDetection()
    model = dt.loadModel(0.60)
    while True:
        updateLights(dt, model)


def updateLights(dt, model):
    for i in range(4):
        sec, light = dt.detectObject(model,i)
        if light == 0:
            trafficLights[0] = (0, sec)
        elif light == 1:
            trafficLights[1] = (1, sec)
        elif light == 2:
            trafficLights[2] = (2, sec)
        elif light == 3:
            trafficLights[3] = (3, sec)
    #print(trafficLights)
    trafficCycle(dt, model)

def trafficCycle(dt, model):
    for i in range(4):
        sec = trafficLights[i][1]
        if sec == 0:
            print(f'no cars detected in light {i}, skipping this light')
            continue
        print(f'cars detected at light {i}')
        for j in range(sec,0,-1):
            sleep(1)
            sec -= 1
            print(f'light {i} is green for {j} seconds')
            secToOff,_ = dt.detectObject(model,i)
            if secToOff == 0:
                print(f'no cars, turning off the light {i}')
                sec = 0
                break




if __name__ == '__main__':
    main()