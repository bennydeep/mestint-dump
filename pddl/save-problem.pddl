(define (problem problem_name) (:domain domain_name)
 (:objects
   sq-1-1 sq-1-2 sq-1-3
   sq-2-1 sq-2-2 sq-2-3
   sq-3-1 sq-3-2 sq-3-3
   w-knight-1
   w-knight-2
   b-knight-1
   b-knight-2
   )

(:init
   (adj sq-1-1 sq-3-2) (adj sq-1-1 sq-2-3)
   (adj sq-3-2 sq-1-1) (adj sq-2-3 sq-1-1)
   (adj sq-3-1 sq-2-3) (adj sq-3-1 sq-1-2)
   (adj sq-2-3 sq-3-1) (adj sq-1-2 sq-3-1)
   (adj sq-3-3 sq-2-1) (adj sq-3-3 sq-1-2)
   (adj sq-2-1 sq-3-3) (adj sq-1-2 sq-3-3)
   (adj sq-1-3 sq-2-1) (adj sq-1-3 sq-3-2)
   (adj sq-2-1 sq-1-3) (adj sq-3-2 sq-1-3)

   (at w-knight-1 sq-1-1)
   (at w-knight-1 sq-3-1)
   (at b-knight-1 sq-1-3)
   (at b-knight-1 sq-3-3)
  
   
    ;todo: put the initial state's facts and numeric values here
)

(:goal (and (at w-knight-1 sq-1-3) (at w-knight-1 sq-3-3) (at b-knight-1 sq-1-3) (at b-knight-1 sq-3-1)))
  

;un-comment the following line if metric is needed
;(:metric minimize (???))
)
