%% Part A
syms y z

x = 16 / (y*z);
f = (6 * x * y * z) / (x + 2*y + 2*z);
f_simp = simplifyFraction(f);

f_gradient = gradient(f, [y, z]);
simplifyFraction(f_gradient(1, 1), 'Expand', true);
simplifyFraction(f_gradient(2, 1), 'Expand', true);

%%  Part B
% syms x y z
% f = (6 * x * y * z) / (x + 2*y + 2*z);
% h = hessian(f, [x, y, z]);
% 
% x = 4;
% y = 2;
% z = 2;
% eig(subs(h))

h = hessian(f, [y, z]);
y = 2;
z = 2;
subs(h);
eig(subs(h))