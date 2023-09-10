(define (domain fourknights_c8rfh5)

(:requirements :strips)


(:predicates (adj ?square-1 ?square-2)
   
   (at ?what ?square)
   (clear ?square)
)

(:action move
    :parameters (?who ?from ?to)
    :precondition (and (adj ?from ?to)
		       (clear ?to)
		       (at ?who ?from))
    :effect (and (not (at ?who ?from))
		 (at ?who ?to) (clear ?from) (not(clear ?to)))
    )
)