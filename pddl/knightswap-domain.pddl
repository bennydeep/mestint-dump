(define (domain springer_game)
  (:requirements :strips)
  (:predicates (adj ?square-1 ?square-2)
   
   (at ?what ?square))

  (:action start
    :parameters (?px ?py)
    :precondition (ready)
    :effect (and (not (ready)) (at ?px ?py) (not (clear ?px ?py))
		 (mark ?px ?py)))

  (:action RRD ; right-right-down
    :parameters (?px ?py ?fx ?fy ?ix)
    :precondition (and (at ?px ?py) (clear ?fx ?fy)
		       (inc ?px ?ix) (inc ?ix ?fx) (inc ?py ?fy))
    :effect (and (not (at ?px ?py)) (not (clear ?fx ?fy))
		 (at ?fx ?fy) (mark ?fx ?fy)))

  (:action RRU ; right-right-up
    :parameters (?px ?py ?fx ?fy ?ix)
    :precondition (and (at ?px ?py) (clear ?fx ?fy)
		       (inc ?px ?ix) (inc ?ix ?fx) (dec ?py ?fy))
    :effect (and (not (at ?px ?py)) (not (clear ?fx ?fy))
		 (at ?fx ?fy) (mark ?fx ?fy)))

  (:action LLD ; left-left-down
    :parameters (?px ?py ?fx ?fy ?ix)
    :precondition (and (at ?px ?py) (clear ?fx ?fy)
		       (dec ?px ?ix) (dec ?ix ?fx) (inc ?py ?fy))
    :effect (and (not (at ?px ?py)) (not (clear ?fx ?fy))
		 (at ?fx ?fy) (mark ?fx ?fy)))

  (:action LLU ; left-left-up
    :parameters (?px ?py ?fx ?fy ?ix)
    :precondition (and (at ?px ?py) (clear ?fx ?fy)
		       (dec ?px ?ix) (dec ?ix ?fx) (dec ?py ?fy))
    :effect (and (not (at ?px ?py)) (not (clear ?fx ?fy))
		 (at ?fx ?fy) (mark ?fx ?fy)))

  (:action RDD ; right-down-down
    :parameters (?px ?py ?fx ?fy ?iy)
    :precondition (and (at ?px ?py) (clear ?fx ?fy)
		       (inc ?px ?fx) (inc ?py ?iy) (inc ?iy ?fy))
    :effect (and (not (at ?px ?py)) (not (clear ?fx ?fy))
		 (at ?fx ?fy) (mark ?fx ?fy)))

  (:action RUU ; right-up-up
    :parameters (?px ?py ?fx ?fy ?iy)
    :precondition (and (at ?px ?py) (clear ?fx ?fy)
		       (inc ?px ?fx) (dec ?py ?iy) (dec ?iy ?fy))
    :effect (and (not (at ?px ?py)) (not (clear ?fx ?fy))
		 (at ?fx ?fy) (mark ?fx ?fy)))

  (:action LDD ; left-down-down
    :parameters (?px ?py ?fx ?fy ?iy)
    :precondition (and (at ?px ?py) (clear ?fx ?fy)
		       (dec ?px ?fx) (inc ?py ?iy) (inc ?iy ?fy))
    :effect (and (not (at ?px ?py)) (not (clear ?fx ?fy))
		 (at ?fx ?fy) (mark ?fx ?fy)))

  (:action LUU ; left-up-up
    :parameters (?px ?py ?fx ?fy ?iy)
    :precondition (and (at ?px ?py) (clear ?fx ?fy)
		       (dec ?px ?fx) (dec ?py ?iy) (dec ?iy ?fy))
    :effect (and (not (at ?px ?py)) (not (clear ?fx ?fy))
		 (at ?fx ?fy) (mark ?fx ?fy)))
  )