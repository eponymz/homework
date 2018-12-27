// main file to determine which submission node to run
#include <iostream>
#include <string>
#include "Rectangles.h"

using namespace std;

int main() {
    cout << "Which file would you like to run? (rectangle/features)" << endl;
    string userChoice;
    cin >> userChoice;
    if (userChoice == "rectangle") {
        RectangleMain();
    } else if (userChoice == "features") {
        cout << "Not done yet.." << endl;
        return 500;
    } else {
        cout << "Invalid option.." << endl;
        main();
    }
}

//
// Created by Ian Sabey on 12/26/18.
//
