import math
import time
import numpy as np
from timebudget import timebudget
import psutil
import tracemalloc
from multiprocessing import Pool
from dream.simulation.imports import MachineJobShop, QueueJobShop, ExitJobShop, Job
from dream.simulation.Globals import runSimulation
import matplotlib.pyplot as plt

#define the objects of the model
Q1=QueueJobShop('Q1','Queue1', capacity=float("inf"), schedulingRule="Priority")
Q2=QueueJobShop('Q2','Queue2', capacity=float("inf"))
Q3=QueueJobShop('Q3','Queue3', capacity=float("inf"))
M1=MachineJobShop('M1','Machine1')
M2=MachineJobShop('M2','Machine2')
M3=MachineJobShop('M3','Machine3')
E=ExitJobShop('E','Exit')  

#define predecessors and successors for the objects    
Q1.defineRouting(successorList=[M1])
Q2.defineRouting(successorList=[M2])
Q3.defineRouting(successorList=[M3])
M1.defineRouting(predecessorList=[Q1])
M2.defineRouting(predecessorList=[Q2])
M3.defineRouting(predecessorList=[Q3])

#define the routes of the Jobs in the system
J1Route=[{"stationIdsList": ["Q1"]},
         {"stationIdsList": ["M1"],"processingTime":{'Fixed':{'mean':1}}},
         {"stationIdsList": ["Q3"]},
         {"stationIdsList": ["M3"],"processingTime":{'Fixed':{'mean':3}}},
         {"stationIdsList": ["Q2"]},
         {"stationIdsList": ["M2"],"processingTime":{'Fixed':{'mean':2}}},
         {"stationIdsList": ["E"],}]
J2Route=[{"stationIdsList": ["Q1"]},
         {"stationIdsList": ["M1"],"processingTime":{'Fixed':{'mean':2}}},
         {"stationIdsList": ["Q2"]},
         {"stationIdsList": ["M2"],"processingTime":{'Fixed':{'mean':4}}},
         {"stationIdsList": ["Q3"]},
         {"stationIdsList": ["M3"],"processingTime":{'Fixed':{'mean':6}}},
         {"stationIdsList": ["E"],}]
J3Route=[{"stationIdsList": ["Q1"]},
         {"stationIdsList": ["M1"],"processingTime":{'Fixed':{'mean':10}}},
         {"stationIdsList": ["Q3"]},
         {"stationIdsList": ["M3"],"processingTime":{'Fixed':{'mean':3}}},
         {"stationIdsList": ["E"],}]

#define the Jobs
J1=Job('J1','Job1',route=J1Route, priority=1, dueDate=100)
J2=Job('J2','Job2',route=J2Route, priority=1, dueDate=90)
J3=Job('J3','Job3',route=J3Route, priority=0, dueDate=110)


def main(input_index=0, test=0):
    # add all the objects in a list
    objectList=[M1,M2,M3,Q1,Q2,Q3,E,J1,J2,J3]  
    # set the length of the experiment  
    maxSimTime=float('inf')
    # call the runSimulation giving the objects and the length of the experiment
    runSimulation(objectList, maxSimTime)

    # return results for the test
    if test:
        returnSchedule=[]     
        for job in [J1,J2,J3]: 
            for record in job.schedule:
                returnSchedule.append([record[0].objName,record[1]])
        return returnSchedule
    
    # print the results
    for job in [J1,J2,J3]: 
        for record in job.schedule:
            print("Complex operation. Input index: {:2d}\n".format(input_index))
            print(job.name, "got into", record["station"].objName, "at", record["entranceTime"])
        print("-"*30)   

def gantt_chart():
    
    # Declaring a figure "gnt"
    fig, gnt = plt.subplots()
    
    # Setting Y-axis limits
    gnt.set_ylim(0, 50)
    
    # Setting X-axis limits
    gnt.set_xlim(0, 160)
    
    # Setting labels for x-axis and y-axis
    gnt.set_xlabel('Time')
    gnt.set_ylabel('Tasks')
    
    # Setting ticks on y-axis
    gnt.set_yticks([15, 25, 35])
    # Labelling tickes of y-axis
    gnt.set_yticklabels(['Job1', 'Job2', 'Job3'])
    
    # Setting graph attribute
    gnt.grid(True)
    
    # Declaring a bar in schedule
    gnt.broken_barh([(40, 50)], (30, 9), facecolors =('tab:orange'))
    
    # Declaring multiple bars in at same level and same width
    gnt.broken_barh([(110, 10), (150, 10)], (10, 9),
                            facecolors ='tab:blue')
    
    gnt.broken_barh([(10, 50), (100, 20), (130, 10)], (20, 9),
                                    facecolors =('tab:red'))
    plt.savefig("gantt1.png")

# Let's parallelize the code
iterations_count = round(1e7)

@timebudget
def run_complex_operations(operation, input, pool):
    pool.map(operation, input)

processes_count = 3

def comparison_chart(sequential_data=0, parallel_data=0):
    # Creating dataset
    parallel_data = [10, 22, 14]
    sequential_data = [11, 24, 22]

    n=3
    r = np.arange(n)
    width = 0.25
    
    
    plt.bar(r, sequential_data, color = 'b',
            width = width, edgecolor = 'black',
            label='Sequential')
    plt.bar(r + width, parallel_data, color = 'g',
            width = width, edgecolor = 'black',
            label='Parallel')
    
    plt.xlabel("Comparisons")
    plt.ylabel("Quantities")
    plt.title("Comparison btn Parallel and Sequential Codes")
    
    # plt.grid(linestyle='--')
    plt.xticks(r + width/2,['CPU','Memory','Latency'])
    plt.legend()
    
    plt.savefig("comparisons.png")

      
if __name__ == '__main__':

    # Start monitoring
    start = time.perf_counter()
    tracemalloc.start()
    main()
    # displaying the memory
    sequential_mem_usage = int(tracemalloc.get_traced_memory()[0])
    print("Sequential memory usage : ", sequential_mem_usage)
    # End monitoring
    tracemalloc.stop()
    # Calling psutil.cpu_precent() for 4 seconds
    sequential_cpu_usage = int(psutil.cpu_percent(4))
    print('Sequential CPU usage is: ', sequential_cpu_usage)
    # Measure latency
    sequential_latency = int(time.perf_counter() - start)
    print('sequential latency : {:.6f}s'.format(sequential_latency))
    sequential_data = [sequential_cpu_usage, sequential_mem_usage, sequential_latency]

    #gantt_chart()

    # Start monitoring
    start = time.perf_counter()
    tracemalloc.start()
    processes_pool = Pool(processes_count)
    run_complex_operations(main, range(10), processes_pool)
    # displaying the memory
    parallel_mem_usage = int(tracemalloc.get_traced_memory()[0])
    print("Parallel memory usage : ", parallel_mem_usage)
    # End monitoring
    tracemalloc.stop()
    # Calling psutil.cpu_precent() for 4 seconds
    parallel_cpu_usage = int(psutil.cpu_percent(4))
    print('Parallel CPU usage is: ', parallel_cpu_usage)
    # Measure latency
    parallel_latency = int(time.perf_counter() - start)
    print('Parallel latency : {:.6f}s'.format(parallel_latency))
    parallel_data = [parallel_cpu_usage, parallel_mem_usage, parallel_latency]

    comparison_chart(parallel_data=parallel_data, sequential_data=sequential_data)

