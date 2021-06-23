syms x
f = 10*x^6 - 48*x^5 + 15*x^4 + 200*x^3 - 120*x^2 - 480*x + 100;

% Find first and second derivatives
diff(f)
diff(diff(f))

% Roots of first derivative
p = [60 -240 60 600 -240 -480];
roots(p)

