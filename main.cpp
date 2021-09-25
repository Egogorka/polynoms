#include <iostream>

#include "src/Polynom.h"
#include <complex>

using std::complex;
using namespace std::complex_literals;

int main() {

    //Polynomial<int>::default_value = 0;

    Polynomial<complex<float>> poly1 {1,2,3};
    std::cout << poly1 << std::endl;
    std::cout << poly1(1.0f + 1if) << std::endl;

    Polynomial<complex<float>> poly2 {3,2,1};
    std::cout << poly2 << std::endl;
    std::cout << poly2(1) << std::endl;

    auto poly = poly1 - poly2;
    std::cout << poly << std::endl;
    std::cout << poly(1) << std::endl;

    Polynomial<complex<float>> poly3 {1,1};
    Polynomial<complex<float>> poly4 {-1,1};

    std::cout << poly3 * poly4 << std::endl;

    return 0;
}
