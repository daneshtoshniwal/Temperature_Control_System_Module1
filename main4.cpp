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
#include "inputData.h"
#include "constants.h"
using namespace std;
vector<int> trend ={1,1,1,1,1,1,1,1,1,1};
vector<int> fanspeed = {0,0,0,0,0,0,0,0,0,0};
// Function to handle user input from the message queue
void handleUserInput(int msgQueueId, vector<int>& trend, bool& terminate) {
    try {
         while (!terminate) {
        // Receive user input from the message queue
        // Customize this part based on your message structure
        inputData userInput;
        if (msgrcv(msgQueueId, &userInput, sizeof(userInput) - sizeof(long), 1, 0) == -1) {
            perror("msgrcv");
            cout<<"error"<<endl;
            exit(EXIT_FAILURE);
        }
        fanspeed[userInput.rack_id]+=userInput.change_Speed;
     }
    } catch (const exception& e) {
        cerr << "Error in temperature simulation thread: " << e.what() << endl;
    }
   
}
// Function to simulate temperature sensors
void simulateTemperature(vector<vector<double>>& temperatures, int msgQueueId, bool& terminate) {
    random_device rd;
    mt19937 gen(rd());
	// int trend=1; // INCREASING TREND 
    ofstream outfile("temperatures.txt", ios::app);
    try {
        while (!terminate) {
			// RACKID - 0,1,2,3,4
            for (int rackId = 0; rackId < constants::numRacks; ++rackId) {
                // cout<<fanspeed[rackId]<<" ";
                for (int sensorId = 0; sensorId < constants::numSensorsPerRack; ++sensorId) {
                    if(temperatures[rackId][sensorId]<45 and trend[rackId]==1){
                        // TEMP<45 and increasing trend.
                        // fan is switched off
                        // if(fanspeed[rackId]!=0){cout<<"Error_phase1"<<endl;}
                        temperatures[rackId][sensorId]=temperatures[rackId][sensorId]*constants::exporate[rackId];
                    }
                    else if(temperatures[rackId][sensorId]<65 and trend[rackId]==1){
                        if(fanspeed[rackId]<1500 and temperatures[rackId][sensorId]<55 ){
                            temperatures[rackId][sensorId]=temperatures[rackId][sensorId]*constants::exporate[rackId];
                        }
                        else{
                            double increase=constants::temperatureIncreaseRates[rackId]*constants::updateInterval*(1.0 + rand() / (RAND_MAX + 1.0)*0.2); 
                            temperatures[rackId][sensorId] += increase;
                        }
                    }
                    else if(temperatures[rackId][sensorId]<85 and trend[rackId]==1){
                         if(fanspeed[rackId]<2500 and temperatures[rackId][sensorId]<75){
                            temperatures[rackId][sensorId]=temperatures[rackId][sensorId]*constants::exporate[rackId];
                        }
                        else{
                            double increase=constants::temperatureIncreaseRates[rackId]*constants::updateInterval*(1.0 + rand() / (RAND_MAX + 1.0)*0.2); 
                            temperatures[rackId][sensorId] += increase;
                        }
                    }
                    else if(temperatures[rackId][sensorId]>=85 and trend[rackId]==1){
                        // ASSUME 4000 
                        // if(fanspeed[rackId]<4000){cout<<"error_lastphase"<<endl;}
                        trend[rackId]=-1;
                    }
                    if (trend[rackId]==-1) {
			            //cout<<temperatures[rackId][sensorId]<<" "<<endl;
                        double decrease = constants::temperatureDecreaseRate * constants::updateInterval * (1.0 + rand() / (RAND_MAX + 1.0) * 0.2); 						
                        temperatures[rackId][sensorId] -= decrease;
						if(temperatures[rackId][sensorId] < 30.0){trend[rackId]=1;}
                    }

                     SensorData sensorData{1, rackId, sensorId, temperatures[rackId][sensorId],fanspeed[rackId],std::time(nullptr)	};
                    
                     //cout<<x<<endl;
                    if (msgsnd(msgQueueId, &sensorData, sizeof(sensorData) - sizeof(long), 0) == -1) {
                         perror("msgsnd");
                         exit(EXIT_FAILURE);
                    }
                }
            }
            // Print temperatures in real time
            
            for (int rackId = 0; rackId < constants::numRacks; ++rackId) {
                for (int sensorId = 0; sensorId < constants::numSensorsPerRack; ++sensorId) {
                    cout << "Rack " << rackId << ", Sensor " << sensorId
                         << ": " <<temperatures[rackId][sensorId] << "°C"<<" "<<fanspeed[rackId]<<endl;
                }
            }
            cout << "-----------------------\n";
            for (int rackId = 0; rackId < constants::numRacks; ++rackId) {
                for (int sensorId = 0; sensorId < constants::numSensorsPerRack; ++sensorId) {
                    outfile << "Rack " << rackId << ", Sensor " << sensorId
                            << ": " << temperatures[rackId][sensorId] << "°C\n";
                }
            }

            outfile << "-----------------------\n";

            // Wait for the next update
            this_thread::sleep_for(chrono::milliseconds(constants::updateInterval));
        }
    } catch (const exception& e) {
        cerr << "Error in temperature simulation thread: " << e.what() << endl;
    }
}

int main() {
    // Initialize temperatures
    vector<vector<double>> temperatures(constants::numRacks, vector<double>(constants::numSensorsPerRack, 30.0));

    // Create a message queue for IPC
    key_t key = ftok(".", 'q');
    if (key == -1) {
        perror("ftok");
        exit(EXIT_FAILURE);
    }
    // key_t key2 = ftok(".", 'a');
    // if (key2 == -1) {
    //     perror("ftok");
    //     exit(EXIT_FAILURE);
    // }

    int msgQueueId = msgget(key, IPC_CREAT | 0666);
    if (msgQueueId == -1) {
        perror("msgget");
        exit(EXIT_FAILURE);
    }
    // int msgQueueId2 = msgget(key2,0666);
    // if (msgQueueId2 == -1) {
    //     perror("msgget");
    //     exit(EXIT_FAILURE);
    // }

    // Create a thread for simulating temperature
    bool terminate = false;
    thread temperatureThread(simulateTemperature, ref(temperatures), msgQueueId, ref(terminate));

    // // Create a thread for handling user input
    // thread userInputThread(handleUserInput, msgQueueId2, ref(trend), ref(terminate));

    // Wait for user to terminate the program (press Enter)
    cout << "Press Enter to terminate the program...\n";
    cin.get(); 


    // Set the terminate flag to true
    terminate = true;

    // Join both threads
    temperatureThread.join();
    // userInputThread.join();

    // Cleanup - remove the message queue
    if (msgctl(msgQueueId, IPC_RMID, nullptr) == -1) {
        perror("msgctl");
        exit(EXIT_FAILURE);
    }
    return 0;
}

