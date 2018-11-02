// Unit 2 Submission 2
// String Play Program
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>

using namespace std;

string str1, str2, str3;
int opChoice;
bool again;

class Strings {
public:
    void repeat() {
        cout << "Would you like to perform another operation (y or n)? ";
        char againResp;
        cin >> againResp;
        if (againResp == 'y')
            again = true;
        else
            again = false;
    }

    void compare(string str1, string str2)
    {
        cout << "Great! Comparing..." << endl;
        if (str1 != str2)
            cout << str1 << " is not " << str2 << endl;
        repeat();
    }

    void concat(string str1, string str2)
    {
        cout << "Concatenation in progress..." << endl;
        string resultSet = str1 + str2;
        cout << "Result string:\n" << resultSet << endl;
        repeat();
    }

    void length(string str3)
    {
        cout << "Enter the string to check. >> " << endl;
        cin >> str3;
        cout << "Checking length..." << endl;
        cout << str3.length() << endl;
    }

    void execOp(int opChoice) {
        cout << "Enter the first string. >> ";
        cin >> str1;
        cout << "Enter the second string. >> ";
        cin >> str2;
        switch(opChoice) {
            case 1:
                return compare(str1, str2);
            case 2:
                return concat(str1, str2);
            case 3:
                return length(str3);
            default:
                cout << "Invalid option entered..";
        }
    }

    void operation()
    {
        cout << "Which string operation would you like to run?\n"
             << "Options are: (1)compare, (2)concat, (3)length, (4)reverse.";
        int response;
        cin >> response;

        switch(response) {
            case 1 :
                opChoice = 1;
                return execOp(opChoice);
            case 2 :
                opChoice = 2;
                return execOp(opChoice);
            case 3 :
                opChoice = 3;
                return execOp(opChoice);
            case 4 :
                opChoice = 4;
                return execOp(opChoice);
            default:
                cout << "Please choose an option from above.\n";
                operation();
        }
    }

    // header 'main'
    void stringMain() {
        do {
            operation();
        } while (again);
    }
};

//
// Created by Ian Sabey on 11/2/18.
//
