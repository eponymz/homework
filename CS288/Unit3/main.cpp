// main file to determine which submission node to run
#include <iostream>
#include <string>
#include <map>
#include "Vertebrates.h"

using namespace std;

int main() {
    cout << "Welcome to Unit 3. Which file would you like to run? (string/construct)" << endl;
    string fileChoice;
    cin >> fileChoice;
    if (fileChoice == "string") {
        cout << "Not completed yet.." << endl;
        main();
    }
    else if (fileChoice == "construct") {
        cout << "Let's build a lizard." << endl;
        Vertebrate lizard;
        lizard.setIsReptile();
        string lizardSkin = lizard.getSkinCover();
        string lizardType = lizard.getAnimalType();
        int lizardLegs = lizard.getAppendages();
        cout << "Lizards are " << lizardType << ", they have " << lizardSkin << " covering their skin, and they have "
        << lizardLegs << " legs." << endl;
        main();
    }
    else
    {
        cout << "That is an invalid option" << endl;
        main();
    }
}

//
// Created by Ian Sabey on 10/17/18.
//
