#include <iostream>

#include "src/Polynom.h"
#include <complex>

#include "src/durand_kerner.h"

using std::complex;
using namespace std::complex_literals;

std::ostream& operator<<(std::ostream& os, std::vector<c_t>& vec){
    for(auto& elem: vec){
        os << elem << ' ';
    }
    return os;
}

int main() {

    //Polynomial<int>::default_value = 0;

    Polynomial<complex<float>> poly1 {1,0,0,0,1};
    std::cout << poly1 << std::endl;
    std::cout << poly1(1.0f + 1if) << std::endl;

    std::vector<c_t> roots = {c_t(0.5,1),c_t(0.5, -1),c_t(-0.5,0.1),c_t(-0.5,-0.1)};
    std::cout << roots << std::endl;
    durand_kerner(poly1, roots, 60);
    std::cout << roots << std::endl;



    return 0;
}
