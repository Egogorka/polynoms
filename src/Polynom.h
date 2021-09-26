//
// Created by Meevere on 23.09.2021.
//

#ifndef POLYNOMS_POLYNOM_H
#define POLYNOMS_POLYNOM_H

#include <vector>
#include <iostream>
#include <complex>

typedef std::complex<float> c_t;

template <typename T>

// Typename T must support
// addition, subtraction, multiplication
class Polynomial {
protected:
    // from 0-th power of x to n-th
    // a_0 + a_1 x^1 + ... + a_n x^n where
    // a_k = coefficients[k];
    std::vector<T> coef;
public:

    // There is no default value for arbitrary type T, so no default constructor
    // UPDATE: Now we heavily rely on default constructor of T and use it as a "default value", thus can have a default constructor
    Polynomial(): coef(1, T()) {};

    Polynomial(T value, unsigned index): coef(index+1, T()) {
        coef[index] = value;
    }

    explicit Polynomial(std::vector<T>& coef): coef(coef, T()) {};
    explicit Polynomial(unsigned size): coef(size, T()) {};

    // This constructor is made so this sugar will work:
    // Polynomial poly{1,2,3};
    Polynomial(std::initializer_list<T> list): coef(list.size()) {
        int i=0;
        for( auto elem : list ){
            coef[i] = elem;
            i++;
        }
    };

    unsigned degree() const{
        return coef.size() - 1;
    }

    T operator[](unsigned index) const {
        if( index < coef.size() ) return coef[index];
        return T();
    }

    T& operator[](unsigned index) {
        if( index >= coef.size() ) coef.resize(index+1, T());
        return coef[index];
    }

    friend std::ostream& operator<<( std::ostream& os, const Polynomial& poly ){
        for( auto const& a : poly.coef ){
            os << a << ' ';
        }
        return os;
    }

    // Evaluate polynomial at some value "input"
    T operator()(T input) const{
        typename std::vector<T>::const_reverse_iterator it = coef.rbegin();
        T output = *it;
        ++it;
        while( it != coef.rend() ){
            output = *it + input*output;
            ++it;
        }
        return output;
    }

    Polynomial& operator+=(const Polynomial& other){
        auto maxsize = std::max(coef.size(), other.coef.size());
        coef.resize(maxsize, T());

        for(unsigned i=0; i<maxsize; ++i){
            coef[i] += other[i];
        }
        return *this;
    }

    Polynomial& operator-=(const Polynomial& other){
        auto maxsize = std::max(coef.size(), other.coef.size());
        coef.resize(maxsize, T());

        for(unsigned i=0; i<maxsize; ++i){
            coef[i] -= other[i];
        }
        return *this;
    }

    Polynomial& operator*=(const Polynomial& other){
        return *this = *this * other;
    }

    Polynomial& operator=(const Polynomial& other){
        unsigned maxsize = std::max(coef.size(), other.coef.size());
        coef.resize(maxsize, T());

        for(unsigned i=0; i<maxsize; ++i){
            coef[i] = other[i];
        }
        return *this;
    }

    friend Polynomial operator+(const Polynomial& poly1, const Polynomial& poly2){
        unsigned maxsize = std::max(poly1.coef.size(), poly2.coef.size());
        Polynomial poly(maxsize);
        for(unsigned i=0; i<maxsize; ++i){
            poly.coef[i] = poly1[i] + poly2[i];
        }
        return poly;
    }

    friend Polynomial operator-(const Polynomial& poly1, const Polynomial& poly2){
        unsigned maxsize = std::max(poly1.coef.size(), poly2.coef.size());
        Polynomial poly(maxsize);
        for(unsigned i=0; i<maxsize; ++i){
            poly.coef[i] = poly1[i] - poly2[i];
        }
        return poly;
    }

    friend Polynomial operator*(const Polynomial& poly1, const Polynomial& poly2){
        unsigned size = poly1.coef.size()+poly2.coef.size()-1;
        Polynomial poly(size);

        for(unsigned k=0; k<size; ++k){
            auto temp = T();
            for(int i=0; i<=k; ++i){
                if((k - i >=0) && (i < poly1.coef.size()))
                    temp += poly1[i]*poly2[k-i];
            }
            poly[k] = temp;
        }
        return poly;
    }

};


#endif //POLYNOMS_POLYNOM_H
