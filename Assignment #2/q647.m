syms x1 x2 x3

f = (2*x1 - x2 + x3 + 1)^2 + (x1 + 2*x2)^2 + (3*x1 + x2 + 2*x3 - 3)^2;
f_grad = gradient(f, [x1, x2, x3]); % gradient of f
f_hess = hessian(f, [x1, x2, x3]); % hessian of f

x1 = 0;
x2 = 0;
x3 = 0;
x_1 = [x1 x2 x3]';

f_grad_x1 = subs(f_grad); % f(X1)
inv_hess = double(inv(f_hess)); % inverse hessian of f

x_2 = x_1 - inv_hess*f_grad_x1; % X2

x1 = -2;
x2 = 1;
x3 = 4;
subs(f); % f(X2)