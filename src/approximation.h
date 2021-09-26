//
// Created by Meevere on 24.09.2021.
//

#ifndef POLYNOMS_APPROXIMATION_H
#define POLYNOMS_APPROXIMATION_H

#include <vector>
#include "Polynom.h"
#include <complex>
#include <utility>

using std::complex;

std::vector<c_t> get_approximate_roots(const Polynomial<c_t>& poly, std::pair<c_t,c_t> box, unsigned density);

#endif //POLYNOMS_APPROXIMATION_H
