syms c v

u = ((21.9*10^7) / ((v^2)*c)) + (3.9*10^6)*c + 1000*v;
h = hessian(u, [c, v]);

% Choose c > 0 and v != 0, and check all eigenvalues > 0 for positive
% definiteness
c = 0.1;
v = 0.1;
all(eig(subs(h)) > 0)