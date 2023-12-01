#include <iostream>
#include <thread>
#include <chrono>
#include <vector>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <random>
#include <fstream>
#ifndef INPUTDATA_H
#define INPUTDATA_H

// Define the structure
typedef struct inputData {
    long mytype;
    time_t timestamp;
    int rack_id;
    int server_id;
    int fan_speed;
    int change_Speed;
} input;

#endif