
#lang racket

;;Name: MUGOYA DIHFAHSIH
;;Student No. 2100702353

;Part 1: Scheme Vectors
;qtn 1
(define colors
  (vector "red" "orange" "yellow" "green" "blue" "indigo" "violet"))

(define (length-of-vector-elements vct)
  (vector-map string-length vct))

(length-of-vector-elements colors)

;Qtn 2
(define (zero-vector len)
  (make-vector len 0))

(define (append-zeros vec max-len)
  (vector-append vec (zero-vector (- max-len (vector-length vec)))))

(define (sum-vector v1 v2)
  (let ((max-len (max (vector-length v1)
                      (vector-length v2))))
    (vector-map +
                (append-zeros v1 max-len)
                (append-zeros v2 max-len))))

(sum-vector (vector 4 6 8 3) (vector 5 6 7))



;Qtn 3a
(vector-map (lambda (x) (* x x)) (vector 1 2 3 4))

;qtn 3b
(define (vector-for-each proc vec)
(for ([color vec])
  (display (string-append "\"" color "\"")) 
  )(newline))

(vector-for-each display (vector "red" "orange"))
 

;;Part 2: Variadic Functions
;;No.1
(define (insert-between v xs)
  (cond ((null? xs) xs)
        ((null? (cdr xs)) xs)
        (else (cons (car xs)
                    (cons v (insert-between v (cdr xs)))))))

(define (display-all . vs)
  (for-each display (insert-between " " vs))(newline))
(display-all "foo")
(display-all "foo" "bar")

;;No.2
(define (sum-list lst)
(cond ((null? lst) 0)   ;; checking if the list is not empty
   ((number? (car lst)) (+ (car lst) (sum-list (cdr lst)))) ;; the first item is a number, so we add it to the rest
   (else (sum-list (cdr lst))) ;; the first item was not a number, we just check the rest of the list
))

(define sum-them-all (lambda args
                       (sum-list args)))

(sum-them-all 10 20 30 40)
(sum-them-all 12 8 2)

;;No.3
(define average (lambda args
      (/ (apply sum-them-all args) (length args))))
(average 10 20 30 40)
(average 10 20 30)

;; No.4
(define maximum-of-many (lambda args
                          (if (<(length args) 2) ;;check to see if the list has more than one element 
                              (display "List arguments must be more than 1")
                              (apply max args))))

(maximum-of-many 10 20 30 40)
(maximum-of-many 12 8)
