;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname square) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(define (sos x y)
  (+ (sq x)(sq y))
   )

(define (sq x)
  (* x x))

(sos 2 3)

(define (+ x y)
  (if (= x 0)
      y
      (+ (- 1+ x) (1+ y))))

(+3 4)