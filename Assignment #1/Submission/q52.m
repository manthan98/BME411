function [ f, a0, a1, a2, x_star, h_x_star, f_x_star, conv_test ] = q52( x )
% This function automates the quadratic interpolation method calculations for
% Q5.2 from the Engineering Optimization - S.S. Rao textbook.

f = [0, 0, 0];
for i = 1:size(x, 2)
    f(i) = 0.65 - (0.75 / (1 + x(i)^2)) - 0.65*x(i)*atan(1 / x(i));
end

[a0, a1, a2] = asolver(f(1), f(2), f(3), x(1), x(2), x(3));
x_star = (-1 * a1) / (2 * a2);

h_x_star = a0 + a1*x_star + a2*x_star^2;
f_x_star = 0.65 - (0.75 / (1 + x_star^2)) - 0.65*x_star*atan(1 / x_star);

conv_test = abs( (h_x_star - f_x_star) / f_x_star );

end

