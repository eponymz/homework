// fibonacci generator

#include <iostream>

using namespace std;

class FibSeries {
public:
    void fibSeries() {
        int length, count, first{0}, second{1}, next;

        cout << "How many iterations would you like? " << endl;
        cin >> length;

        cout << "The first " << length << " iterations of the Fibonacci series are: " << endl;

        for (count = 0; count < length; count++) {
            if (count <= 1)
                next = count;
            else {
                next = first + second;
                first = second;
                second = next;
            }
            cout << next << endl;
        }
    }
};

//
// Created by Ian Sabey on 10/17/18.
//