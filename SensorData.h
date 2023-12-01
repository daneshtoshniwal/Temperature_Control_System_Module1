#include <iostream>
#include <thread>
#include <chrono>
#include <vector>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <random>
#include <fstream>
#ifndef SENSORDATA_H
#define SENSORDATA_H

// Define the structure
typedef struct SensorData {
    long mtype; // Message type, must be greater than 0
    int rackId;
    int sensorId;
    double temperature;
    time_t timestamp;
} Sensor;

#endif