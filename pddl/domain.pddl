(define (domain fourknights_c8rfh5)

(:requirements :strips :negative-preconditions)


(:predicates (adj ?square-1 ?square-2)
   
   (at ?what ?square)
   (clear ?square)
   (white)
)

(:action move-white
    :parameters (?who ?from ?to)
    :precondition (and (adj ?from ?to)
		       (clear ?to)
               (white)
		       (at ?who ?from))
    :effect (and (not (at ?who ?from))
		 (at ?who ?to) (clear ?from) (not(clear ?to)) (not(white)))
    )
(:action move-black
    :parameters (?who ?from ?to)
    :precondition (and (adj ?from ?to)
		       (clear ?to)
               (not(white))
		       (at ?who ?from))
    :effect (and (not (at ?who ?from))
		 (at ?who ?to) (clear ?from) (not(clear ?to)) (white))
    )
)