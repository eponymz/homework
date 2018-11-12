// Unit 2 Submission 1
// Definition
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>
using namespace std;

class Vertebrate {
private:
    // object attributes (private so as not to tamper with accidentally outside of class)
    string hasBackbone, isMam, extinct;
    string aniMal, habitat;

public:
    // constructor
    Vertebrate(string animalInput, string backBone, string mammal, string isExtinct, string envHabitat)
    {
        aniMal = animalInput;
        hasBackbone = backBone;
        isMam = mammal;
        extinct = isExtinct;
        habitat = envHabitat;
    }

    // functions to return entry.
    // can be used for handling anything (such as passing values to any other methods or classes.
    string getAniMal()
    {
        return aniMal;
    }

    string getBackBone()
    {
        return hasBackbone;
    }

    string getIsMam()
    {
        return isMam;
    }

    string getExtinct()
    {
        return extinct;
    }

    string getHabitat()
    {
        return habitat;
    }
};

//
// Created by Ian Sabey on 11/2/18.
//