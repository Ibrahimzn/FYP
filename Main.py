import ObjDetection
from time import sleep


trafficLights = [(0,0),
                 (1,0),
                 (2,0),
                 (3,0)]

def main():
    dt = ObjDetection.ObjDetection() #create object detection object
    model = dt.loadModel(0.60) #load model with confidence threshold of 60%

    while True: #infinite loop to keep the traffic light on
        updateLights(dt, model)


def updateLights(dt, model): #update the traffic lights times
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

def trafficCycle(dt, model): #traffic light cycle
    for i in range(4):
        sec = trafficLights[i][1]

        if sec == 0: #check if there are no cars at the light
            print(f'no cars detected in light {i}, skipping this light...') 
            continue

        print(f'cars detected at light {i}')

        for j in range(sec,0,-1): #traffic light ON
            sleep(1)
            sec -= 1
            print(f'light {i} is green for {j} seconds')
            secToOff,_ = dt.detectObject(model,i) #to check if there are cars while the light is ON

            if secToOff == 0 or sec == 0: #if there are no cars or the time is up, turn the light to yellow
                print(f'no cars at light {i}, turning Yellow light...')
                for k in range(3):
                    sleep(1)
                    print(f'light {i} is yellow for {3-k} seconds')
                sec = 0
                break

if __name__ == '__main__':
    main()