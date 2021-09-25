//
// Created by Meevere on 24.09.2021.
//

#include "durand_kerner.h"

void durand_kerner(const Polynomial<c_t>& poly, std::vector<c_t>& roots){
    //std::vector<c_t> roots_new(roots);

    for(unsigned i=0; i<roots.size(); ++i){
        c_t denominator(1,0);
        for(unsigned j=0; j<roots.size(); ++j){
            if(i==j) continue;
            denominator *= (roots[i] - roots[j]);
        }
        roots[i] = roots[i] - poly(roots[i])/denominator;
    }
}

void durand_kerner(const Polynomial<c_t>& poly, std::vector<c_t>& roots, unsigned times){
    //std::vector<c_t> roots_new(roots);
    for(;times>0;--times){
        durand_kerner(poly, roots);
    }
}