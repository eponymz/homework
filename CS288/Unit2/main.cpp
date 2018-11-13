// main file to determine which submission node to run
#include <iostream>
#include <string>
#include "Strings.h"
#include "Definition.h"

using namespace std;

int main() {
    cout << "Welcome to Unit 2. Which file would you like to run? (string/construct)" << endl;
    string fileChoice;
    cin >> fileChoice;
    if (fileChoice == "string") {
        Strings strings;
        strings.stringMain();
        main();
    }
    else if (fileChoice == "construct") {
        string backBone, mammal, isExtinct;
        string animal, envHabitat;
        cout << "What type of animal would you like to enter?" << endl;
        cin >> animal;
        cout << "Does this animal have a backbone?(true/false)" << endl;
        cin >> backBone;
        cout << "Is this animal a mammal?(true/false)" << endl;
        cin >> mammal;
        cout << "Is this animal extinct?(true/false)" << endl;
        cin >> isExtinct;
        cout << "What kind of habitat is this animal from?(domestic, wild, etc)" << endl;
        cin >> envHabitat;

        // instantiation of Vertebrate object using variables from user entry.
        Vertebrate newAnimal(animal, backBone, mammal, isExtinct, envHabitat);
        cout << "Here's what you have told me about " << newAnimal.getAniMal() << "s" << endl;
        cout << animal << "s have backbones? " << newAnimal.getBackBone() << endl;
        cout << animal << "s are mammals? " << newAnimal.getIsMam() << endl;
        cout << "Are " << animal << "s extinct? " << newAnimal.getExtinct() << endl;
        cout << "What kind of habitat do they live in? " << newAnimal.getHabitat() << endl;
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

