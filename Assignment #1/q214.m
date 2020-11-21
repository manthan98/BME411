% Determine the optimal angle (theta) by performing unconstrained
% optimization from 0 to pi / 4 radians.
x = fminbnd(@f214, 0, pi / 4);

% Determine minimal area and perimeter.
f214(x)