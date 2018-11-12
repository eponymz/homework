// main file to determine which submission node to run
#include <iostream>
#include <string>
#include "Strings.h"
#include "Definition.h"

using namespace std;

int main() {
    cout << "Welcome to Unit 2. Which file would you like to run? (string/definition)" << endl;
    string fileChoice;
    cin >> fileChoice;
    if (fileChoice == "string") {
        Strings strings;
        strings.stringMain();
        main();
    }
    else if (fileChoice == "definition") {
        Definition definition;
        definition.defMain();
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

