// main file to determine which submission node to run
#include "Calculator.h"
#include "Fibonacci.h"
#include <string>

using namespace std;

int main() {
    cout << "Welcome to Unit 1. Which file would you like to run? (calc or fibSeries)? ";
    string fileChoice;
    cin >> fileChoice;
    if (fileChoice == "calc") {
        Calculator calculator;
        calculator.calcMain();
        main();
    }
    else if (fileChoice == "fibSeries") {
        FibSeries fibSeries;
        fibSeries.fibSeries();
        main();
    }
}

//
// Created by Ian Sabey on 10/17/18.
//

