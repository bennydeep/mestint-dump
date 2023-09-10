(define (problem problem_fourknights_c8rfh5) (:domain fourknights_c8rfh5)
 (:objects
    sq-1-1 sq-1-2 sq-1-3
    sq-2-1 sq-2-2 sq-2-3
    sq-3-1 sq-3-2 sq-3-3
    w-knight
    b-knight

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

    (at w-knight sq-1-1)
    (at w-knight sq-3-1)
    (at b-knight sq-1-3)
    (at b-knight sq-3-3)
    (clear sq-2-1)
    (clear sq-3-2)
    (clear sq-2-3)
    (clear sq-1-2)
    (white)
    
   
)

(:goal (and (at w-knight sq-1-3) (at w-knight sq-3-3) (at b-knight sq-1-1) (at b-knight sq-3-1)))
  
)
