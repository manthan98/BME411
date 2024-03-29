syms x1 x2

f = 100*((x2 - x1^2)^2) + (1 - x1)^2;
f_grad = gradient(f, [x1, x2]);

x1 = -1.2;
x2 = 1.0;
subs(f_grad); % gradient f(X0)

syms a0
fa = 100*(( (1 + 88*a0) - ((-1.2 + 215.6*a0)^2) )^2) + ((1 - (-1.2 + 215.6*a0))^2);
fa_1 = diff(fa) == 0; % f'(alpha_0)
alpha_0 = vpasolve(fa_1, a0); % alpha_0

a0 = alpha_0(3);
double(subs(fa));

x1 = 1.43032;
x2 = 2.0736;
double(subs(f)); % f(X1)
double(subs(f_grad)); % gradient f(X1)

syms a1
fa2 = 100*(((2.0736 - 5.5569*a1) - (1.43032 + 15.0358*a1)^2)^2) + (1 - (1.43032 + 15.0358*a1))^2;
fa2_1 = diff(fa2) == 0; % f'(alpha_1)
alpha_1 = vpasolve(fa2_1, a1); % alpha_1

fa2_2 = diff(diff(fa2));
a1 = alpha_1(3);
subs(fa2_2);

x1 = 1.438;
x2 = 2.07;
double(subs(f)); % f(X2)