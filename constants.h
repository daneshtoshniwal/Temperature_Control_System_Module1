#include <vector>
#ifndef CONSTANTS_H
#define CONSTANTS_H

namespace constants {
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
}
#endif 