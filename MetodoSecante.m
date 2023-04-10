function [x, fval, info] = MetodoSecante(f, x0, x1, tol, maxiter)
% Implementación del método de la secante para encontrar una raíz de f(x)

% Entradas:
% f: función a evaluar
% x0, x1: valores iniciales para el método
% tol: tolerancia para la convergencia
% maxiter: número máximo de iteraciones permitidas

% Salidas:
% x: aproximación de la raíz de f(x)
% fval: valor de f(x) en la aproximación de la raíz
% info: estructura que contiene información sobre la convergencia

% Inicialización
x = x1;
xprev = x0;
iter = 0;

% Iteraciones
while (abs(x - xprev) > tol) && (iter < maxiter)
    iter = iter + 1;
    fval = f(x);
    fvalprev = f(xprev);
    xnew = x - fval*(x - xprev)/(fval - fvalprev);
    xprev = x;
    x = xnew;
end

% Información de la convergencia
if iter >= maxiter
    info.converged = false;
    warning('El método no ha convergido en el número máximo de iteraciones permitidas');
else
    info.converged = true;
end
info.iterations = iter;

end