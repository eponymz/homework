// Unit 1 Submission Node 1
// Calculator Application
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>
using namespace std;

bool again;
int opDecision;
int result;
int num1;
int num2;

class Calculator {
public:
    void execute(int opDecision)
    {
        cout << "Please enter the first number. >> ";
        cin >> num1;
        cout << "Please enter the second number. >> ";
        cin >> num2;
        switch(opDecision) {
            case 1 :
                result = {num1 + num2};
                cout << "Great! The sum of " << num1 << " and " << num2 << " is " << result << endl;
                break;
            case 2 :
                result = {num1 - num2};
                cout << "Great! The difference of " << num1 << " and " << num2 << " is " << result << endl;
                break;
            case 3 :
                result = {num1 * num2};
                cout << "Great! The product of " << num1 << " and " << num2 << " is " << result << endl;
                break;
            case 4 :
                result = {num1 / num2};
                cout << "Great! The quotient of " << num1 << " and " << num2 << " is " << result << endl;
                break;
            default:
                cout << "Invalid option entered.";
        }
        cout << "Would you like to perform another operation (y or n)? ";
        char againResp;
        cin >> againResp;
        if (againResp == 'y')
            again = true;
        else
            again = false;
    }

    void operation()
    {
        cout << "What operation would you like to perform?\n"
             << "Options are: a for add, s for subtract, m for multiply, d for divide >> ";
        char response;
        cin >> response;

        switch(response) {
            case 'a' :
                opDecision = 1;
                return execute(opDecision);
            case 's' :
                opDecision = 2;
                return execute(opDecision);
            case 'm' :
                opDecision = 3;
                return execute(opDecision);
            case 'd' :
                opDecision = 4;
                return execute(opDecision);
            default:
                cout << "Please choose one of the options above.\n";
                operation();
        }
    }

    // main function for execution
    void calcMain() {
        do {
            operation();
        } while (again);
    }

};
//
// Created by Ian Sabey on 10/16/2018.
//