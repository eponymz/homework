// main file to determine which submission node to run
#include <iostream>
#include <string>
#include <map>
#include "Vehicles.h"
#include "Vertebrates.h"

using namespace std;

string getUserChoice() {
    string userResponse, userRespType;
    cout << "What kind of vertebrate would you like info on? "
            "birds/mammals/reptiles/amphibians" << endl;
    cin >> userResponse;
    if (userResponse == "birds") {
        // secondary question to make the program seem more user friendly
        cout << "What kind of bird?" << endl;
        cin >> userRespType;
        new Bird(userRespType);
    } else if (userResponse == "mammals") {
        // secondary question to make the program seem more user friendly
        cout << "What kind of mammal?" << endl;
        cin >> userRespType;
        new Mammal(userRespType);
    } else if (userResponse == "reptiles") {
        // secondary question to make the program seem more user friendly
        cout << "What kind of reptile?" << endl;
        cin >> userRespType;
        new Reptile(userRespType);
    } else if (userResponse == "amphibians") {
        // secondary question to make the program seem more user friendly
        cout << "What kind of amphibian?" << endl;
        cin >> userRespType;
        new Amphibian(userRespType);
    } else {
        cout << "Please enter an option from above.";
        getUserChoice();
    }
    return std::string();
};

void runVehicle() {
    string userChoice;
    string vehicleTypes[5] = {"sedan","minivan","crossover","coupe","convertible"};
    cout << "What kind of vehicle would you like details on? "
            "(sedan/minivan/crossover/coupe/convertible)" << endl;
    cin >> userChoice;
    if (userChoice == vehicleTypes[0]) {
        new Sedan();
    } else if (userChoice == vehicleTypes[1]) {
        new Minivan();
    } else if (userChoice == vehicleTypes[2]) {
        new Crossover();
    } else if (userChoice == vehicleTypes[3]) {
        new Coupe();
    } else if (userChoice == vehicleTypes[4]) {
        new Convertible();
    } else {
        cout << "Invalid option entered..\nReturning to main.." << endl;
    }
}

int main()
{
    string fileChoice;
    cout << "Which file would you like to run? (vehicle/vertebrates)" << endl;
    cin >> fileChoice;
    if (fileChoice == "vertebrates") {
        getUserChoice();
        main();
    } else if (fileChoice == "vehicle") {
        runVehicle();
        main();
    } else {
        cout << "Not a valid option.." << endl;
        main();
    }
}

//
// Created by Ian Sabey on 12/24/18.
//
