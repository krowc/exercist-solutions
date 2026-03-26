(defpackage :lillys-lasagna
  (:use :cl)
  (:export :expected-time-in-oven
           :remaining-minutes-in-oven
           :preparation-time-in-minutes
           :elapsed-time-in-minutes))

(in-package :lillys-lasagna)

;; Define function expected-time-in-oven
(defun expected-time-in-oven () "Returns lasagna cooking time (in minutes)"
  '337)

;; Define function remaining-minutes-in-oven
(defun remaining-minutes-in-oven (time)
  "Derives remaining minutes in oven from function expected-time-in-oven.
  
    Param: time - actual minutes the lasagna has been in the oven."
  (- (expected-time-in-oven) time))

;; Define function preparation-time-in-minutes
(defun preparation-time-in-minutes (layers)
  "Calculates total lasagna preparation time (in minutes) given a number 
   of layers. Assumes each layer takes 19 minutes to prepare.
  
    Param: layers - number of layers of the lasagna"
  (* 19 layers))

;; Define function elapsed-time-in-minutes
(defun elapsed-time-in-minutes (layers time)
  "Calculates the total elapsed time by adding preparation time in minutes
   and the actual minutes the lasagna has been in the oven.
  
    Param: layers - number of layers of the lasagna
             time - actual minutes the lasagna has been in the oven."
  (+ (preparation-time-in-minutes layers) time))
