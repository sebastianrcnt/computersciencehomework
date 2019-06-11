A = [1,2;3,4]
e = eig(A)
e1 = e(1);
e2 = e(2);
if not(isreal(e1)) && not(isreal(e2))
    if real(e1) > 0 && real(e2) > 0
        fprintf('Unstable, Spiral Point')
    elseif real(e1) < 0 && real(e2) < 0
        fprintf('Asymptotically Stable, Spiral Point')
    elseif real(e1) == 0 && real(e2) == 0
        fprintf('If linear system, Stable, Center')
        fprintf('If locally linear system, Indeterminate, Spiral Point or Center')
    else
        fprintf('Error.')
    end
elseif isreal(e1) && isreal(e2)
    if e1 == e2
        if e1 > 0 && e2 > 0
            fprintf('If linear system, Unstable, Proper Node or Improper Node')
            fprintf('If locally linear system, Unstable, Spiral Point or Node')
        elseif e1 < 0 && e2 < 0
            fprintf('If linear system, Asymptotically stable, Proper Node or Improper Node')
            fprintf('If locally linear system, Asymptotically stable, Spiral Point or Node')
        else
            fprintf('Error.')
        end
    elseif not(e1 == e2)
        if e1 * e2 > 0
            if e1 > 0 && e2 > 0
                fprintf('Unstable, Node')
            elseif e1 < 0 && e2 < 0
                fprintf('Asymptotically Stable, Node')
            else
                fprintf('Error')
            end
        elseif e1 * e2 < 0
            fprintf('Unstable, Saddle Point')
        else
            fprintf('Error.')
        end
    end
end
