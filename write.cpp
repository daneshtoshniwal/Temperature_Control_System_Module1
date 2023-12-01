#include <iostream>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <ctime>
#include<chrono>
#include<thread>
using namespace std;

// Structure for output data
struct outputData {
    long mytype;
    time_t timestamp;
    int rack_id;
    int server_id;
    int fan_speed;
    int change_Speed;
};

int main() {
    // Create a message queue for IPC
    key_t key = ftok(".", 'a');
    if (key == -1) {
        perror("ftok");
        exit(EXIT_FAILURE);
    }

    int msgQueueId = msgget(key, IPC_CREAT | 0666);
    if (msgQueueId == -1) {
        perror("msgget");
        exit(EXIT_FAILURE);
    }

    // Create and send 20-30 instances of outputData
    int cnt=0;
    int val=100;
    while(true){
        for (int i = 0; i < 1; ++i) {
            outputData data;
            data.mytype=1;
            data.timestamp = std::time(nullptr);
            data.rack_id = cnt%10; // Assuming there are 5 racks
            data.server_id = i; // Assuming there are 3 servers per rack
            data.fan_speed = 100 ; // Example fan speed value
            // data.change_Speed = i % 10; // Example change speed value
            data.change_Speed=val;

            // Send the data through the message queue
            if (msgsnd(msgQueueId, &data, sizeof(data) - sizeof(long), 0) == -1) {
                perror("msgsnd");
                exit(EXIT_FAILURE);
            }

            cout << "Data sent: " << "Rack " << data.rack_id << ", Server " << data.server_id
                << ", Fan Speed " << data.fan_speed << ", Change Speed " << data.change_Speed << "\n";
        }
        std::this_thread::sleep_for(std::chrono::milliseconds(2000));
        cnt++;
    }

    // Cleanup - remove the message queue
    if (msgctl(msgQueueId, IPC_RMID, nullptr) == -1) {
        perror("msgctl");
        exit(EXIT_FAILURE);
    }

    return 0;
}