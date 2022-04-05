#lang scheme
(require rnrs/mutable-pairs-6)

(define (cons x y)
  (let ((new (get-new-pair)))
(set-car! new x)
(set-cdr! new y)
new))

(cons 3 5)