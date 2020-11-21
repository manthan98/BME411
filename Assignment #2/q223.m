table = [0 380; 0.25 200; 0.50 100; 0.75 20; 1.00 0];

syms a b
y = (a + b*table(1,1) - table(1,2))^2 + (a + b*table(2,1) - table(2,2))^2 + (a + b*table(3,1) - table(3,2))^2 + (a + b*table(4,1) - table(4,2))^2 + (a + b*table(5,1) - table(5,2))^2;

y_expanded = expand(y);
f_a = diff(y, a) == 0;
f_b = diff(y, b) == 0;

% Computes a and b based on system of equations from gradient.
[A, B] = equationsToMatrix([f_a, f_b], [a, b]);
X = linsolve(A, B);