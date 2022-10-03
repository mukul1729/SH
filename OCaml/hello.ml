open Stdlib.Printf
let ord a =
    int_of_char a

let rec total a =
    match a with
    | [] -> 0
    | h :: t -> h + total t

let rec map f l =
    match l with
    | [] -> []
    | h :: t -> f h :: map f t

let t = (1,"one",'1')


type person = 
    {first: string;
     sur: string;
     age: int}

type colour = 
    | Red
    | Blue
    | RGB of int*int*int

type 'a tree = 
    | Leaf
    | Node of 'a tree * 'a * 'a tree

let rec total t = 
    match t with
    | Leaf -> 0
    | Node (l,x,r) -> total l + x + total r

let t =
        Node (Node (Leaf, 1, Leaf), 2, Node (Node (Leaf, 3, Leaf), 4, Leaf));;

let rec length lst =
    match lst with
    | [] -> 0
    | h :: t -> 1 + length t

let rec last lst k = 
    match lst with
    | [] -> None
    | h :: t -> if k = 1 then h else last t (k-1)

let rec rev l =
    match l with
    | [] -> []
    | h :: t -> rev t @ [h]


let isvowel c = 
    match c with
    | 'a' -> true
    | 'e' -> true
    | 'i' -> true
    | 'o' -> true
    | 'u' -> true
    | _ -> false

let max a b = 
    if a > b then a else b

let rec range a b = 
    if a > b then []
    else a :: range (a + 1) b;

