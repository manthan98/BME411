function f = f214(x)
% Computes the output to both objective functions for Q2.14 in Optimization
% textbook by Belegundu et al.

A = 15 * cos(x);
B = 15 * sin(x);

x_min = min(-5, A - 10);
y_min = min(-5, B - 10);
x_max = max(5, A + 10);
y_max = max(5, B + 10);

AA = x_max - x_min;
BB = y_max - y_min;

f1 = AA * BB; % Area
f2 = 2 * (AA + BB); % Perimeter

% Modify based on perimeter or area output as desired - default output
% is area.
f = f1;

end