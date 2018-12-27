# include<iostream>
using namespace std;

class Vehicle
{
public:
    string engineSize, color, doors;
    Vehicle() {

    }
    string setDoors(string doorOptions) {
        return doors = doorOptions;
    }
    string setEngineSize(string engineOptions) {
        return engineSize = engineOptions;
    }
    string setColor(string colorOptions) {
        return color = colorOptions;
    }
    void display(string vehicleType, string extraFeatures) {
        cout << "Here are the " << vehicleType << " options at the dealership currently." << endl;
        cout << "Engine options are:\n" << engineSize << endl;
        cout << "Door options are:\n" << doors << endl;
        cout << "Color options are:\n" << color << endl;
        cout << "Extra features of " << vehicleType << "s:\n" << extraFeatures << endl;
    }
};

// coupe, and convertible

class Sedan: public Vehicle
{
public:
    Sedan() {
        string extraFeatures = "excellent fuel economy, midsized (easy to handle)";
        setColor("blue, red, black, silver, white");
        setEngineSize("inline 4cyl\nv6");
        setDoors("4");
        display("sedan", extraFeatures);
    }
};
class Minivan: public Vehicle
{
public:
    Minivan() {
        string extraFeatures = "excellent fuel economy, perfect for the family";
        setColor("blue, gold, forrest green, silver, white");
        setEngineSize("inline 4cyl\nv6");
        setDoors("5 (4 + hatch)");
        display("minivan", extraFeatures);
    }
};
class Crossover: public Vehicle
{
public:
    Crossover() {
        string extraFeatures = "good for camping trips (extra room in hatch)";
        setColor("sea blue, red, black, silver");
        setEngineSize("inline 4cyl\nv6");
        setDoors("5 (4 + hatch)");
        display("crossover", extraFeatures);
    }
};
class Coupe: public Vehicle
{
public:
    Coupe() {
        string extraFeatures = "sleek body trim, fits 2 comfortably";
        setColor("yellow, red, black, white");
        setEngineSize("inline 4cyl\nv6");
        setDoors("2");
        display("coupe", extraFeatures);
    }
};
class Convertible: public Vehicle
{
public:
    Convertible() {
        string extraFeatures = "'convertible' great for tall people, decent fuel economy";
        setColor("blue, red, black, silver, white, gold, yellow");
        setEngineSize("inline 4cyl\nv6, v8");
        setDoors("2, 4");
        display("convertible", extraFeatures);
    }
};
