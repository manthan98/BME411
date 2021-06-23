syms x1 x2 x3 lambda

L = 9 - 8*x1 - 6*x2 - 4*x3 + 2*(x1)^2 + 2*(x2)^2 + x3^2 + 2*x1*x2 + 2*x1*x3 + lambda*(x1 + x2 + 2*x3 - 3);
f = 9 - 8*x1 - 6*x2 - 4*x3 + 2*(x1)^2 + 2*(x2)^2 + x3^2 + 2*x1*x2 + 2*x1*x3;

f_x1 = diff(L, x1) == 0;
f_x2 = diff(L, x2) == 0;
f_x3 = diff(L, x3) == 0;
f_x4 = diff(L, lambda) == 0;

[A, B] = equationsToMatrix([f_x1, f_x2, f_x3, f_x4], [x1, x2, x3, lambda]);
X = linsolve(A, B);

x1 = X(1);
x2 = X(2);
x3 = X(3);
subs(f);

