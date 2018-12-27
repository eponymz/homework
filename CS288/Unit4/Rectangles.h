# include<iostream>
using namespace std;

class Rectangle {
private:
    double length;
    double width;
public:
    double getArea() {
        return length * width;
    }
    void setLength(double len) {
        length = len;
    }
    void setWidth(double wid) {
        width = wid;
    }

    Rectangle operator+(const Rectangle& b) {
        Rectangle rectangle{};
        rectangle.length = this->length + b.length;
        rectangle.width = this->width + b.width;
        return rectangle;
    }
};

void RectangleMain() {
    Rectangle Rectangle1{};
    Rectangle Rectangle2{};
    // this will be the result of adding the 2
    Rectangle Rectangle3{};
    double area;

    // build rectangle 1 and get/display area
    Rectangle1.setLength(5.0);
    Rectangle1.setWidth(9.0);
    area = Rectangle1.getArea();
    cout << "Area of Rectangle 1:\n" << area << endl;

    // build rectangle 1 and get/display area
    Rectangle2.setLength(20.3);
    Rectangle2.setWidth(3.5);
    area = Rectangle2.getArea();
    cout << "Area of Rectangle 2:\n" << area << endl;

    // add the 2 together
    Rectangle3 = Rectangle1 + Rectangle2;
    area = Rectangle3.getArea();
    cout << "Area of Rectangle 3:\n" << area << endl;
}

//
// Created by Ian Sabey on 12/26/2018.
//
