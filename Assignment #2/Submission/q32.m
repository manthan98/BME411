%% Part A
syms x1 x2

f = (x1 + x2) / (3 + x1^2 + x2^2 + x1*x2);
f_grad = gradient(f, [x1, x2]); % gradient of f
f1 = f_grad(1,1);
f2 = f_grad(2,1);

[x_0, y_0] = solve(f1, x1, x2);
[x_1, y_1] = solve(f2, x1, x2);

% Stationary point(s)
x1 = intersect(x_0, x_1);
x2 = intersect(y_0, y_1);
subs(f);

%% Part B
syms x1 x2
h = hessian(f, [x1, x2]);

x1 = intersect(x_0, x_1);
x2 = intersect(y_0, y_1);

x1 = -1;
x2 = -1;

eig(subs(h));

x1 = 1;
x2 = 1;

eig(subs(h));