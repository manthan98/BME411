function [ a0, a1, a2 ] = asolver( f1, f2, f3, x1, x2, x3 )
% This function computes the a-values in the quadratic interpolation
% method.

a0 = ( (f1*x2*x3*(x3-x2)) + (f2*x3*x1*(x1-x3)) + (f3*x1*x2*(x2-x1)) ) / ( (x1-x2)*(x2-x3)*(x3-x1) );
a1 = ( (f1*(x2^2-x3^2)) + (f2*(x3^2-x1^2)) + (f3*(x1^2-x2^2)) ) / ( (x1-x2)*(x2-x3)*(x3-x1) );
a2 = -1 * ( ( (f1*(x2-x3)) + (f2*(x3-x1)) + (f3*(x1-x2)) ) / ( (x1-x2)*(x2-x3)*(x3-x1) ) );

end

