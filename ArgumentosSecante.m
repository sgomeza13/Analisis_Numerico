% Definición de la función f(x)
f = @(x) (abs(x))^(x - 1) - 2.5 * x - 5;

% Llamada a la función secante
[x, fval, info] = MetodoSecante(f, -3, -2, 0.5e-6, 100);

% Impresión de los resultados
disp(['Aproximación de la raíz: ', num2str(x)]);
disp(['Valor de f en la aproximación de la raíz: ', num2str(fval)]);
if info.converged
    disp(['Número de iteraciones necesarias para converger: ', num2str(info.iterations)]);
else
    disp('El método no ha convergido en el número máximo de iteraciones permitidas');
end