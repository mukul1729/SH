open Stdlib.Printf
let rec factorial n =
    match n with
    | 0  -> 1
    | _ -> n * factorial (n - 1)

let is_prime n =
    let n = max n (-n) in
    let rec is_not_divisor d =
      d * d > n || (n mod d <> 0 && is_not_divisor (d + 1))
    in
      is_not_divisor 2
  
let rec all_primes a b =
    if a > b then [] else
        let rest = all_primes (a + 1) b in
        if is_prime a then a :: rest else rest;;

let p() = let x = 50 in x*x
let () = printf "%d\n" (factorial 10);;
