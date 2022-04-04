#lang racket
(define-record-type :point

(make-point x y)

point?

(x point-x)

(y point-y))

(define (point-pretty-print p)

(display (format "X: ~a Y: ~a~n" (point-x p) (point-y p))))

(define (point=? p q)

(and (= (point-x p) (point-x q))

(= (point-y p) (point-y q))))

(define (square x) (* x x))

(define (distance a b)

(+ (square (- (point-x a) (point-x b)))

(square (- (point-y a) (point-y b)))))

(define (counter-clockwise p q r)

(- (* (- (point-x q) (point-x p))

(- (point-y r) (point-y p)))

(* (- (point-y q) (point-y p))

(- (point-x r) (point-x p)))))

(define (rightturn? p q r)

(let ((cross (counter-clockwise p q r)))

(if (zero? cross)

(< (distance q p) (distance r p))

(negative? cross))))

(define (leftmost? p q)

(or (< (point-y q) (point-y p))

(and (= (point-y q) (point-y p))

(< (point-x q) (point-x p)))))

(define (min-point points)

(define (min-point-iter p ps)

(if (null? ps)

p

(let ((q (car ps)))

(min-point-iter (if (leftmost? p q)

q

p)

(cdr ps)))))

(min-point-iter (car points) (cdr points)))

(define (wrap-step p points)

(define (wrap-step-iter q ps)

(if (null? ps)

q

(wrap-step-iter (if (rightturn? p q (car ps))

(car ps)

q)

(cdr ps))))

(wrap-step-iter p points))

(define (gift-wrapping points)

(let ((minp (min-point points)))

(define (gift-iterate p res)

(let ((q (wrap-step p points)))

(point-pretty-print q)

(if (point=? minp q)

(cons q res)

(gift-iterate q (cons q res)))))

(gift-iterate (car points) '())))

(define (test)

(define test-points

(list (make-point 1 1) (make-point 0 2) (make-point 1 4) (make-point 3 4)

(make-point 3 2) (make-point 1 3) (make-point 2 5)))

(point-pretty-print (min-point test-points))

(= (length (gift-wrapping test-points)) 6))

;; vim:ft=scheme


 

(define-record-type :point

(make-point x y)

point?

(x point-x)

(y point-y))

(define (point-pretty-print p)

(display (format "X: ~a Y: ~a~n" (point-x p) (point-y p))))

(define (point=? p q)

(and (= (point-x p) (point-x q))

(= (point-y p) (point-y q))))

(define (square x) (* x x))

(define (distance a b)

(+ (square (- (point-x a) (point-x b)))

(square (- (point-y a) (point-y b)))))

(define (counter-clockwise p q r)

(- (* (- (point-x q) (point-x p))

(- (point-y r) (point-y p)))

(* (- (point-y q) (point-y p))

(- (point-x r) (point-x p)))))

(define (rightturn? p q r)

(let ((cross (counter-clockwise p q r)))

(if (zero? cross)

(< (distance q p) (distance r p))

(negative? cross))))

(define (leftmost? p q)

(or (< (point-y q) (point-y p))

(and (= (point-y q) (point-y p))

(< (point-x q) (point-x p)))))

(define (min-point points)

(define (min-point-iter p ps)

(if (null? ps)

p

(let ((q (car ps)))

(min-point-iter (if (leftmost? p q)

q

p)

(cdr ps)))))

(min-point-iter (car points) (cdr points)))

(define (wrap-step p points)

(define (wrap-step-iter q ps)

(if (null? ps)

q

(wrap-step-iter (if (rightturn? p q (car ps))

(car ps)

q)

(cdr ps))))

(wrap-step-iter p points))

(define (gift-wrapping points)

(let ((minp (min-point points)))

(define (gift-iterate p res)

(let ((q (wrap-step p points)))

(point-pretty-print q)

(if (point=? minp q)

(cons q res)

(gift-iterate q (cons q res)))))

(gift-iterate (car points) '())))

(define (test)

(define test-points

(list (make-point 1 1) (make-point 0 2) (make-point 1 4) (make-point 3 4)

(make-point 3 2) (make-point 1 3) (make-point 2 5)))

(point-pretty-print (min-point test-points))

(= (length (gift-wrapping test-points)) 6))

;; vim:ft=scheme


 

(define-record-type :point

(make-point x y)

point?

(x point-x)

(y point-y))

(define (point-pretty-print p)

(display (format "X: ~a Y: ~a~n" (point-x p) (point-y p))))

(define (point=? p q)

(and (= (point-x p) (point-x q))

(= (point-y p) (point-y q))))

(define (square x) (* x x))

(define (distance a b)

(+ (square (- (point-x a) (point-x b)))

(square (- (point-y a) (point-y b)))))

(define (counter-clockwise p q r)

(- (* (- (point-x q) (point-x p))

(- (point-y r) (point-y p)))

(* (- (point-y q) (point-y p))

(- (point-x r) (point-x p)))))

(define (rightturn? p q r)

(let ((cross (counter-clockwise p q r)))

(if (zero? cross)

(< (distance q p) (distance r p))

(negative? cross))))

(define (leftmost? p q)

(or (< (point-y q) (point-y p))

(and (= (point-y q) (point-y p))

(< (point-x q) (point-x p)))))

(define (min-point points)

(define (min-point-iter p ps)

(if (null? ps)

p

(let ((q (car ps)))

(min-point-iter (if (leftmost? p q)

q

p)

(cdr ps)))))

(min-point-iter (car points) (cdr points)))

(define (wrap-step p points)

(define (wrap-step-iter q ps)

(if (null? ps)

q

(wrap-step-iter (if (rightturn? p q (car ps))

(car ps)

q)

(cdr ps))))

(wrap-step-iter p points))

(define (gift-wrapping points)

(let ((minp (min-point points)))

(define (gift-iterate p res)

(let ((q (wrap-step p points)))

(point-pretty-print q)

(if (point=? minp q)

(cons q res)

(gift-iterate q (cons q res)))))

(gift-iterate (car points) '())))

(define (test)

(define test-points

(list (make-point 1 1) (make-point 0 2) (make-point 1 4) (make-point 3 4)

(make-point 3 2) (make-point 1 3) (make-point 2 5)))

(point-pretty-print (min-point test-points))

(= (length (gift-wrapping test-points)) 6))