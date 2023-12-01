
#include <iostream>

#include <sys/types.h>

#include <sys/ipc.h>

#include <sys/msg.h>

#include <unistd.h>

 

using namespace std;

 

// Structure for temperature data

struct SensorData {

    long mtype; // Message type, must be greater than 0

    int rackId;

    int sensorId;

    double temperature;
   // double fanspeed;
    time_t timestamp;
};

 

int main() {

    // Create a message queue for IPC

    key_t key = ftok(".", 'q');

    if (key == -1) {

        perror("ftok");

        exit(EXIT_FAILURE);

    }

 

    int msgQueueId = msgget(key, 0666);

    if (msgQueueId == -1) {

        perror("msgget");

        exit(EXIT_FAILURE);

    }

 

    // Receive messages from the message queue

    while (true) {

        SensorData sensorData;

        ssize_t receivedBytes = msgrcv(msgQueueId, &sensorData, sizeof(sensorData) - sizeof(long), 1, 0);

 

        if (receivedBytes == -1) {

            perror("msgrcv");

            exit(EXIT_FAILURE);

        }

 

        // Check for termination message

        if (sensorData.temperature == -1.0) {

            cout << "Termination message received. Exiting...\n";

            break;

        }

 

        // Print received temperature data

        cout << "Received message: Rack " << sensorData.rackId << ", Sensor " << sensorData.sensorId

             << ", Temperature: " << sensorData.temperature << "°C\n";
            time_t timestamp = sensorData.timestamp;
	    cout << "Received timestamp: " << (timestamp);
    }

 

    return 0;

}
