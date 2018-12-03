#include <iostream>
#include <string>

using namespace std;

class Vertebrate
{
// defining variables. private to ensure they are not touched unless called by the setter functions.
private:
    string skinCover, animalType;
    int appendages;


public:
    //constructor
    Vertebrate() {
        skinCover = getSkinCover();
        animalType = getAnimalType();
        appendages = getAppendages();
    };


    // setter functions
    void setIsReptile() {
        skinCover = "scales";
        animalType = "reptiles";
        setAppendages(4);
    };
    void setIsMammal() {
        skinCover = "fur/hair";
        animalType = "mammals";
        setAppendages(4);
    };
    void setIsFowl() {
        skinCover = "feathers";
        animalType = "birds";
        setAppendages(2);
    };
    void setIsAmphibious() {
        skinCover = "mucus";
        animalType = "amphibians";
        setAppendages(4);
    };
    void setAppendages(int legs) {
        appendages = legs;
    };


    // getter functions
    string getSkinCover() {
        return skinCover;
    };

    int getAppendages() {
        return appendages;
    };

    string getAnimalType() {
        return animalType;
    }
};

//
// Created by Ian Sabey on 11/29/18.
//
