//
// Created by Meevere on 24.09.2021.
//

#include "approximation.h"
#include <algorithm>

std::vector<c_t> get_approximate_roots(const Polynomial<c_t>& poly, std::pair<c_t,c_t> box, const unsigned density){
    // Here we assume, that no roots are multiple
    std::vector<float> dots(density*density, 0);

    c_t dr = box.second - box.first;

    for(unsigned i=0; i<density; ++i){
        for(unsigned j=0; j<density; ++j){
            c_t dot = box.first + c_t(dr.real()*i/density,dr.imag()*j/density);
            dots[i*density+j] = norm(poly(dot));
        }
    }

    std::sort(dots.begin(), dots.end());

    std::vector<c_t> out(poly.degree());
    for(unsigned i=0; i<=poly.degree(); ++i){
        out[i] = dots[i];
    }
    return out;
}