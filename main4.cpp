#include <iostream>
#include <thread>
#include <chrono>
#include <vector>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <random>
#include <fstream>

using namespace std;

// Constants
const int numRacks = 10;
const int numSensorsPerRack = 1;
const int updateInterval = 100; // in milliseconds
const double temperatureIncreaseRate = (85.0 - 30.0) / 5000.0; // Increase from 30 to 85 in 5 seconds
const double temperatureDecreaseRate = (85.0 - 30.0) / 5000.0; // Decrease from 85 to 30 in 5 seconds
const double temperatureIncreaseRate1 = (85.0 - 30.0) / 9000.0; // Increase from 30 to 85 in 9 seconds
const double temperatureDecreaseRate1 = (85.0 - 30.0) / 5000.0; // Decrease from 85 to 30 in 5 seconds
const double temperatureIncreaseRate2 = (85.0 - 30.0) / 2000.0; // Increase from 30 to 85 in 2 seconds
const double temperatureDecreaseRate2 = (85.0 - 30.0) / 5000.0; // Decrease from 85 to 30 in 5 seconds
const double temperatureIncreaseRate3 = (85.0 - 30.0) / 12000.0; // Increase from 30 to 85 in 12 seconds
const double temperatureDecreaseRate3 = (85.0 - 30.0) / 5000.0; // Decrease from 85 to 30 in 5 seconds
const double temperatureIncreaseRate4 = (85.0 - 30.0) / 10000.0; // Increase from 30 to 85 in 10 seconds
const double temperatureDecreaseRate4 = (85.0 - 30.0) / 5000.0; // Decrease from 85 to 30 in 5 seconds
const double temperatureIncreaseRates[numRacks] = {
    temperatureIncreaseRate,
    temperatureIncreaseRate1,
    temperatureIncreaseRate2,
    temperatureIncreaseRate3,
    temperatureIncreaseRate4,
    temperatureIncreaseRate,
    temperatureIncreaseRate1,
    temperatureIncreaseRate2,
    temperatureIncreaseRate3,
    temperatureIncreaseRate4

};
const double exporate[numRacks]={
    1.05,
    1.02,
    1.1,
    1.02,
    1.02,
    1.05,
    1.02,
    1.1,
    1.02,
    1.02,
};
vector<int> trend ={1,1,1,1,1,1,1,1,1,1};
vector<int> fanspeed = {0,0,0,0,0,0,0,0,0,0};
//int trend[numRacks]; // Array to store trend for each rack
// memset(trend, 1, sizeof(trend));
//memset((&trend[0], 1, sizeof(trend));

// Initialize all racks with increasing trend
// for (int i = 0; i < numRacks; ++i) {
//     trend[i] = 1;
// }

// Structure for temperature data
struct SensorData {
    long mtype; // Message type, must be greater than 0
    int rackId;
    int sensorId;
    double temperature;
   // double fanspeed;
    time_t timestamp;
};

