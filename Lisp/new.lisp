(defun my-length (list)
  (if list
	(+ (car list) (my-length (cdr list)))
	0))

(defun add (x y) (+ x y))
