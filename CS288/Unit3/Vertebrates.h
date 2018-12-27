#include <iostream>
#include <string>

using namespace std;

class Vertebrate
{
public:
    string skinCover, animalType, appendages;
    //constructor
    Vertebrate()
    {
        skinCover = getSkinCover();
        animalType = getAnimalType();
        appendages = getAppendages();
    };
    void setAppendages(int legs) {
        int appendages = legs;
    };
    string getSkinCover() {
        return skinCover;
    };
    string getAppendages() {
        return appendages;
    };
    string getAnimalType() {
        return animalType;
    };
};

//class Habitat
//{
//public:
//    string livingEnv;
//    Habitat()
//    {
//        livingEnv = getLivingEnv();
//    }
//
//    string getLivingEnv() {
//        return livingEnv;
//    }
//};
//
//// if i included the above, each derived class below would be restructured to the following
//class Bird: public Vertebrate, public Habitat {
//public:
//    Bird(string birdType) {
//        skinCover = "feathers";
//        animalType = "birds";
//        livingEnv = "nests, generally in trees";
//        setAppendages(2);
//        cout << birdType << "s are " << animalType << endl;
//        cout << birdType << "s have " << skinCover << endl;
//        cout << birdType << "s have " << appendages << " legs" << endl;
//        cout << birdType << "s (for the most part) live in " << livingEnv << endl;
//    }
//};

class Bird: public Vertebrate {
public:
    Bird(string birdType) {
        skinCover = "feathers";
        animalType = "birds";
        setAppendages(2);
        cout << birdType << "s are " << animalType << endl;
        cout << birdType << "s have " << skinCover << endl;
        cout << birdType << "s have " << appendages << " legs" << endl;
    }
};

class Amphibian: public Vertebrate {
public:
    Amphibian(string amphType) {
        skinCover = "mucus";
        animalType = "amphibians";
        setAppendages(4);
        cout << amphType << "s are " << animalType << endl;
        cout << amphType << "s have " << skinCover << endl;
        cout << amphType << "s have " << appendages << " legs" << endl;
    }
};

class Mammal: public Vertebrate {
public:
    Mammal(string mammType) {
        skinCover = "fur/hair";
        animalType = "mammals";
        setAppendages(4);
        cout << mammType << "s are " << animalType << endl;
        cout << mammType << "s have " << skinCover << endl;
        cout << mammType << "s have " << appendages << " legs" << endl;
    }
};

class Reptile: public Vertebrate {
public:
    Reptile(string repType) {
        skinCover = "scales";
        animalType = "reptiles";
        setAppendages(4);
        cout << repType << "s are " << animalType << endl;
        cout << repType << "s have " << skinCover << endl;
        cout << repType << "s have " << appendages << " legs" << endl;
    }
};

//
// Created by Ian Sabey on 12/24/18.
//
