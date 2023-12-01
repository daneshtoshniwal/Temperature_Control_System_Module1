#include <iostream>
#include <thread>
#include <chrono>
#include <vector>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <random>
#include <fstream>
#include "SensorData.h"

// Implement a function to initialize the struct
void init(SensorData* structPtr) {
    structPtr->mtype=0; // Message type, must be greater than 0
    structPtr->rackId=0;
    structPtr->sensorId=0;
    structPtr->temperature=0;
    structPtr->fanspeed=0;
    structPtr->timestamp=0;
}

// Define an example variable of the struct
SensorData Sensor;