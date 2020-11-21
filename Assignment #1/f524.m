function [ f_out, f1, f2, x_2 ] = f524( x )
% Automates function and next step calculations for Q5.24 from 
% the Engineering Optimization - S.S. Rao textbook.

f_out = 25600*x^4 - 25600*x^3 + 6416*x^2 - 16*x + 4;
f1 = 102400*x^3 - 76800*x^2 + 12832*x - 16;
f2 = 307200*x^2 - 153600*x + 12832;
x_2 = x - (f1 / f2);

end

