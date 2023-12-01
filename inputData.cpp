#include <iostream>
#include <thread>
#include <chrono>
#include <vector>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <random>
#include <fstream>
#include "inputData.h"

// Implement a function to initialize the struct
void init(inputData* structPtr) {
    structPtr->mytype=0; // Message type, must be greater than 0
    structPtr->rack_id=0;
    structPtr->server_id=0;
    structPtr->fan_speed=0;
    structPtr->change_Speed=0;
    structPtr->timestamp=0;

}

// Define an example variable of the struct
inputData input;