struct inputData {
    long mytype;
    time_t timestamp;
    int rack_id;
    int server_id;
    int fan_speed;
    int change_Speed;
};
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
        // cout<<fanspeed[userInput.rack_id]<<endl;
        // cout<<userInput.rack_id<<" "<<userInput.server_id<<endl;
        // cout<<userInput.timestamp<<endl;
        // Modify the shared data based on user input
        // trend[userInput.rackId] = userInput.fanspeed; // Assuming fanspeed is used for modification
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
            for (int rackId = 0; rackId < numRacks; ++rackId) {
                // cout<<fanspeed[rackId]<<" ";
                for (int sensorId = 0; sensorId < numSensorsPerRack; ++sensorId) {
                    // Simulate temperature increase
                    

                    // If temperature exceeds 85, start decreasing
                    // if (trend[rackId]==-1) {
			        //     //cout<<temperatures[rackId][sensorId]<<" "<<endl;
                    //     double decrease = temperatureDecreaseRate * updateInterval * (1.0 + rand() / (RAND_MAX + 1.0) * 0.2); 						
                    //     temperatures[rackId][sensorId] -= decrease;
					// 	if(temperatures[rackId][sensorId] < 30.0){trend[rackId]=1;}
                    // }
					// else if(trend[rackId]==1){
					// 	 double increase=temperatureIncreaseRates[rackId]*updateInterval*(1.0 + rand() / (RAND_MAX + 1.0)*0.2); 
					// 	//double increase = temperatureIncreaseRate * updateInterval * (1.0 + rand() / (RAND_MAX + 1.0) * 0.2); 							
                    // 	temperatures[rackId][sensorId] += increase;
					// 	if(temperatures[rackId][sensorId] > 85.0){trend[rackId]=-1;}
							
					// }
                    if(temperatures[rackId][sensorId]<45 and trend[rackId]==1){
                        // TEMP<45 and increasing trend.
                        // fan is switched off
                        // if(fanspeed[rackId]!=0){cout<<"Error_phase1"<<endl;}
                        temperatures[rackId][sensorId]=temperatures[rackId][sensorId]*exporate[rackId];
                    }
                    else if(temperatures[rackId][sensorId]<65 and trend[rackId]==1){
                        if(fanspeed[rackId]<1500 and temperatures[rackId][sensorId]<55 ){
                            temperatures[rackId][sensorId]=temperatures[rackId][sensorId]*exporate[rackId];
                        }
                        else{
                            double increase=temperatureIncreaseRates[rackId]*updateInterval*(1.0 + rand() / (RAND_MAX + 1.0)*0.2); 
                            temperatures[rackId][sensorId] += increase;
                        }
                    }
                    else if(temperatures[rackId][sensorId]<85 and trend[rackId]==1){
                         if(fanspeed[rackId]<2500 and temperatures[rackId][sensorId]<75){
                            temperatures[rackId][sensorId]=temperatures[rackId][sensorId]*exporate[rackId];
                        }
                        else{
                            double increase=temperatureIncreaseRates[rackId]*updateInterval*(1.0 + rand() / (RAND_MAX + 1.0)*0.2); 
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
                        double decrease = temperatureDecreaseRate * updateInterval * (1.0 + rand() / (RAND_MAX + 1.0) * 0.2); 						
                        temperatures[rackId][sensorId] -= decrease;
						if(temperatures[rackId][sensorId] < 30.0){trend[rackId]=1;}
                    }

                     SensorData sensorData{1, rackId, sensorId, temperatures[rackId][sensorId],std::time(nullptr)	};
                    
                     //cout<<x<<endl;
                    if (msgsnd(msgQueueId, &sensorData, sizeof(sensorData) - sizeof(long), 0) == -1) {
                         perror("msgsnd");
                         exit(EXIT_FAILURE);
                    }
                }
            }
            // cout<<endl;

            // Print temperatures in real time
            for (int rackId = 0; rackId < numRacks; ++rackId) {
                for (int sensorId = 0; sensorId < numSensorsPerRack; ++sensorId) {
                    cout << "Rack " << rackId << ", Sensor " << sensorId
                         << ": " <<temperatures[rackId][sensorId] << "°C\n";
                }
            }
            cout << "-----------------------\n";
            for (int rackId = 0; rackId < numRacks; ++rackId) {
                for (int sensorId = 0; sensorId < numSensorsPerRack; ++sensorId) {
                    outfile << "Rack " << rackId << ", Sensor " << sensorId
                            << ": " << temperatures[rackId][sensorId] << "°C\n";
                }
            }

            outfile << "-----------------------\n";

            // Wait for the next update
            this_thread::sleep_for(chrono::milliseconds(updateInterval));
        }
    } catch (const exception& e) {
        cerr << "Error in temperature simulation thread: " << e.what() << endl;
    }
}

int main() {
    // Initialize temperatures
    vector<vector<double>> temperatures(numRacks, vector<double>(numSensorsPerRack, 30.0));

    // Create a message queue for IPC
    key_t key = ftok(".", 'q');
    if (key == -1) {
        perror("ftok");
        exit(EXIT_FAILURE);
    }
    key_t key2 = ftok(".", 'a');
    if (key2 == -1) {
        perror("ftok");
        exit(EXIT_FAILURE);
    }

    int msgQueueId = msgget(key, IPC_CREAT | 0666);
    if (msgQueueId == -1) {
        perror("msgget");
        exit(EXIT_FAILURE);
    }
    int msgQueueId2 = msgget(key2,0666);
    if (msgQueueId2 == -1) {
        perror("msgget");
        exit(EXIT_FAILURE);
    }

    // Create a thread for simulating temperature
    bool terminate = false;
    thread temperatureThread(simulateTemperature, ref(temperatures), msgQueueId, ref(terminate));

    // Create a thread for handling user input
    thread userInputThread(handleUserInput, msgQueueId2, ref(trend), ref(terminate));

    // Wait for user to terminate the program (press Enter)
    cout << "Press Enter to terminate the program...\n";
    cin.get(); 


    // Set the terminate flag to true
    terminate = true;

    // Join both threads
    temperatureThread.join();
    userInputThread.join();

    // Cleanup - remove the message queue
    if (msgctl(msgQueueId, IPC_RMID, nullptr) == -1) {
        perror("msgctl");
        exit(EXIT_FAILURE);
    }

    return 0;
}

