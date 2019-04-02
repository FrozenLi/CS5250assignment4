'''
CS5250 Assignment 4, Scheduling policies simulator
Sample skeleton program
Input file:
    input.txt
Output files:
    FCFS.txt
    RR.txt
    SRTF.txt
    SJF.txt
'''
import sys
import copy

input_file = 'input.txt'

class Process:
    last_scheduled_time = 0
    def __init__(self, id, arrive_time, burst_time):
        self.id = id
        self.arrive_time = arrive_time
        self.burst_time = burst_time
    #for printing purpose
    def __repr__(self):
        return ('[id %d : arrival_time %d,  burst_time %d]'%(self.id, self.arrive_time, self.burst_time))

def FCFS_scheduling(process_list):
    #store the (switching time, proccess_id) pair
    schedule = []
    current_time = 0
    waiting_time = 0
    for process in process_list:
        if(current_time < process.arrive_time):
            current_time = process.arrive_time
        schedule.append((current_time,process.id))
        waiting_time = waiting_time + (current_time - process.arrive_time)
        current_time = current_time + process.burst_time
    average_waiting_time = waiting_time/float(len(process_list))
    return schedule, average_waiting_time

#Input: process_list, time_quantum (Positive Integer)
#Output_1 : Schedule list contains pairs of (time_stamp, proccess_id) indicating the time switching to that proccess_id
#Output_2 : Average Waiting Time
def RR_scheduling(process_list, time_quantum ):



    return (["to be completed, scheduling process_list on round robin policy with time_quantum"], 0.0)

def SRTF_scheduling(process_list):
    remaining_process = copy.deepcopy(process_list)
    schedule=[]
    available_process=[]
    current_time=0
    waiting_time=0
    for process in process_list:
        available_process,actions,current_time=process_SRTF(available_process,start_time=current_time,end_time=process.arrive_time)
        schedule=schedule+actions
        available_process.append(process)
    available_process+=process_SRTF(available_process,start_time=current_time,end_time=1000)
    return schedule, 0.0

def process_SRTF(available_process,start_time,end_time):
    if len(available_process)<=0:
        return available_process,[],start_time
    current_time = start_time
    processes=[]
    while current_time<end_time and (check_complete(available_process)==False):

        process_to_do_pos = min_process(available_process)

        if available_process[process_to_do_pos].burst_time+current_time<=end_time:
            processes.append((current_time,available_process[process_to_do_pos].id))
            current_time+=available_process[process_to_do_pos].burst_time
            available_process[process_to_do_pos].burst_time=0

        else:
            processes.append((current_time,available_process[process_to_do_pos].id))
            available_process[process_to_do_pos].burst_time=available_process[process_to_do_pos].burst_time-(end_time-current_time)
            current_time=end_time

    return available_process,processes,current_time

def check_complete(process_list):
    for process in process_list:
        if process.burst_time>0:
            return False
    return True


def min_process(available_process):
    #find one non complete task

    for i in range(0,len(available_process)):
        if available_process[i].burst_time>0:
            min_process_pos=i
            break

    #find minimum
    for i in range(0,len(available_process)):
        if available_process[i].burst_time<available_process[min_process_pos].burst_time and available_process[i].burst_time>0:
            min_process_pos=i
    return min_process_pos




def SJF_scheduling(process_list, alpha):
    return (["to be completed, scheduling SJF without using information from process.burst_time"],0.0)


def read_input():
    result = []
    with open(input_file) as f:
        for line in f:
            array = line.split()
            if (len(array)!= 3):
                print ("wrong input format")
                exit()
            result.append(Process(int(array[0]),int(array[1]),int(array[2])))
    return result
def write_output(file_name, schedule, avg_waiting_time):
    with open(file_name,'w') as f:
        for item in schedule:
            f.write(str(item) + '\n')
        f.write('average waiting time %.2f \n'%(avg_waiting_time))


def main(argv):
    process_list = read_input()
    print ("printing input ----")
    for process in process_list:
        print (process)
    print ("simulating FCFS ----")
    FCFS_schedule, FCFS_avg_waiting_time =  FCFS_scheduling(process_list)
    write_output('FCFS.txt', FCFS_schedule, FCFS_avg_waiting_time )
    print ("simulating RR ----")
    RR_schedule, RR_avg_waiting_time =  RR_scheduling(process_list,time_quantum = 2)
    write_output('RR.txt', RR_schedule, RR_avg_waiting_time )
    print ("simulating SRTF ----")
    SRTF_schedule, SRTF_avg_waiting_time =  SRTF_scheduling(process_list)
    write_output('SRTF.txt', SRTF_schedule, SRTF_avg_waiting_time )
    print ("simulating SJF ----")
    SJF_schedule, SJF_avg_waiting_time =  SJF_scheduling(process_list, alpha = 0.5)
    write_output('SJF.txt', SJF_schedule, SJF_avg_waiting_time )

if __name__ == '__main__':
    main(sys.argv[1:])
