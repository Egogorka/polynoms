#include <iostream>

#include "src/Polynom.h"
#include <complex>

#include "src/durand_kerner.h"
#include "src/approximation.h"

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
    std::cout << "Input polynomial with form:" << '\n' << "a_0 + a_1 x^1 + a_2 x^3 + ..." << '\n';
    std::cout << poly1 << std::endl << '\n';

    std::cout << "Polynomial at 1+1i : " << '\n';
    std::cout << poly1(1.0f + 1if) << std::endl << '\n';

    std::vector<c_t> roots = {c_t(0.5,1),c_t(0.5, -1),c_t(-0.5,0.1),c_t(-0.5,-0.1)};
    std::cout << "Durand-Kerner algo with random starting points (60 iterations) : " << std::endl;
    std::cout << "Points in :" << roots << std::endl;
    durand_kerner(poly1, roots, 60);
    std::cout << "Points out :" << roots << std::endl << '\n';

    auto roots2 = get_approximate_roots(poly1, std::make_pair(c_t(-1,-1),c_t(1,1)), 100);
    std::cout << "Approximation algo via min|p(x)| : " << '\n' << roots2 << std::endl;

    return 0;

    // TODO:
    // + Понять, что такое map. Впихнуть его в get_approximate_roots, получить результат и узнать вообще, стоит ли этот метод, или нужно его улучшать
    // +     Сделать пару тестов (вручную) для get_approximate_roots
    // Поработать с durand_kerner() функцией. Вроде она работает, но надо бы проверить, как хорошо.
        /// Сложно точно это сказать для любых начальных точек
        // Отобразить действие алгоритма в python
    // Реализовать частичную сумму ряда Тейлора экспоненты (чсрТэ).
        // Отобразить нули частичной суммы с помощью durand_kerner()
    // Реализовать у полинома функцию масштабирования
        // Сварганить монстра из чсрТэ и масштабирования, durand_kerner кстати хорошо с ним работает ибо нули не должны далеко уходить от предыдущей итерации.
}
