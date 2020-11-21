syms x

f = 25600*x^4 - 25600*x^3 + 6416*x^2 - 16*x + 4;

% Compute first and second derivatives of f.
diff(f);
diff(diff(f));