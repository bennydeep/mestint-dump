;Header and description

(define (domain domain_name)

;remove requirements that are not needed
(:requirements :strips)


; un-comment following line if constants are needed
;(:constants )

(:predicates (adj ?square-1 ?square-2)
   
   (at ?what ?square)
   
)


;define actions here
(:action move
    :parameters (?who ?from ?to)
    :precondition (and (adj ?from ?to)
		       
		       (at ?who ?from))
    :effect (and (not (at ?who ?from))
		 (at ?who ?to))
    )
)