//
// Created by Meevere on 24.09.2021.
//

#ifndef POLYNOMS_DURAND_KERNER_H
#define POLYNOMS_DURAND_KERNER_H

#include <vector>
#include "Polynom.h"
#include <complex>
#include <utility>

using std::complex;
typedef complex<float> c_t;

void durand_kerner(const Polynomial<c_t>& poly, std::vector<c_t>& roots);
void durand_kerner(const Polynomial<c_t>& poly, std::vector<c_t>& roots, unsigned times);

#endif //POLYNOMS_DURAND_KERNER_H
