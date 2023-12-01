#include <CppUTest/TestHarness.h>
#include <CppUTest/CommandLineTestRunner.h>
// #include "main4.cpp"
#include <iostream>
#include <thread>
#include <chrono>
#include <vector>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <random>
#include <fstream>
// #include <bits/stdc++.h>
#include "SensorData.h"
#include "inputData.h"
#include "constants.h"
// #include <set>
using namespace std;

#define EPOCH_TIME 0
#define MIN_TEMP -273.15

#define MIN_RANGE_ID -1
#define MAX_RANGE_ID 8 

#define MIN_RACK_ID 0
#define MAX_RACK_ID 11

#define MIN_SENSOR_ID 0
#define MAX_SENSOR_ID 1

#define MIN_FANSPEED 0
#define MAX_FANSPEED 4000

#define REC 10

#define MAX_PROCESSING_DURATION 10000

#define CHECK_MTYPE(mtype) \
{ \
    if (mtype < MIN_RANGE_ID) { \
        FAIL("mtype is invalid."); \
    } \
}

#define CHECK_RACKID(rackID) \
{ \
    if (rackID < MIN_RACK_ID || rackID > MAX_RACK_ID) { \
        FAIL("rack ID is invalid."); \
    } \
}

#define CHECK_SENSORID(sensorID) \
{ \
    if (sensorID < MIN_SENSOR_ID || sensorID > MAX_SENSOR_ID) { \
        FAIL("sensor ID is invalid."); \
    } \
}


#define CHECK_RANGE(range) \
{ \
    if (range < MIN_RANGE_ID || range > MAX_RANGE_ID) { \
        FAIL("range is invalid."); \
    } \
}

#define CHECK_TEMP(temp) \
{ \
    if (temp < MIN_TEMP) { \
        FAIL("Temperatue is invalid."); \
    } \
}

#define CHECK_DATETIME(timestamp) \
{ \
    string formatted_time = ctime(&timestamp);\
    if (timestamp < EPOCH_TIME) { \
        FAIL("timestamp is invalid."); \
    } \
}

#define CHECK_TIME_CONSTRAINT(duration)\
{\
    if(duration > MAX_PROCESSING_DURATION)\
    {\
        FAIL("Too much time elapsed in processing."); \
    }\
}\

#define CHECK_EQUAL_STRUCTS(struct1,struct2)\
{\
    if(struct1.required_temperature != struct2.required_temperature)\
    {\
        FAIL("The processing required is incorrect."); \
    }\
}\

#define CHECK_FANSPEED(fanspeed)\
{\
    if (fanspeed < MIN_FANSPEED || fanspeed > MAX_FANSPEED) { \
        FAIL("fanspeed is invalid."); \
    } \
}\

#define CHECK_REC(rec)\
{\
    if (rec != REC) { \
        FAIL("rec is invalid."); \
    } \
}\

// Create a TestFixture class for testing
TEST_GROUP(TemperatureSimulationTestGroup)
{
    // Declare variables needed for testing
    vector<vector<double>> temperatures;
    bool terminate;

    void setup() 
    {
        // Initialize variables before each test
        // temperatures = vector<vector<double>>(numRacks, vector<double>(numSensorsPerRack, 30.0));
        // terminate = false;
    }

    void teardown() 
    {
        // Cleanup after each test (if needed)
    }
};

// Write a simple test
TEST(TemperatureSimulationTestGroup, OutputTest)
{

    // key_t key = ftok(".", 'q');

    // if (key == -1) {

    //     perror("ftok");

    //     exit(EXIT_FAILURE);

    // }

    // int msgQueueId = msgget(key, 0666);

    // if (msgQueueId == -1) {

    //     perror("msgget");

    //     exit(EXIT_FAILURE);

    // }

    // // Receive messages from the message queue
    // int cnt=15;
    // while (cnt--) {
    //     SensorData sensorData;

    //     ssize_t receivedBytes = msgrcv(msgQueueId, &sensorData, sizeof(sensorData) - sizeof(long), 1, 0);

    //     CHECK_RACKID(sensorData.rackId);
    //     CHECK_SENSORID(sensorData.sensorId);
    //     CHECK_TEMP(sensorData.temperature);
    //     CHECK_DATETIME(sensorData.timestamp);

    //     if (receivedBytes == -1) {

    //         perror("msgrcv");

    //         exit(EXIT_FAILURE);

    //     }

 

    //     // Check for termination message

    // }
}

TEST(TemperatureSimulationTestGroup, OutputTest1)
{

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
    vector<int> count(10,0);
 

    // Receive messages from the message queue
    // set<int> st;
    int cnt=21;
    while (cnt--) {

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

        count[sensorData.rackId]++;
        // st.insert(sensorData.rackId);
        // if(st.size()==10){
        //     cout<<"Recieved data from each rack sucessfully. "<<endl;
        //     st.clear();
        // }
        // Print received temperature data
        // cout << "Received message: Rack " << sensorData.rackId << ", Sensor " << sensorData.sensorId

        //      << ", Temperature: " << sensorData.temperature << "°C\n";
        //     time_t timestamp = sensorData.timestamp;
	    // cout << "Received timestamp: " << ctime(&timestamp);
    }
    int rec=0;
    for(int i=0;i<10;i++){
        if(count[i]>0){rec++;}
    }
    CHECK_REC(rec);

    return ;

}


TEST(TemperatureSimulationTestGroup, TimeTest)
{
    time_t timestampstart;
    time_t timestampend;
    
}

TEST(TemperatureSimulationTestGroup, InputTest)
{
    // vector<int> fanspeed = {0,0,0,0,0,0,0,0,0,0};
    // key_t key = ftok(".", 'a');
    // if (key == -1) {
    //     perror("ftok");
    //     exit(EXIT_FAILURE);
    // }

    // int msgQueueId = msgget(key,0666);
    // if (msgQueueId == -1) {
    //     perror("msgget");
    //     exit(EXIT_FAILURE);
    // }

    // int cnt = 10;
    // while (cnt--) {
    //     // Receive user input from the message queue
    //     // Customize this part based on your message structure
    //     inputData userInput;
    //     if (msgrcv(msgQueueId, &userInput, sizeof(userInput) - sizeof(long), 1, 0) == -1) {
    //         perror("msgrcv");
    //         cout<<"error"<<endl;
    //         exit(EXIT_FAILURE);
    //     }
    //     fanspeed[userInput.rack_id]+=userInput.change_Speed;
    //     // cout<<" "<<fanspeed[userInput.rack_id]<<endl;
    //     CHECK_FANSPEED(fanspeed[userInput.rack_id]);
    // }    
}

int main(int ac, char** av)
{
    // Initialize CppUTest framework
    return CommandLineTestRunner::RunAllTests(ac, av);
}