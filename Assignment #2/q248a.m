%% Part A
syms x2 x3

x1 = (-1*x2) - (2*x3) + 3;
f = 9 - 8*x1 - 6*x2 - 4*x3 + 2*(x1)^2 + 2*(x2)^2 + x3^2 + 2*x1*x2 + 2*x1*x3;
f_expanded = expand(f);

f_gradient = gradient(f, [x2, x3]);
f_x2 = f_gradient(1, 1) == 0;
f_x3 = f_gradient(2, 1) == 0;

[A, B] = equationsToMatrix([f_x2, f_x3], [x2, x3]);
X = linsolve(A, B);

%% Part B
syms x1 x2 x3
f = 9 - 8*x1 - 6*x2 - 4*x3 + 2*(x1^2) + 2*(x2^2) + x3^2 + 2*x1*x2 + 2*x1*x3;
h = hessian(f, [x1, x2, x3]);

x1 = 4/3;
x2 = 4/9;
x3 = 7/9;
d = real(eig(h));
isposdef = isAlways(d > 0);